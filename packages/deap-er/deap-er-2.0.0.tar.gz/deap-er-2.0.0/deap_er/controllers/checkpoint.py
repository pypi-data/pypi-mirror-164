# ====================================================================================== #
#                                                                                        #
#   MIT License                                                                          #
#                                                                                        #
#   Copyright (c) 2022 - Mattias Aabmets, The DEAP Team and Other Contributors           #
#                                                                                        #
#   Permission is hereby granted, free of charge, to any person obtaining a copy         #
#   of this software and associated documentation files (the "Software"), to deal        #
#   in the Software without restriction, including without limitation the rights         #
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell            #
#   copies of the Software, and to permit persons to whom the Software is                #
#   furnished to do so, subject to the following conditions:                             #
#                                                                                        #
#   The above copyright notice and this permission notice shall be included in all       #
#   copies or substantial portions of the Software.                                      #
#                                                                                        #
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR           #
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,             #
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE          #
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER               #
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,        #
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE        #
#   SOFTWARE.                                                                            #
#                                                                                        #
# ====================================================================================== #
from typing import Optional, Union
from pathlib import Path
import numpy as np
import random
import time
import uuid
import dill
import os


__all__ = ['Checkpoint']


# ====================================================================================== #
class Checkpoint:
    """
    This class can be used to save and load evolution progress to and from files.
    It's implemented as a lightweight wrapper around the builtin :code:`open()` function.
    Objects are (de-)serialized using the `dill <https://pypi.org/project/dill/>`_ library.
    Only those objects which have been set as attributes of the checkpoint object are
    persisted to disk. The target save file is assigned on object instantiation.
    Checkpoint objects automatically persist also the *RNG* states of the
    :mod:`random` and :mod:`numpy.random` modules.

    :param file_name: The name of the checkpoint file.
        By default, a random UUID + :code:`.dcpf` extension is used.
    :param dir_path: The path to the checkpoint directory. By default,
        the current working directory + :code:`/deap-er` is used.
    :param autoload: If True **and** the checkpoint file exists, loads the
        file during initialization, optional. The default value is True.
    :param make_dir: If True, the target directory is recursively created
        on save, if it does not exist. The default value is True.
    :param raise_errors: If True, errors are propagated, optional.
        By default, errors are not propagated and False is returned instead.
    """
    # -------------------------------------------------------- #
    _dir_ = 'deap-er'  # Checkpoint Directory
    _ext_ = '.dcpf'    # [D]eaper [C]heck [P]oint [F]ile
    _omit_ = ['_last_op_']

    _rand_state_: object = None
    _numpy_state_: dict = None
    _range_counter_: int = 0
    _save_freq_: float = 60.0
    _last_op_: str = 'none'

    # -------------------------------------------------------- #
    def __init__(self,
                 file_name: Optional[str] = None,
                 dir_path: Optional[Path] = None,
                 autoload: Optional[bool] = True,
                 make_dir: Optional[bool] = True,
                 raise_errors: Optional[bool] = False):
        if file_name is None:
            file_name = str(uuid.uuid4()) + self._ext_
        if dir_path is None:
            dir_path = Path(os.getcwd()).resolve()
            dir_path = dir_path.joinpath(self._dir_)
        self.file_path = dir_path.joinpath(file_name)
        self.raise_errors = raise_errors
        self.make_dir = make_dir
        if autoload is True:
            self.load()

    # -------------------------------------------------------- #
    def load(self) -> bool:
        """
        Loads objects from the checkpoint file and sets them as attributes of ``self``.

        :raise IOError: If the operation failed and :code:`self.raise_errors` is True.
        :raise dill.PickleError: If the operation failed and :code:`self.raise_errors` is True.
        :return: True if the operation completed successfully, False otherwise.
        """
        try:
            with open(self.file_path, 'rb') as f:
                self.__dict__ = dill.load(f)
            random.setstate(self._rand_state_)
            np.random.set_state(self._numpy_state_)
        except (IOError, dill.PickleError) as ex:
            if self.raise_errors:
                raise ex
            self._last_op_ = 'load_error'
            return False
        self._last_op_ = 'load_success'
        return True

    # -------------------------------------------------------- #
    def save(self) -> bool:
        """
        Saves the attributes of ``self`` into the checkpoint file.
        If the file already exists, it will be overwritten.
        If the target directory does not exist, it will be created recursively.

        :raise IOError: If the operation failed and :code:`self.raise_errors` is True.
        :raise dill.PickleError: If the operation failed and :code:`self.raise_errors` is True.
        :return: True if the operation completed successfully, False otherwise.
        """
        try:
            self._rand_state_ = random.getstate()
            self._numpy_state_ = np.random.get_state()
            if self.make_dir:
                self.file_path.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )
            with open(self.file_path, 'wb') as f:
                _dict_ = vars(self).copy()
                for key in self._omit_:
                    _dict_.pop(key, None)
                dill.dump(_dict_, f)
        except (IOError, dill.PickleError) as ex:
            if self.raise_errors:
                raise ex
            self._last_op_ = 'save_error'
            return False
        self._last_op_ = 'save_success'
        return True

    # -------------------------------------------------------- #
    def range(self, generations: int) -> range:
        """
        A special generator method that behaves almost like the builtin :code:`range()`
        function, but it accepts only a single argument of the number of generations to
        compute. It is intended to be used in a ``for`` loop to iterate over the main
        evolutionary process. The checkpoint is saved to disk every ``self.save_freq``
        seconds and also at the end of the loop, if saving is enabled. The saving
        frequency can be changed while the ``for`` loop is running. The values of
        the range counter are automatically determined from the current *(loaded)*
        state of the checkpoint object.

        :param generations: The amount of generations to compute.
        :return: A generator that yields the integer values of the internal counter.
        """
        if generations < 0:
            raise ValueError(
                'Iterations argument cannot be a negative number.'
            )
        from_ = self._range_counter_ + 1
        to_excl = self._range_counter_ + generations + 1

        if self.save_freq == -1:             # saving is disabled
            for i in range(from_, to_excl):
                yield i
                self._range_counter_ = i
        else:                                # saving is enabled
            last_save = time.time()
            for i in range(from_, to_excl):
                yield i
                self._range_counter_ = i
                now = time.time()
                elapsed = now - last_save
                if elapsed >= self._save_freq_:
                    last_save = now
                    self.save()
            self.save()

    # -------------------------------------------------------- #
    @property
    def save_freq(self) -> float:
        """
        The time in seconds after which to periodically save the checkpoint to
        a file, when the ``range()`` function is being executed in a ``for`` loop.
        Setting the value to ``-1`` disables saving. Accepts ``int`` and ``float``
        types as values. Float-types allow sub-second timing precision.

        :return: The current saving frequency period, in
            seconds. The default value is 60 seconds.
        """
        return self._save_freq_

    @save_freq.setter
    def save_freq(self, value: Union[int, float]) -> None:
        self._save_freq_ = float(value)

    # -------------------------------------------------------- #
    @property
    def last_op(self) -> str:
        """
        | Returns the status of the last operation performed on the checkpoint object.
        | Possible string-type return values are:

            * *none*
            * *load_success*
            * *load_error*
            * *save_success*
            * *save_error*
        """
        return self._last_op_

    # -------------------------------------------------------- #
    def is_loaded(self) -> bool:
        """
        Shorthand for ``checkpoint.last_op == 'load_success'``.

        :return: True if the checkpoint was successfully loaded from file.
        """
        return self._last_op_ == 'load_success'

    # -------------------------------------------------------- #
    def is_saved(self) -> bool:
        """
        Shorthand for ``checkpoint.last_op == 'save_success'``.

        :return: True if the checkpoint was successfully saved to file.
        """
        return self._last_op_ == 'save_success'
