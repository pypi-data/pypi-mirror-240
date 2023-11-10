from typing import List
import warnings
import numpy as np
import quaternion

from skanym.core.math.constants import VERY_HIGH_A_TOL, VERY_HIGH_R_TOL
from skanym.core.math.transform import Transform
from skanym.core.animate.key import Key


class Curve:
    """Class to represent an animation curve.

    It is a list of keys that are used to animate a value over time.
    It contains a list of keys as its single attribute and provides
    methods to manipulate the keys and interpolate between them.

    The keys are sorted by increasing time when added via the
    add_key() or set_key_at() methods.

    All keys in the animation curve must be of the same type.
    A curve object can hold keys of any type.
    However, the type of keys supported for interpolation are:
    - int
    - float
    - list or array of floats
    - numpy.quaternion
    - Transform

    Curves do not support keys with a negative time.

    Attributes:
    ----------
    keys : (Key) list
        The keys that make up the animation curve.
        They are sorted by ascending time whenever a new one is added.
    """

    def __init__(self, keys: List[Key] = []):
        """**Default constructor for the Curve class.**

        Parameters:
        ----------
        keys : (Key) list, optional
            The keys of the animation curve, by default empty list.
        """
        # Goes through the process of adding the keys one by one instead of copying the list
        # To ensure that keys go through the checks in the add_key() method.
        self.keys = []
        for key in keys:
            self.add_key(key)

    def validate_for_interpolation(self):
        """
        Verifies that the animation curve is valid for interpolation.
        A valid animation must:
        - contain time values between 0 and 1 included.
        - contain at least 1 key.
        - contain keys of the same type.
        - not contain more than 1 key at a given time.
        - be sorted by increasing time.

        Raises:
        ----------
        ValueError
            If the animation curve is not valid.
        """
        if self.is_empty():
            raise ValueError("Animation curve must contain at least 1 key.")

        lowest_key_time = 0.0
        previous_key_time = None
        first_key_type = self.keys[0].get_type()
        for key in self.keys:
            if key.time < 0.0 or key.time > 1.0:
                raise ValueError(
                    f"Invalid time {key.time}. Time must be between 0.0 and 1.0 included."
                )

            if key.time < lowest_key_time:
                raise ValueError(
                    f"Invalid time. Keys must be sorted by increasing time."
                )
            lowest_key_time = key.time

            if not previous_key_time is None:
                if np.isclose(
                    key.time,
                    previous_key_time,
                    rtol=VERY_HIGH_R_TOL,
                    atol=VERY_HIGH_A_TOL,
                ):
                    raise ValueError(
                        f"Invalid time {key.time}. Animation curve cannot contain 2 keys with times within 1e-3 of each other."
                    )
            previous_key_time = key.time

            if key.get_type() != first_key_type:
                raise ValueError(
                    f"Invalid key type. All keys must be of the same type."
                )

    def is_empty(self):
        """Returns whether the animation curve is empty.

        Returns:
        ----------
        bool
            True if the animation curve is empty, False otherwise.
        """
        return self.get_key_count() == 0

    def get_key_count(self) -> int:
        """Returns the number of keys in the animation curve.

        Returns:
        ----------
        int
            The number of keys in the animation curve.
        """
        return len(self.keys)

    def normalize_single_key_time(self, key, ratio: float):
        """
        Normalizes the time of a single key.

        Parameters:
        ----------
        key_time : float
            The time of the key to normalize.
        ratio : float
            The normalization ratio.
        """
        if ratio == 0:
            # TODO Error ratio is 0, no normalization needed.
            pass
        else:
            key.time /= ratio

    def normalize_times(self, ratio: float):
        """Normalizes the animation curve.
        Effectively divides the time of each key by the ratio.
        This is mostly used to restrict the time of the keys between 0 and 1 included.

        Parameters:
        ----------
        ratio : float
            The normalization ratio.
        """
        for key in self.keys:
            self.normalize_single_key_time(key, ratio)

    def normalize_values(self, ratio):
        """Normalizes the values of the animation curve.
        Effectively multiplies the value of each key by the given ratio.
        This used to restrict the values of the keys to a specific range.

        Note:
        ----------
        This method is only supported for keys of type int, float.

        Parameters:
        ----------
        ratio : float
            The ratio to normalize the animation curve by.

        Warns:
        ----------
        Warning
            If the animation curve contains keys of type other than int or float.

        Raises:
        ----------
        ZeroDivisionError
            If the ratio is 0.
        """
        if ratio == 0:
            raise ZeroDivisionError("Invalid ratio. Cannot normalize by 0.")

        if not self.is_empty():
            if self.keys[0].get_type() in [int, float, np.float32, np.float64]:
                for key in self.keys:
                    key.value /= ratio
            else:
                warnings.warn(
                    f"Cannot normalize values of type {str(self.keys[0].get_type())}. Only int and float supported.",
                    stacklevel=2,
                )

    def add_key(self, key: Key):
        """Adds a key to the animation curve.

        Note:
        ----------
        this method uses the get_key_at() method to check if a key already exists at the given time.
        See the documentation of that method for more details about the tolerance values of the check.
        Automatically sorts the keys by increasing time after a successful addition.

        Raises:
        ----------
        ValueError
            If the time of the key is negative.
        ValueError
            If type of the key does not match the type of the keys in the curve.
        ValueError
            If a key with the same time already exists in animation curve.
            To edit an existing key, use the set_key_at() method instead.

        Parameters:
        ----------
        key : Key
            The key to be added to the animation curve.
        """

        # Key time positiveness check
        if key.time < 0.0:
            raise ValueError(
                f"Invalid key time {key.time}. Key time must be greater or equal to 0."
            )

        # Key type check
        def _validate_key_type(self, key_type: type) -> bool:
            first_key_type = self.keys[0].get_type()

            valid_types = [
                int,
                float,
                np.float32,
                np.float64,
                np.quaternion,
                np.ndarray,
                list,
            ]

            if key_type != first_key_type:
                raise ValueError(
                    f"Key type ({str(key.get_type())}) does not match the type of the first key of the animation curve ({str(self.keys[0].get_type())})."
                )
            elif key_type not in valid_types:
                raise ValueError(
                    f"Invalid key type {str(key_type)}. Key type must be one of {str(valid_types)}."
                )

        if not self.is_empty():
            _validate_key_type(self, key.get_type())

        # Key time uniqueness check
        if self.get_key_at(key.time) is not None:
            raise ValueError(
                f"Key at the given time {str(key.time)} already exists in animation curve. \
            Use set_key_at() to change the value of an existing key."
            )

        self.keys.append(key)
        self.keys.sort(key=lambda key: key.time)

    def set_key_at(self, time, value):
        """Sets the value of the key at the given time.
        If no key exists at the given time, a new key is added
        via the add_key() method.

        Note:
        ----------
        this method uses the get_key_at() method to check if a key already exists at the given time.
        See the documentation of that method for more details about the tolerance values of the check.

        Parameters:
        ----------
        time : float
            The time of the key to be set.
        value : Key
            The new value of the key.
        """
        key = self.get_key_at(time)
        if key is not None:
            key.value = value
        else:
            self.add_key(Key(time, value))

    def get_key_at(self, time):
        """Returns the key from the animation curve with the given time.

        Note
        ----
        If a key in the animation curve exists with a time within a tolerance of the given time,
        this key is returned.
        Tolerance values are defined in the constants.py file.
        Very high tolerance values are used here since it is never useful to have 2 keys extremely close together.
        They would become indistinguishable. See constants.py for more details.

        Parameters:
        ----------
        time : float
            The time of the key to be returned.

        Returns:
        ----------
        Key
            The key at the given time. None if no key at the given time is found.
        """
        # Find the key close to the given time using binary search.
        low = 0
        high = self.get_key_count() - 1
        while low <= high:
            mid = (low + high) // 2
            if self.keys[mid].time < (time - VERY_HIGH_A_TOL):
                low = mid + 1
            elif self.keys[mid].time > (time + VERY_HIGH_A_TOL):
                high = mid - 1
            else:
                return self.keys[mid]
        return None

    def remove_key_at(self, time):
        """Removes the key at the given time.

        Note:
        ----------
        this method uses the get_key_at() method to check if a key exists at the given time.
        See the documentation of that method for more details about the tolerance values of the check.

        Warns:
        ----------
        UserWarning
            If no key at the given time is found.

        Parameters:
        ----------
        time : float
            The time of the key to be removed.
        """
        key = self.get_key_at(time)
        if key is not None:
            self.keys.remove(key)
        else:
            warnings.warn(
                "No key found at the given time. Key removal ignored.", stacklevel=2
            )

    def get_previous_key(self, time):
        """Returns the previous key of the animation curve at the given key time.
        i.e. the key with the largest time less than the given time.

        Parameters:
        ----------
        time : float
            The time at which the previous key is to be returned.

        Returns:
        ----------
        Key
            The previous key. None if no key is found.

        Note:
        ----------
        If the given time is less than the time of the first key in the animation curve,
        the first key is returned.
        """
        if self.is_empty():
            return None

        # return the last key with a time less than the given time
        for key_id in range(len(self.keys) - 1, -1, -1):
            if self.keys[key_id].time <= time:
                return self.keys[key_id]

        return self.keys[-1]

    def get_next_key(self, time):
        """Returns the next key of the animation curve at the given key time.
        i.e. the key with the smallest time greater than the given time.

        Parameters:
        ----------
        time : float
            The time at which the next key is to be returned.

        Returns:
        ----------
        Key
          The next key. None if no key is found.

        Note:
        ----------
        If the given time is greater than the time of the last key in the animation curve,
        the last key is returned.
        """
        if self.is_empty():
            return None

        for key_id in range(len(self.keys)):
            if self.keys[key_id].time > time:
                return self.keys[key_id]

        return self.keys[0]

    def get_previous_value(self, time, shift=0.0):
        """Returns the previous value of the animation curve at the given key time.

        Parameters:
        ----------
        time : float
            The time at which the previous value is to be returned.

        Returns:
        ----------
        Any
            The previous value. None if no key is found.

        See Also:
        ----------
        get_previous_key(): used to get the previous key from which the value is returned.

        Note
        ----
        Used for constant interpolation.
        """
        # Check if keys list is empty
        if self.is_empty():
            return None

        time = (time + shift) % 1.0

        previous_key = self.get_previous_key(time)
        return previous_key.value

    def get_lerp_value(self, time, shift=0.0):
        """Computes the lerp value for the given key time.

        The lerp value is the value obtained by linearly interpolating
        between the previous and next keys.
        Not all key types support lerp interpolation. See the
        class description for a list of supported key types.

        Parameters:
        ----------
        time : float
            The time where to compute the lerp value.
        shift : float, optional
            The shift is added to the given time.

        Returns:
        ----------
        any
            The lerp value. None if no key is found.

        See Also:
        ----------
        get_previous_key(): used to get the previous key.
        get_next_key(): used to get the next key.
        lerp(): used to compute the lerp value.

        Note
        ----
        Used for linear interpolation.
        """
        # Check if keys list is empty
        if self.is_empty():
            return None

        time = (time + shift) % 1.0

        previous_key = self.get_previous_key(time)
        next_key = self.get_next_key(time)
        delta = next_key.time - previous_key.time

        if np.isclose(delta, 0, rtol=VERY_HIGH_R_TOL, atol=VERY_HIGH_A_TOL):
            return previous_key.value
        else:
            progress = (time - previous_key.time) / delta
            pk_val = previous_key.value
            nk_val = next_key.value

            return Curve.lerp(pk_val, nk_val, progress)

    @staticmethod
    def lerp(first_val, second_val, ratio):
        """Computes the lerp value at the given ratio between two values.

        A ratio of 0 returns the first value.
        Similarly, a ratio of 1 returns the second value.

        For int, float and array of int and float, The interp() function
        of numpy is used to compute the lerp value.
        See https://numpy.org/doc/stable/reference/generated/numpy.interp.html
        For quaternion, the slerp() function of numpy quaternion is used.
        See https://github.com/moble/quaternion/blob/main/src/quaternion/quaternion_time_series.py#L61
        For transform, the lerp() function of the Transform class is used.
        This method makes use of the two previous methods to compute the lerp value.
        See skanym/core/math/transform.py
        All other types are not supported.

        Parameters:
        ----------
        first_val : any
            The first value.
        second_val : any
            The second value.
        ratio : float
            The ratio used to compute the lerp value.

        Returns:
        ----------
        any
            The linearly interpolated value.

        Raises:
        ----------
        TypeError
            If the type of the given values is not supported.
            See the class description for a list of supported types.

        Note:
        ----------
        The type checking is only done on the first_val parameter.
        The type of the two values must be the same.
        """

        if isinstance(first_val, (int, float)):
            result = np.interp(ratio, [0, 1], [first_val, second_val])
            if isinstance(first_val, int):
                return int(result)
            else:
                return result

        elif isinstance(first_val, (list, np.ndarray)):
            size = len(first_val)
            result = np.empty(size)
            for i in range(len(first_val)):
                result[i] = np.interp(ratio, [0, 1], [first_val[i], second_val[i]])
            if isinstance(first_val, list):
                return result.tolist()
            else:
                return result

        elif isinstance(first_val, np.quaternion):
            return quaternion.slerp(first_val, second_val, 0, 1, ratio)

        elif isinstance(first_val, Transform):
            return Transform.lerp(first_val, second_val, ratio)
        else:
            raise TypeError(
                f"Cannot lerp between elements of type {str(type(first_val))}."
            )

    def __repr__(self):
        if self.keys:
            return f"Curve(type={str(self.keys[0].get_type())}, keys={str(self.keys)})"
        else:
            return "Curve(type=None, keys=[])"

    def __eq__(self, other):
        """Equality operator for Curve objects.

        Note
        ----
        Two curves are considered equal if all keys are equal. See Key.__eq__()

        Parameters
        ----------
        other : Curve
            Curve object to compare to.

        Returns
        -------
        bool
            True if the two Curves are equal, False otherwise.
        """
        if isinstance(other, Curve):
            return np.all(self.keys == other.keys)
        return NotImplemented
