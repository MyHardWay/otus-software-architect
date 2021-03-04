from BaseHandler import BaseHandler

class XmlHandler(BaseHandler):

    def can_handle(self, file_input: str) -> bool:
        return True if file_input.endswith('xml') else False

    def handle(self, file_input: str, file_output: str) -> bool:
        if self.can_handle(file_input):
            self._log_handle(file_input)
            self.save_to_file(file_input, file_output)
        elif self.next_handler:
            self.next_handler.handle(file_input, file_output)