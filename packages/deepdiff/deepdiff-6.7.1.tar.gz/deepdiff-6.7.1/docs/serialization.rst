:doc:`/index`

.. _serialization_label:

Serialization
=============

.. _to_dict_label:

To Dict
-------

In order to convert the DeepDiff object into a normal Python dictionary, use the to_dict() method.

Example:
    >>> t1 = {1: 1, 2: 2, 3: 3, 4: {"a": "hello", "b": [1, 2, 3]}}
    >>> t2 = {1: 1, 2: 2, 3: 3, 4: {"a": "hello", "b": "world\n\n\nEnd"}}
    >>> ddiff = DeepDiff(t1, t2)
    >>> ddiff.to_dict()
    {'type_changes': {"root[4]['b']": {'old_type': <class 'list'>, 'new_type': <class 'str'>, 'old_value': [1, 2, 3], 'new_value': 'world\n\n\nEnd'}}}


Note that you can override the :ref:`view_label` that was originally used to generate the diff here.

Example:
    >>> t1 = {1: 1, 2: 2, 3: 3, 4: {"a": "hello", "b": [1, 2, 3]}}
    >>> t2 = {1: 1, 2: 2, 3: 3, 4: {"a": "hello", "b": "world\n\n\nEnd"}}
    >>> ddiff = DeepDiff(t1, t2, view='tree')
    >>> ddiff.to_dict(view_override='text')
    {'type_changes': {"root[4]['b']": {'old_type': <class 'list'>, 'new_type': <class 'str'>, 'old_value': [1, 2, 3], 'new_value': 'world\n\n\nEnd'}}}

.. _to_json_label:

To Json
-------

Dump json of the text view.

In order to do safe json serialization, use the to_json() method.

**Parameters**

default_mapping : dictionary(optional), a dictionary of mapping of different types to json types.

by default DeepDiff converts certain data types. For example Decimals into floats so they can be exported into json.
If you have a certain object type that the json serializer can not serialize it, please pass the appropriate type
conversion through this dictionary.

kwargs: Any other kwargs you pass will be passed on to Python's json.dumps()


Example 1 Serialize custom objects:
    >>> class A:
    ...     pass
    ...
    >>> class B:
    ...     pass
    ...
    >>> t1 = A()
    >>> t2 = B()
    >>> ddiff = DeepDiff(t1, t2)
    >>> ddiff.to_json()
    TypeError: We do not know how to convert <__main__.A object at 0x10648> of type <class '__main__.A'> for json serialization. Please pass the default_mapping parameter with proper mapping of the object to a basic python type.

    >>> default_mapping = {A: lambda x: 'obj A', B: lambda x: 'obj B'}
    >>> ddiff.to_json(default_mapping=default_mapping)
    '{"type_changes": {"root": {"old_type": "A", "new_type": "B", "old_value": "obj A", "new_value": "obj B"}}}'


Example 2:
    >>> t1 = {1: 1, 2: 2, 3: 3, 4: {"a": "hello", "b": [1, 2, 3]}}
    >>> t2 = {1: 1, 2: 2, 3: 3, 4: {"a": "hello", "b": "world\n\n\nEnd"}}
    >>> ddiff = DeepDiff(t1, t2, view='tree')
    >>> ddiff.to_json()
    '{"type_changes": {"root[4][\'b\']": {"old_type": "list", "new_type": "str", "old_value": [1, 2, 3], "new_value": "world\\n\\n\\nEnd"}}}'


.. _to_json_pickle_label:

To Json Pickle
--------------

If you want the original DeepDiff object to be serialized with all the bells and whistles, you can use the to_json_pickle() and from_json_pickle() in order to serialize and deserialize its results into json. Note that json_pickle is unsafe and json pickle dumps from untrusted sources should never be loaded. It is recommended not to use this serialization unless you have to.

.. note::
    You need to install the `jsonpickle <https://github.com/jsonpickle/jsonpickle>`_ package to use the to_json_pickle() method.

Serialize and then deserialize back to deepdiff
    >>> t1 = {1: 1, 2: 2, 3: 3}
    >>> t2 = {1: 1, 2: "2", 3: 3}
    >>> ddiff = DeepDiff(t1, t2)
    >>> jsoned = ddiff.to_json_pickle()
    >>> jsoned
    '{"type_changes": {"root[2]": {"new_type": {"py/type": "builtins.str"}, "new_value": "2", "old_type": {"py/type": "builtins.int"}, "old_value": 2}}}'
    >>> ddiff_new = DeepDiff.from_json_pickle(jsoned)
    >>> ddiff == ddiff_new
    True


.. _from_json_pickle_label:

From Json Pickle
----------------

Load the diff object from the json pickle dump.
Take a look at the above :ref:`to_json_pickle_label` for an example.


.. _delta_to_flat_dicts_label:

Delta Serialize To Flat Dictionaries
------------------------------------

Sometimes, it is desired to serialize a :ref:`delta_label` object to a list of flat dictionaries. For example, to store them in relation databases. In that case, you can use the Delta.to_flat_dicts to achieve the desired outcome.

For example:

    >>> from pprint import pprint
    >>> from deepdiff import DeepDiff, Delta
    >>> t1 = {"key1": "value1"}
    >>> t2 = {"field2": {"key2": "value2"}}
    >>> diff = DeepDiff(t1, t2, verbose_level=2)
    >>> pprint(diff, indent=2)
    { 'dictionary_item_added': {"root['field2']": {'key2': 'value2'}},
      'dictionary_item_removed': {"root['key1']": 'value1'}}
    >>>
    >>> delta = Delta(diff, verify_symmetry=True)
    >>> flat_dicts = delta.to_flat_dicts()
    >>> pprint(flat_dicts, indent=2)
    [ { 'action': 'dictionary_item_added',
        'path': ['field2', 'key2'],
        'value': 'value2'},
      {'action': 'dictionary_item_removed', 'path': ['key1'], 'value': 'value1'}]


Example 2:

    >>> t3 = ["A", "B"]
    >>> t4 = ["A", "B", "C", "D"]
    >>> diff = DeepDiff(t3, t4, verbose_level=2)
    >>> pprint(diff, indent=2)
    {'iterable_item_added': {'root[2]': 'C', 'root[3]': 'D'}}
    >>>
    >>> delta = Delta(diff, verify_symmetry=True)
    >>> flat_dicts = delta.to_flat_dicts()
    >>> pprint(flat_dicts, indent=2)
    [ {'action': 'iterable_item_added', 'path': [2], 'value': 'C'},
      {'action': 'iterable_item_added', 'path': [3], 'value': 'D'}]


.. _delta_from_flat_dicts_label:

Delta Load From Flat Dictionaries
------------------------------------

    >>> from deepdiff import DeepDiff, Delta
    >>> t3 = ["A", "B"]
    >>> t4 = ["A", "B", "C", "D"]
    >>> diff = DeepDiff(t3, t4, verbose_level=2)
    >>> delta = Delta(diff, verify_symmetry=True)
    DeepDiff Deprecation: use bidirectional instead of verify_symmetry parameter.
    >>> flat_dicts = delta.to_flat_dicts()
    >>>
    >>> delta2 = Delta(flat_dict_list=flat_dicts)
    >>> t3 + delta == t4
    True


Back to :doc:`/index`
