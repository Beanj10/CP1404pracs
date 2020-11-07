
from kivy.app import App
from kivy.lang import Builder


Miles_Km = 1.609


class MilesConverterApp(App):
    def build(self):
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self):
        number = self.get_validated_miles()
        ans = number * Miles_Km
        self.root.ids.output_label.text = str(ans)

    def handle_increment(self, value):
        number = self.get_validated_miles() + value
        self.root.ids.input_miles.text = str(number)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()