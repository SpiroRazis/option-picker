from abc import ABC, abstractmethod


class DataContainer(ABC):

    @abstractmethod
    def getData(self):
        pass

    #@abstractmethod
    #def setData(self, data):
    #    pass

    @abstractmethod
    def isValidContent(self, content):
        pass


class OptionList(DataContainer):

    def __init__(self):
        self._options = []

    def getData(self):
        return self._options

    def isValidContent(self, content):
        if isinstance(content, OptionData):
            check_key_object, check_text_obj = content.getData()
            for option in self._options:
                if (check_key_object == option.getOptionKey()):
                    raise ValueError("Pre-Existing Key: %s" % str(check_key_object))
                elif (check_text_obj == option.getTextData()):
                    raise ValueError("Pre-Existing Text: %s" % str(check_text_obj))
            return True
        else:
            raise TypeError("Not an Option!")

    def addOption(self, option_object):
        try:
            if self.isValidContent(option_object):
                self._options.append(option_object)
                #self._addOptionHelper(option_object)
                # print("appended")
                # self._printOptions()
        except (ValueError, TypeError) as e:
            print(e)
            raise ValueError("Unable to Add Entry")

    def getOptionByKey(self, key_string):
        # print(key_string)
        for option in self._options:
            if key_string == option.getOptionKey().getData():
                return option
        raise KeyError("Key Not Found.")

    def __len__(self):
        return len(self._options)

    def _printOptions(self):
        for option in self._options:
            print(str(option))

    # SEARCH OPTION LIST FOR INPUT STRING
    def __contains__(self, object):
        if isinstance(object, OptionData):
            # SEARCH OPTION LIST FOR BOTH KEY AND TEXT
            return self._containsHelperOptionData(object)
        elif isinstance(object, OptionKey):
            return self._containsHelperOptionKey(object)
        elif isinstance(object, TextData):
            return self._containsHelperTextData(object)
        return False

    def _containsHelperOptionData(self, check_option):
        check_key_object, check_text_data_obj = check_option.getData()
        has_key_data = self._containsHelperOptionKey(check_key_object)
        has_text_data = self._containsHelperTextData(check_text_data_obj)
        return has_key_data and has_text_data

    def _containsHelperOptionKey(self, check_key_object):
        checking_string = str(check_key_object)
        for option in self._options:
            key_object, text_data_obj = option.getData()
            if (checking_string == str(key_object)):
                return True
        return False

    def _containsHelperTextData(self, check_text_data_obj):
        checking_string = str(check_text_data_obj)
        for option in self._options:
            key_object, text_data_obj = option.getData()
            if (checking_string == str(text_data_obj)):
                return True
        return False


class OptionData:

    def __init__(self, key_string, text_string):
        try:
            self.key_object = OptionKey(key_string)
            self.text_data_obj = TextData(text_string)
        except ValueError as e:
            print(e)
            raise ValueError("Invalid Option Data")

    def getOptionKey(self):
        return self.key_object

    def getTextData(self):
        return self.text_data_obj

    def getData(self):
        return self.getOptionKey(), self.getTextData()

    def __str__(self):
        return str(self.key_object) + ") " + str(self.text_data_obj)

    def __eq__(self, option_data_obj):
        if isinstance(option_data_obj, OptionData):
            check_key_object, check_text_obj = option_data_obj.getData()
            return ((self.key_object == check_key_object) and \
                    (self.text_data_obj == check_text_obj))
        return False


class OptionKey(DataContainer):

    def __init__(self, key_string):
        try:
            if self.isValidContent(key_string):
                self.key_string = key_string
        except (ValueError, TypeError) as e:
            print(e)
            raise ValueError("Invalid Key Data.")

    def getData(self):
        return str(self)

    def isValidContent(self, content):
        if isinstance(content, str):
            if content:
                for char in content:
                    if not (char.isalpha() or char.isdigit()):
                        raise ValueError("Invalid Character: %s" % char)
                return True
            else:
                raise ValueError("Empty String")
        else:
            raise TypeError("Not a String!")

    def __str__(self):
        return self.key_string

    def __eq__(self, key_object):
        if isinstance(key_object, OptionKey):
            return str(self) == str(key_object)
        return False



class TextData(DataContainer):

    def __init__(self, text_string):
        try:
            if self.isValidContent(text_string):
                self.text = text_string
        except (ValueError, TypeError) as e:
            print(e)
            raise ValueError("Invalid Text Data")

    def getData(self):
        return str(self)

    def isValidContent(self, content):
        if isinstance(content, str):
            if content:
                return True
            else:
                raise ValueError("Empty Text Data")
        else:
            raise TypeError("Not a String!")

    def __str__(self):
        return self.text

    def __eq__(self, text_data_obj):
        if isinstance(text_data_obj, TextData):
            return str(self) == str(text_data_obj)
        return False
