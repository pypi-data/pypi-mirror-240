from __future__ import annotations
import logging
from typing import Iterable
from django.utils.html import format_html

from .models import Item, PropNature

logger = logging.getLogger(__name__)


class ItemDisplay:
    def __init__(self, item: Item):
        self.item = item

    def sections(self):
        if not self.item.data:
            return
        
        all_cprops = self.item.category.categoryprop_set.all()
        root_cprops = [cp for cp in all_cprops if not '.' in cp.prop_fullname]

        default_section = ItemSection()
        sections = [default_section]

        root_data = self.item.data_manager.decode()
        used_fullnames = set()

        for root_cp in root_cprops:
            if root_cp.prop_name in root_data:
                used_fullnames.add(root_cp.prop_fullname)
                value = root_data[root_cp.prop_name]
                
                if root_cp.prop_nature == PropNature.SECTION and isinstance(value, dict):
                    section_data = value
                    section = ItemSection(root_cp.prop_name)
                    sections.append(section)

                    section_cprops = [cp for cp in all_cprops if cp.prop_fullname.startswith(f'{root_cp.prop_name}.')]
                    for section_cp in section_cprops:
                        if section_cp.prop_name in section_data:
                            used_fullnames.add(section_cp.prop_fullname)
                            value = section_data[section_cp.prop_name]
                                    
                            pv = ItemPropValues(section_cp.prop_name, value, section_cp.prop_nature)
                            section.propvalues.append(pv)

                    for key in sorted(section_data.keys()):
                        if not f'{root_cp.prop_name}.{key}' in used_fullnames:
                            pv = ItemPropValues(key, section_data[key])
                            section.propvalues.append(pv)
                        
                else:
                    pv = ItemPropValues(root_cp.prop_name, value, root_cp.prop_nature)
                    default_section.propvalues.append(pv)

        for key in sorted(root_data.keys()):
            if not key in used_fullnames:
                pv = ItemPropValues(key, root_data[key])
                default_section.propvalues.append(pv)

        return sections


class ItemSection:
    def __init__(self, title: str = None):
        self.title = title
        self.propvalues: list[ItemPropValues] = []


class ItemPropValues:
    def __init__(self, name: str, value, nature: PropNature = None):
        self.name = name
        self.value = value


    def html(self):            
        if isinstance(self.value, dict) and len(self.value) > 0 and all(isinstance(value, dict) for value in self.value.values()):
            # Display as table
            rows = [{"_": key, **self.value[key]} for key in sorted(self.value.keys())]
            headers = self._get_headers_from_dicts(rows)
            return self._format_table(headers, rows)
        
        else:
            return self._format_value(self.value)
        

    def _format_table(self, headers: list[str], rows: Iterable[dict]):
        args = []
        h = '<table class="table table-sm" data-toggle="table">'
        h += '<thead><tr>'
        for header in headers:
            h += f'<th data-sortable="true">{header}</th>'
        h += '</tr></thead>'
        h += '<tbody>'
        for row in rows:
            h += '<tr>'
            for header in headers:
                h += '<td>{}</td>'
                args.append(self._format_value(row.get(header)))
            h += '</tr>'
        h += '</tbody>'
        h += '</table>'
        return format_html(h, *args)


    def _format_value(self, value) -> str:
        if value is None:
            return format_html('')
        elif isinstance(value, list):
            result = None
            for sub in value:
                if result:
                    result = format_html('{}\n<br/>{}', result, self._format_value(sub))
                else:
                    result = self._format_value(sub)
            return result
        elif isinstance(value, dict):
            return format_html('<small><code>{}</code></small>', value)
        elif isinstance(value, Item):
            return format_html('<a href="{}">{}</a>', value.get_absolute_url(), value)
        elif isinstance(value, str) and value.startswith(('http://', 'https://')):
            return format_html('<a href="{}">{}</a>', value, value)
        else:
            return str(value) # TODO: use Django function instead of this


    def _get_headers_from_dicts(self, values: Iterable[dict]):
        headers = []
        for value in values:
            for key in value:
                if not key in headers:
                    headers.append(key)
        return headers
