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
    from channelengine_merchant_api_client.model.merchant_product_extra_data_item_request import MerchantProductExtraDataItemRequest
    from channelengine_merchant_api_client.model.vat_rate_type import VatRateType
    globals()['MerchantProductExtraDataItemRequest'] = MerchantProductExtraDataItemRequest
    globals()['VatRateType'] = VatRateType


class MerchantProductRequest(ModelNormal):
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
        ('merchant_product_no',): {
            'max_length': 64,
            'min_length': 0,
        },
        ('parent_merchant_product_no',): {
            'max_length': 64,
            'min_length': 0,
        },
        ('parent_merchant_product_no2',): {
            'max_length': 64,
            'min_length': 0,
        },
        ('name',): {
            'max_length': 256,
            'min_length': 0,
        },
        ('brand',): {
            'max_length': 256,
            'min_length': 0,
        },
        ('size',): {
            'max_length': 64,
            'min_length': 0,
        },
        ('color',): {
            'max_length': 64,
            'min_length': 0,
        },
        ('ean',): {
            'max_length': 64,
            'min_length': 0,
        },
        ('manufacturer_product_number',): {
            'max_length': 64,
            'min_length': 0,
        },
        ('stock',): {
            'inclusive_minimum': 0,
        },
        ('price',): {
            'inclusive_minimum': 0,
        },
        ('shipping_time',): {
            'max_length': 128,
            'min_length': 0,
        },
        ('url',): {
            'max_length': 512,
            'min_length': 0,
        },
        ('image_url',): {
            'max_length': 512,
            'min_length': 0,
        },
        ('extra_image_url1',): {
            'max_length': 512,
            'min_length': 0,
        },
        ('extra_image_url2',): {
            'max_length': 512,
            'min_length': 0,
        },
        ('extra_image_url3',): {
            'max_length': 512,
            'min_length': 0,
        },
        ('extra_image_url4',): {
            'max_length': 512,
            'min_length': 0,
        },
        ('extra_image_url5',): {
            'max_length': 512,
            'min_length': 0,
        },
        ('extra_image_url6',): {
            'max_length': 512,
            'min_length': 0,
        },
        ('extra_image_url7',): {
            'max_length': 512,
            'min_length': 0,
        },
        ('extra_image_url8',): {
            'max_length': 512,
            'min_length': 0,
        },
        ('extra_image_url9',): {
            'max_length': 512,
            'min_length': 0,
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
            'merchant_product_no': (str,),  # noqa: E501
            'parent_merchant_product_no': (str, none_type,),  # noqa: E501
            'parent_merchant_product_no2': (str, none_type,),  # noqa: E501
            'extra_data': ([MerchantProductExtraDataItemRequest], none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'brand': (str, none_type,),  # noqa: E501
            'size': (str, none_type,),  # noqa: E501
            'color': (str, none_type,),  # noqa: E501
            'ean': (str, none_type,),  # noqa: E501
            'manufacturer_product_number': (str, none_type,),  # noqa: E501
            'stock': (int,),  # noqa: E501
            'price': (float,),  # noqa: E501
            'msrp': (float, none_type,),  # noqa: E501
            'purchase_price': (float, none_type,),  # noqa: E501
            'vat_rate_type': (VatRateType,),  # noqa: E501
            'shipping_cost': (float, none_type,),  # noqa: E501
            'shipping_time': (str, none_type,),  # noqa: E501
            'url': (str, none_type,),  # noqa: E501
            'image_url': (str, none_type,),  # noqa: E501
            'extra_image_url1': (str, none_type,),  # noqa: E501
            'extra_image_url2': (str, none_type,),  # noqa: E501
            'extra_image_url3': (str, none_type,),  # noqa: E501
            'extra_image_url4': (str, none_type,),  # noqa: E501
            'extra_image_url5': (str, none_type,),  # noqa: E501
            'extra_image_url6': (str, none_type,),  # noqa: E501
            'extra_image_url7': (str, none_type,),  # noqa: E501
            'extra_image_url8': (str, none_type,),  # noqa: E501
            'extra_image_url9': (str, none_type,),  # noqa: E501
            'category_trail': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'merchant_product_no': 'MerchantProductNo',  # noqa: E501
        'parent_merchant_product_no': 'ParentMerchantProductNo',  # noqa: E501
        'parent_merchant_product_no2': 'ParentMerchantProductNo2',  # noqa: E501
        'extra_data': 'ExtraData',  # noqa: E501
        'name': 'Name',  # noqa: E501
        'description': 'Description',  # noqa: E501
        'brand': 'Brand',  # noqa: E501
        'size': 'Size',  # noqa: E501
        'color': 'Color',  # noqa: E501
        'ean': 'Ean',  # noqa: E501
        'manufacturer_product_number': 'ManufacturerProductNumber',  # noqa: E501
        'stock': 'Stock',  # noqa: E501
        'price': 'Price',  # noqa: E501
        'msrp': 'MSRP',  # noqa: E501
        'purchase_price': 'PurchasePrice',  # noqa: E501
        'vat_rate_type': 'VatRateType',  # noqa: E501
        'shipping_cost': 'ShippingCost',  # noqa: E501
        'shipping_time': 'ShippingTime',  # noqa: E501
        'url': 'Url',  # noqa: E501
        'image_url': 'ImageUrl',  # noqa: E501
        'extra_image_url1': 'ExtraImageUrl1',  # noqa: E501
        'extra_image_url2': 'ExtraImageUrl2',  # noqa: E501
        'extra_image_url3': 'ExtraImageUrl3',  # noqa: E501
        'extra_image_url4': 'ExtraImageUrl4',  # noqa: E501
        'extra_image_url5': 'ExtraImageUrl5',  # noqa: E501
        'extra_image_url6': 'ExtraImageUrl6',  # noqa: E501
        'extra_image_url7': 'ExtraImageUrl7',  # noqa: E501
        'extra_image_url8': 'ExtraImageUrl8',  # noqa: E501
        'extra_image_url9': 'ExtraImageUrl9',  # noqa: E501
        'category_trail': 'CategoryTrail',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, merchant_product_no, *args, **kwargs):  # noqa: E501
        """MerchantProductRequest - a model defined in OpenAPI

        Args:
            merchant_product_no (str): A unique identifier of the product. (sku).

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
            parent_merchant_product_no (str, none_type): If this product is a different version of another  product (for example, all fields are the same except  size), then this field should contain  the 'MerchantProductNo' of the parent. The parent  should already exist (or be present between the products  in the content of the API call, it does not matter whether  the parent is behind the child in the list).. [optional]  # noqa: E501
            parent_merchant_product_no2 (str, none_type): If this product is a different version of another  product (for example, all fields are the same except  color) and itself is a parent with child products (e.g. of sizes),  then this field should contain the 'MerchantProductNo' of the grandparent. The grandparent  should already exist (or be present between the products  in the content of the API call, it does not matter whether  the grandparent is behind the child in the list).  When you set this field, the ParentMerchantProductNo should be left empty.                Use this field in case of three level product hierarchy,  e.g. model - color - size.  This is required for channels like Otto.. [optional]  # noqa: E501
            extra_data ([MerchantProductExtraDataItemRequest], none_type): An optional list of key-value pairs containing  extra data about this product. This data can be  sent to channels or used for filtering products.. [optional]  # noqa: E501
            name (str, none_type): The name of the product.. [optional]  # noqa: E501
            description (str, none_type): A description of the product. Can contain these HTML tags:  div, span, pre, p, br, hr, hgroup, h1, h2, h3, h4, h5, h6, ul, ol, li, dl, dt, dd, strong, em, b, i, u, img, a, abbr, address, blockquote, area, audio, video, caption, table, tbody, td, tfoot, th, thead, tr.. [optional]  # noqa: E501
            brand (str, none_type): The brand of the product.. [optional]  # noqa: E501
            size (str, none_type): Optional. The size of the product (variant). E.g. fashion size (S-XL, 46-56, etc), width of the watch, etc... [optional]  # noqa: E501
            color (str, none_type): Optional. The color of the product (variant).. [optional]  # noqa: E501
            ean (str, none_type): The EAN of GTIN of the product.. [optional]  # noqa: E501
            manufacturer_product_number (str, none_type): The unique product reference used by the manufacturer/vendor of the product.. [optional]  # noqa: E501
            stock (int): The number of items in stock.. [optional]  # noqa: E501
            price (float): Price, including VAT.. [optional]  # noqa: E501
            msrp (float, none_type): Manufacturer's suggested retail price.. [optional]  # noqa: E501
            purchase_price (float, none_type): Optional. The purchase price of the product. Useful for repricing.. [optional]  # noqa: E501
            vat_rate_type (VatRateType): [optional]  # noqa: E501
            shipping_cost (float, none_type): Shipping cost of the product.. [optional]  # noqa: E501
            shipping_time (str, none_type): A textual representation of the shippingtime.  For example, in Dutch: 'Op werkdagen voor 22:00 uur besteld, morgen in huis'.. [optional]  # noqa: E501
            url (str, none_type): A URL pointing to the merchant's webpage  which displays this product.. [optional]  # noqa: E501
            image_url (str, none_type): A URL at which an image of this product  can be found.. [optional]  # noqa: E501
            extra_image_url1 (str, none_type): Url to an additional image of product (1).. [optional]  # noqa: E501
            extra_image_url2 (str, none_type): Url to an additional image of product (2).. [optional]  # noqa: E501
            extra_image_url3 (str, none_type): Url to an additional image of product (3).. [optional]  # noqa: E501
            extra_image_url4 (str, none_type): Url to an additional image of product (4).. [optional]  # noqa: E501
            extra_image_url5 (str, none_type): Url to an additional image of product (5).. [optional]  # noqa: E501
            extra_image_url6 (str, none_type): Url to an additional image of product (6).. [optional]  # noqa: E501
            extra_image_url7 (str, none_type): Url to an additional image of product (7).. [optional]  # noqa: E501
            extra_image_url8 (str, none_type): Url to an additional image of product (8).. [optional]  # noqa: E501
            extra_image_url9 (str, none_type): Url to an additional image of product (9).. [optional]  # noqa: E501
            category_trail (str, none_type): The category to which this product belongs.  Please supply this field in the following format:  'maincategory > category > subcategory'  For example:  'vehicles > bikes > mountainbike'.. [optional]  # noqa: E501
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

        self.merchant_product_no = merchant_product_no
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
    def __init__(self, merchant_product_no, *args, **kwargs):  # noqa: E501
        """MerchantProductRequest - a model defined in OpenAPI

        Args:
            merchant_product_no (str): A unique identifier of the product. (sku).

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
            parent_merchant_product_no (str, none_type): If this product is a different version of another  product (for example, all fields are the same except  size), then this field should contain  the 'MerchantProductNo' of the parent. The parent  should already exist (or be present between the products  in the content of the API call, it does not matter whether  the parent is behind the child in the list).. [optional]  # noqa: E501
            parent_merchant_product_no2 (str, none_type): If this product is a different version of another  product (for example, all fields are the same except  color) and itself is a parent with child products (e.g. of sizes),  then this field should contain the 'MerchantProductNo' of the grandparent. The grandparent  should already exist (or be present between the products  in the content of the API call, it does not matter whether  the grandparent is behind the child in the list).  When you set this field, the ParentMerchantProductNo should be left empty.                Use this field in case of three level product hierarchy,  e.g. model - color - size.  This is required for channels like Otto.. [optional]  # noqa: E501
            extra_data ([MerchantProductExtraDataItemRequest], none_type): An optional list of key-value pairs containing  extra data about this product. This data can be  sent to channels or used for filtering products.. [optional]  # noqa: E501
            name (str, none_type): The name of the product.. [optional]  # noqa: E501
            description (str, none_type): A description of the product. Can contain these HTML tags:  div, span, pre, p, br, hr, hgroup, h1, h2, h3, h4, h5, h6, ul, ol, li, dl, dt, dd, strong, em, b, i, u, img, a, abbr, address, blockquote, area, audio, video, caption, table, tbody, td, tfoot, th, thead, tr.. [optional]  # noqa: E501
            brand (str, none_type): The brand of the product.. [optional]  # noqa: E501
            size (str, none_type): Optional. The size of the product (variant). E.g. fashion size (S-XL, 46-56, etc), width of the watch, etc... [optional]  # noqa: E501
            color (str, none_type): Optional. The color of the product (variant).. [optional]  # noqa: E501
            ean (str, none_type): The EAN of GTIN of the product.. [optional]  # noqa: E501
            manufacturer_product_number (str, none_type): The unique product reference used by the manufacturer/vendor of the product.. [optional]  # noqa: E501
            stock (int): The number of items in stock.. [optional]  # noqa: E501
            price (float): Price, including VAT.. [optional]  # noqa: E501
            msrp (float, none_type): Manufacturer's suggested retail price.. [optional]  # noqa: E501
            purchase_price (float, none_type): Optional. The purchase price of the product. Useful for repricing.. [optional]  # noqa: E501
            vat_rate_type (VatRateType): [optional]  # noqa: E501
            shipping_cost (float, none_type): Shipping cost of the product.. [optional]  # noqa: E501
            shipping_time (str, none_type): A textual representation of the shippingtime.  For example, in Dutch: 'Op werkdagen voor 22:00 uur besteld, morgen in huis'.. [optional]  # noqa: E501
            url (str, none_type): A URL pointing to the merchant's webpage  which displays this product.. [optional]  # noqa: E501
            image_url (str, none_type): A URL at which an image of this product  can be found.. [optional]  # noqa: E501
            extra_image_url1 (str, none_type): Url to an additional image of product (1).. [optional]  # noqa: E501
            extra_image_url2 (str, none_type): Url to an additional image of product (2).. [optional]  # noqa: E501
            extra_image_url3 (str, none_type): Url to an additional image of product (3).. [optional]  # noqa: E501
            extra_image_url4 (str, none_type): Url to an additional image of product (4).. [optional]  # noqa: E501
            extra_image_url5 (str, none_type): Url to an additional image of product (5).. [optional]  # noqa: E501
            extra_image_url6 (str, none_type): Url to an additional image of product (6).. [optional]  # noqa: E501
            extra_image_url7 (str, none_type): Url to an additional image of product (7).. [optional]  # noqa: E501
            extra_image_url8 (str, none_type): Url to an additional image of product (8).. [optional]  # noqa: E501
            extra_image_url9 (str, none_type): Url to an additional image of product (9).. [optional]  # noqa: E501
            category_trail (str, none_type): The category to which this product belongs.  Please supply this field in the following format:  'maincategory > category > subcategory'  For example:  'vehicles > bikes > mountainbike'.. [optional]  # noqa: E501
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

        self.merchant_product_no = merchant_product_no
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
