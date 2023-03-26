import logging

class Calculator:
    """_summary_
    """
    
    def __init__(self):
        logging.info(f"Instantiating {self.__class__.__name__}")
        self.expression = ""
        self.result = ""
    
    def delete(self):
        logging.debug(f"Deleting last character ({self.expression[-1]})")
        self.expression = self.expression[:-1]
        
    def clear(self):
        logging.info(f"Clearing expression")
        self.expression = ""
        
    def add_to_expression(self, entry):
        logging.debug(f"Appending {entry} to expression")
        self.expression += entry
        
    def update_expression(self, new_expression):
        logging.debug(f"Updating expression to result or key input")
        self.expression = new_expression
    
    def equals(self):
        logging.info(f"Evaluating {self.expression}")
        try:
            self.result = str(eval(self.expression))
            self.update_expression(self.result)
        except Exception as e:
            logging.warning(f"{e}")
        