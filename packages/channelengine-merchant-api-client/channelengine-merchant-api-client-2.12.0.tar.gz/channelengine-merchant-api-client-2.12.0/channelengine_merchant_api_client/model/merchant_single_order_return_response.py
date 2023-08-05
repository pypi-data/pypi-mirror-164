"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.11.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from channelengine_merchant_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from channelengine_merchant_api_client.exceptions import ApiAttributeError


def lazy_import():
    from channelengine_merchant_api_client.model.merchant_single_order_return_line_response import MerchantSingleOrderReturnLineResponse
    from channelengine_merchant_api_client.model.return_reason import ReturnReason
    from channelengine_merchant_api_client.model.return_status import ReturnStatus
    globals()['MerchantSingleOrderReturnLineResponse'] = MerchantSingleOrderReturnLineResponse
    globals()['ReturnReason'] = ReturnReason
    globals()['ReturnStatus'] = ReturnStatus


class MerchantSingleOrderReturnResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('customer_comment',): {
            'max_length': 4001,
            'min_length': 0,
        },
        ('merchant_comment',): {
            'max_length': 4001,
            'min_length': 0,
        },
        ('refund_incl_vat',): {
            'inclusive_minimum': 0,
        },
        ('refund_excl_vat',): {
            'inclusive_minimum': 0,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'merchant_order_no': (str, none_type,),  # noqa: E501
            'lines': ([MerchantSingleOrderReturnLineResponse], none_type,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'merchant_return_no': (str, none_type,),  # noqa: E501
            'channel_return_no': (str, none_type,),  # noqa: E501
            'channel_id': (int, none_type,),  # noqa: E501
            'global_channel_id': (int, none_type,),  # noqa: E501
            'global_channel_name': (str, none_type,),  # noqa: E501
            'status': (ReturnStatus,),  # noqa: E501
            'id': (int,),  # noqa: E501
            'reason': (ReturnReason,),  # noqa: E501
            'customer_comment': (str, none_type,),  # noqa: E501
            'merchant_comment': (str, none_type,),  # noqa: E501
            'refund_incl_vat': (float,),  # noqa: E501
            'refund_excl_vat': (float,),  # noqa: E501
            'return_date': (datetime, none_type,),  # noqa: E501
            'extra_data': ({str: (str,)}, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'merchant_order_no': 'MerchantOrderNo',  # noqa: E501
        'lines': 'Lines',  # noqa: E501
        'created_at': 'CreatedAt',  # noqa: E501
        'updated_at': 'UpdatedAt',  # noqa: E501
        'merchant_return_no': 'MerchantReturnNo',  # noqa: E501
        'channel_return_no': 'ChannelReturnNo',  # noqa: E501
        'channel_id': 'ChannelId',  # noqa: E501
        'global_channel_id': 'GlobalChannelId',  # noqa: E501
        'global_channel_name': 'GlobalChannelName',  # noqa: E501
        'status': 'Status',  # noqa: E501
        'id': 'Id',  # noqa: E501
        'reason': 'Reason',  # noqa: E501
        'customer_comment': 'CustomerComment',  # noqa: E501
        'merchant_comment': 'MerchantComment',  # noqa: E501
        'refund_incl_vat': 'RefundInclVat',  # noqa: E501
        'refund_excl_vat': 'RefundExclVat',  # noqa: E501
        'return_date': 'ReturnDate',  # noqa: E501
        'extra_data': 'ExtraData',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """MerchantSingleOrderReturnResponse - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            merchant_order_no (str, none_type): The unique order reference used by the Merchant.. [optional]  # noqa: E501
            lines ([MerchantSingleOrderReturnLineResponse], none_type): [optional]  # noqa: E501
            created_at (datetime): The date at which the return was created in ChannelEngine.. [optional]  # noqa: E501
            updated_at (datetime): The date at which the return was last modified in ChannelEngine.. [optional]  # noqa: E501
            merchant_return_no (str, none_type): The unique return reference used by the Merchant, will be empty in case of a channel or unacknowledged return.. [optional]  # noqa: E501
            channel_return_no (str, none_type): The unique return reference used by the Channel, will be empty in case of a merchant return.. [optional]  # noqa: E501
            channel_id (int, none_type): The id of the channel.. [optional]  # noqa: E501
            global_channel_id (int, none_type): The id of the Global Channel.. [optional]  # noqa: E501
            global_channel_name (str, none_type): The name of the Global Channel.. [optional]  # noqa: E501
            status (ReturnStatus): [optional]  # noqa: E501
            id (int): The unique return reference used by ChannelEngine.. [optional]  # noqa: E501
            reason (ReturnReason): [optional]  # noqa: E501
            customer_comment (str, none_type): Optional. Comment of customer on the (reason of) the return.. [optional]  # noqa: E501
            merchant_comment (str, none_type): Optional. Comment of merchant on the return.. [optional]  # noqa: E501
            refund_incl_vat (float): Refund amount incl. VAT.. [optional]  # noqa: E501
            refund_excl_vat (float): Refund amount excl. VAT.. [optional]  # noqa: E501
            return_date (datetime, none_type): The date at which the return was originally created in the source system (if available).. [optional]  # noqa: E501
            extra_data ({str: (str,)}, none_type): Extra data on the return. Each item must have an unqiue key. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """MerchantSingleOrderReturnResponse - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            merchant_order_no (str, none_type): The unique order reference used by the Merchant.. [optional]  # noqa: E501
            lines ([MerchantSingleOrderReturnLineResponse], none_type): [optional]  # noqa: E501
            created_at (datetime): The date at which the return was created in ChannelEngine.. [optional]  # noqa: E501
            updated_at (datetime): The date at which the return was last modified in ChannelEngine.. [optional]  # noqa: E501
            merchant_return_no (str, none_type): The unique return reference used by the Merchant, will be empty in case of a channel or unacknowledged return.. [optional]  # noqa: E501
            channel_return_no (str, none_type): The unique return reference used by the Channel, will be empty in case of a merchant return.. [optional]  # noqa: E501
            channel_id (int, none_type): The id of the channel.. [optional]  # noqa: E501
            global_channel_id (int, none_type): The id of the Global Channel.. [optional]  # noqa: E501
            global_channel_name (str, none_type): The name of the Global Channel.. [optional]  # noqa: E501
            status (ReturnStatus): [optional]  # noqa: E501
            id (int): The unique return reference used by ChannelEngine.. [optional]  # noqa: E501
            reason (ReturnReason): [optional]  # noqa: E501
            customer_comment (str, none_type): Optional. Comment of customer on the (reason of) the return.. [optional]  # noqa: E501
            merchant_comment (str, none_type): Optional. Comment of merchant on the return.. [optional]  # noqa: E501
            refund_incl_vat (float): Refund amount incl. VAT.. [optional]  # noqa: E501
            refund_excl_vat (float): Refund amount excl. VAT.. [optional]  # noqa: E501
            return_date (datetime, none_type): The date at which the return was originally created in the source system (if available).. [optional]  # noqa: E501
            extra_data ({str: (str,)}, none_type): Extra data on the return. Each item must have an unqiue key. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
