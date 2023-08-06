from code_mixed_text_toolkit.utils.demo_utils import remainder

class CodeMixedTextToolkit:
  """
  Instantiate a CodeMixedTextToolkit operation.
  """

  def demo_function(self, num):
    """
    A demo function to get numbers described.

    :param num: The number
    :type num: int

    :return: Description of the number
    :rtype: str
    """

    message = ""
    if(remainder(num,2) == 0):
      message = "The number you gave is even."
    else:
      message = "The number you gave is odd."

    return message