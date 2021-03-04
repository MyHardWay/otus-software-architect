from BaseHandler import BaseHandler

class TxtHandler(BaseHandler):

    def can_handle(self, file_input: str) -> bool:
        return True if file_input.endswith('txt') else False

    def handle(self, file_input: str, file_output) -> bool:
        if self.can_handle(file_input):
            self._log_handle(file_input)
            self.save_to_file(file_input, file_output)
        elif self.next_handler:
            self.next_handler.handle(file_input, file_output)