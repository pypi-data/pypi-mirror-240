import re
from datetime import date
from typing import List, Dict, Any

from payslip_parser.parsers.base_payslip_parser import BasePayslipParser
from payslip_parser.text_blocks.base_text_block import BaseTextBlock
from payslip_parser.configuration.config import RegionBounds
from payslip_parser.text_blocks.idf_text_block import IDFTextBlock


class IDFPayslipParser(BasePayslipParser):
    def _get_payslip_name(self, payslip_path: str) -> str:
        filename = payslip_path.split('/')[-1].split('\\')[-1].split('.')[0]
        month = filename[8:-5] if len(filename[8:-5]) == 2 else '0' + filename[8:-5]  # add leading zero to month
        payslip_name = filename[:7] + '__' + filename[-5:-1] + '-' + month
        return payslip_name

    def _get_worker_id(self, header_blocks: List[BaseTextBlock]) -> str:
        idf_personal_number_block = header_blocks[4]
        assert idf_personal_number_block.region_name == 'personal_data'
        return idf_personal_number_block.parsed_text['numbers']

    def _get_worker_name(self, header_blocks: List[BaseTextBlock]) -> str:
        worker_name_block = header_blocks[0]
        assert worker_name_block.region_name == 'to'
        return worker_name_block.parsed_text['alphas'][4:]  # get rid of מ.א. prefix

    def _get_payslip_date(self, header_blocks: List[BaseTextBlock]) -> date:
        payslip_date_block = header_blocks[3]
        assert payslip_date_block.region_name == 'payslip_date'
        return date(
            year=int(payslip_date_block.parsed_text['numbers'][-4:]),
            month=int(payslip_date_block.parsed_text['numbers'][:-4]),
            day=1
        )

    def _get_additional_metadata(self, header_blocks: List[BaseTextBlock]) -> Any:
        payment_unit_block = header_blocks[2]
        assert payment_unit_block.region_name == 'to'

        national_id_block = header_blocks[5]
        assert national_id_block.region_name == 'personal_data'

        bank_name_block = header_blocks[6]
        account_details_block = header_blocks[7]
        assert bank_name_block.region_name == account_details_block.region_name == 'bank_details'

        return {
            'payment_unit': payment_unit_block.parsed_text['numbers'],  # יחתש
            'national_id': national_id_block.parsed_text['numbers'][:9],  # remove יחתש suffix, if exists
            'bank_details': {
                'bank_name': bank_name_block.parsed_text['alphas'],
                'branch_code': bank_name_block.parsed_text['numbers'],
                'branch_name': account_details_block.parsed_text['alphas'],
                'account_number': account_details_block.parsed_text['numbers']
            }
        }

    def _instantiate_text_block(self, block_id: int, region_bounds: RegionBounds, region_name: str, is_header: bool,
                                text: str) -> BaseTextBlock:
        return IDFTextBlock(block_id, region_bounds, region_name, is_header, text)

    def _body_block_to_record(self, block: IDFTextBlock) -> Dict:
        assert not block.is_header

        region_name = block.region_name
        alphas = block.parsed_text['alphas']
        numbers = block.parsed_text['numbers']

        if region_name == 'net_monthly_payment':
            return {'שכר חודשי נטו': float(numbers)}

        if region_name == 'net_differences':
            return {'הפרשים נטו': float(numbers)}

        if region_name == 'total_transfer_to_bank':
            return {'סהכ העברה לבנק': float(numbers)}

        if alphas == '':
            return {}

        if region_name == 'raw_data':
            return self._parse_raw_data_region(alphas, numbers)

        if region_name == 'monthly_payments':
            return self._parse_monthly_regions(alphas, numbers, negate_sums=False)

        if region_name == 'monthly_reductions':
            return self._parse_monthly_regions(alphas, numbers, negate_sums=True)

        if region_name == 'payments_differences':
            return self._parse_differences_regions(alphas, numbers, negate_total=False)

        if region_name == 'reductions_differences':
            return self._parse_differences_regions(alphas, numbers, negate_total=True)

    def _parse_raw_data_region(self, alphas: str, numbers: str) -> Dict:
        """Parses נתונים גולמיים"""
        # TODO improve this function
        if alphas.startswith('רגיל') or alphas.startswith('חובה'):
            start_date = date(
                day=int(numbers[:2]),
                month=int(numbers[2:4]),
                year=int(f'{self.config.century_prefix}{numbers[4:]}')
            )
            return {
                'שם הנתון': alphas[4:],
                'ערך הנתון': alphas[:4],
                'ת. תחילה': start_date,
            }

        if alphas.startswith('דחית שרות החובה'):
            start_date = date(
                day=int(numbers[:2]),
                month=int(numbers[2:4]),
                year=int(f'{self.config.century_prefix}{numbers[4:]}')
            )
            return {
                'שם הנתון': alphas[14:],
                'ערך הנתון': alphas[:14],
                'ת. תחילה': start_date,
            }

        return {
            'unknown': f'{alphas}{numbers}',
        }

    @staticmethod
    def _parse_monthly_regions(alphas: str, numbers: str, negate_sums: bool) -> Dict:
        """Parses תשלומים שוטפים or ניכויים שוטפים"""
        split_numbers = numbers.split('.')
        if len(split_numbers) == 2:  # only סכום נוכחי
            previous_sum = None
            current_sum = float(numbers)
        elif len(split_numbers) == 3:  # both סכום נוכחי and סכום קודם
            current_sum = float(split_numbers[0] + '.' + split_numbers[1][:2])  # shekels.agorot
            previous_sum = float(split_numbers[1][2:] + '.' + split_numbers[2])  # shekels.agorot
        else:
            raise RuntimeError(f'Error parsing {alphas}!')

        if negate_sums:  # negate sums if we are parsing ניכויים
            current_sum = -current_sum
            previous_sum = -previous_sum if previous_sum is not None else None

        return {
            'שם התשלום/ניכוי': alphas,
            'סכום קודם': previous_sum,
            'סכום נוכחי': current_sum,
        }

    def _parse_differences_regions(self, alphas: str, numbers: str, negate_total: bool) -> Dict:
        """Parses הפרשי תשלומים or הפרשי ניכויים"""
        pattern = '(?P<from_DD>[0-9]{2})(?P<from_MM>[0-9]{2})(?P<from_YY>[0-9]{2})' \
                  '(?P<to_DD>[0-9]{2})(?P<to_MM>[0-9]{2})(?P<to_YY>[0-9]{2})' \
                  '(?P<shekels>[0-9]{1,5}).(?P<agorot>[0-9]{2})'
        m = re.match(pattern, numbers)
        if m:
            from_date = date(
                year=int(f'{self.config.century_prefix}{m.group("from_YY")}'),
                month=int(m.group("from_MM")),
                day=int(m.group("from_DD"))
            )
            to_date = date(
                year=int(f'{self.config.century_prefix}{m.group("to_YY")}'),
                month=int(m.group("to_MM")),
                day=int(m.group("to_DD"))
            )
            total = float(f'{m.group("shekels")}.{m.group("agorot")}')
        else:
            raise RuntimeError(f'Error parsing {alphas}!')

        if negate_total:
            total = -total

        return {
            'שם הפרש תשלום/ניכוי': alphas,
            'תשלום/ניכוי מתאריך': from_date,
            'תשלום/ניכוי עד תאריך': to_date,
            'סכום הפרשי תשלומים/ניכויים': total,
        }
