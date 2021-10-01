from dataclasses import dataclass


@dataclass
class DataSet(object):
    context: str
    fname: str
    train: object
    val: object
    ksx1001 : str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def val(self) -> object: return self._val

    @val.setter
    def val(self, val): self._val = val

    @property
    def ksx1001(self) -> str : return self._ksx1001

    @ksx1001.setter
    def ksx1001(self, ksx1001): self._ksx1001 = ksx1001



