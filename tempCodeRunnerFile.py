lst_len = len(self.text_lst)
        buttons = []
        for i in range(lst_len):
            button = Button2.Button2(113, 11 + 30 * i, 15, 15, "+", None, self.button_color, self.button_color_hover, self.button_text_color, self.add_value, value = self.value_lst[i])
           