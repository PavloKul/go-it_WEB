from abc import ABC, abstractmethod
import json
import pickle


class SerializationInterface(ABC):
    @abstractmethod
    def serialize(self, data, file_name):
        pass


class SerializationJSON(SerializationInterface):
    def serialize(self, data, file_name='data.json'):
        with open (file_name, 'w') as fh:
            json.dump(data, fh)
    
            
class SerializationBin(SerializationInterface):
    def serialize(self, data, file_name='data.bin'):
        with open(file_name, 'wb') as fh:
            pickle.dump(data, fh)
            

if __name__ == '__main__':
    data = {'a':1,'b':4}
    a = SerializationJSON()
    a.serialize(data)
    b = SerializationBin()
    b.serialize(data)
