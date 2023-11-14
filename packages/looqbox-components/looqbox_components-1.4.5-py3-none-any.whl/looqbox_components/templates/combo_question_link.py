from looqbox.objects.looq_html import ObjHTML
from typing import List, Dict
from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ComboQuestionLink(LooqObject):
    """
    Create a looqbox ComboBox template.
    """

    def __init__(
            self,
            base_question: str,
            show_preview: bool = True,
            clear_button_text: str = "Limpar Filtros"
    ):
        """
        Args:
            base_question (str): A string to be displayed before the selected options.
            show_preview (bool, optional): A boolean to show or hide the preview of the selected options.
            clear_button_text (str, optional): A string to be displayed in the clear button.
        
        Returns:
            lq.ObjHTML: Return a Looqbox object JSON structure.
        
        Examples:
            >>> section_options = [{"label": "seção 1"}, {"label": "seção 2"}, {"label": "seção 3"}]
            >>> categories_option = [{"label": "eletrônicos"}, {"label": "comida", "search_value": "10000"}]
            >>> product_options = [{"label": "mouse", "filter": "na categoria eletrônicos"},
            >>>     {"label": "teclado", "filter": "na categoria eletrônicos"},
            >>>     {"label": "arroz", "filter": "na categoria comida"},
            >>>     {"label": "feijao", "filter": "na categoria 10000", "search_value": "10123"}
            >>> ]
            >>>
            >>> store_combo = ComboQuestionLink(base_question="venda", show_preview=True, clear_button_text="Limpar")
            >>> store_combo.add_combo_filter(box_tile="Seção", is_multiselect=True, option_header="na secao", box_content=section_options)
            >>> store_combo.add_combo_filter(box_tile="Categoria", is_multiselect=True, option_header="na categoria", box_content=categories_option)
            >>> store_combo.add_combo_filter(box_tile="Produto", is_multiselect=False, option_header="do produto", box_content=product_options)
        """
        super().__init__()
        self.base_question = base_question
        self.show_preview = str(show_preview).lower()
        self.clear_button_text = clear_button_text
        self._selects_lists: List[Dict] = []
    
    def add_combo_filter(self, box_tile: str, is_multiselect: bool, option_header: str, box_content: dict):
        """
        Add a combobox filter to the template.

        Args:
            box_tile (str): The name of the filter.
            is_multiselect (bool): A boolean to set if the filter is a multiselect.
            option_header (str): A string to be displayed before the selected options.
            box_content (dict): A dictionary with the options to be displayed in the filter.
        """
        self._selects_lists.append({"box_name": box_tile, "is_multiselect": is_multiselect,
                                    "value": option_header, "content": box_content})

    def _build_options_list(self, options_content, value):
        options = [(f"{{label: '{option.get('label')}', value: '{value} {option.get('label')}'"
                    f"{self._build_filter_condition_statement(option.get('filter'))}"
                    f"{self._build_search_value_condition_statement(option.get('search_value'))}}}")
                   for option in options_content]
        formated_combo_options = [", ".join(option for option in options)]
        return formated_combo_options[0]

    def _build_filter_condition_statement(self, filter: None | str) -> str:
        base_filter = ", filter: '"

        return "" if filter is None else base_filter + filter + "'"

    def _build_search_value_condition_statement(self, search_value: None | str) -> str:
        base_search_value = ", searchValue: '"

        return "" if search_value is None else base_search_value + search_value + "'"

    def _build_select(self, select):
        options = self._build_options_list(
            select.get("content"), select.get("value", ""))
        select_box_html = ("{name: '" + select.get("box_name", "") + "', multiSelect: " +
                           str(select.get("is_multiselect", "false")).lower() + ", options: [" + options + "]}")
        return select_box_html

    def _build_component_html(self):
        selects = ", ".join([self._build_select(select)
                             for select in self._selects_lists])

        combo_question_link = self._enrich_base_template(selects)

        return ObjHTML(combo_question_link)

    def _enrich_base_template(self, selects):
        return self._get_combo_question_link_html_template().format(self.base_question,
                                                                    self.show_preview,
                                                                    self.clear_button_text,
                                                                    selects)

    def _get_combo_question_link_html_template(self) -> str:
        import os
        html_template_path = os.path.join(os.path.dirname(
            __file__), "resources", "combo_question_link.html")
        try:
            with open(html_template_path, "r") as template_file:
                combo_question_link_template = "".join(
                    template_file.readlines())
                template_file.close()
            return combo_question_link_template
        except IOError as error:
            raise error

    def to_json_structure(self, visitor: BaseRender):
        self.combobox = self._build_component_html()
        return self.combobox.to_json_structure(visitor)
