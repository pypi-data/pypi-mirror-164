# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "PartyAddress",
    "AccountDetails",
    "RoutingDetailsBankAddress",
    "RoutingDetails",
    "Connection",
    "InternalAccount",
]


class PartyAddress(BaseModel):
    country: Optional[Optional[str]]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: Optional[str]

    id: Optional[str]

    line1: Optional[Optional[str]]

    line2: Optional[Optional[str]]

    live_mode: Optional[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    locality: Optional[Optional[str]]
    """Locality or City."""

    object: Optional[str]

    postal_code: Optional[Optional[str]]
    """The postal code of the address."""

    region: Optional[Optional[str]]
    """Region or State."""

    updated_at: Optional[str]


class AccountDetails(BaseModel):
    account_number: Optional[str]

    account_number_type: Optional[Literal["iban", "clabe", "wallet_address", "pan", "other"]]
    """
    Supports iban and clabe, otherwise other if the bank account number is in a
    generic format.
    """

    created_at: Optional[str]

    discarded_at: Optional[Optional[str]]

    id: Optional[str]

    live_mode: Optional[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Optional[str]

    updated_at: Optional[str]


class RoutingDetailsBankAddress(BaseModel):
    country: Optional[Optional[str]]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: Optional[str]

    id: Optional[str]

    line1: Optional[Optional[str]]

    line2: Optional[Optional[str]]

    live_mode: Optional[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    locality: Optional[Optional[str]]
    """Locality or City."""

    object: Optional[str]

    postal_code: Optional[Optional[str]]
    """The postal code of the address."""

    region: Optional[Optional[str]]
    """Region or State."""

    updated_at: Optional[str]


class RoutingDetails(BaseModel):
    bank_address: Optional[Optional[RoutingDetailsBankAddress]]

    bank_name: Optional[str]

    created_at: Optional[str]

    discarded_at: Optional[Optional[str]]

    id: Optional[str]

    live_mode: Optional[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Optional[str]

    payment_type: Optional[
        Optional[
            Literal[
                "ach",
                "au_becs",
                "bacs",
                "book",
                "card",
                "check",
                "eft",
                "interac",
                "provxchange",
                "rtp",
                "sen",
                "sepa",
                "signet",
                "wire",
            ]
        ]
    ]
    """
    If the routing detail is to be used for a specific payment type this field will
    be populated, otherwise null.
    """

    routing_number: Optional[str]
    """The routing number of the bank."""

    routing_number_type: Optional[
        Literal["aba", "swift", "au_bsb", "ca_cpa", "cnaps", "gb_sort_code", "in_ifsc", "my_branch_code", "br_codigo"]
    ]

    updated_at: Optional[str]


class Connection(BaseModel):
    created_at: Optional[str]

    discarded_at: Optional[Optional[str]]

    id: Optional[str]

    live_mode: Optional[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Optional[str]

    updated_at: Optional[str]

    vendor_customer_id: Optional[Optional[str]]
    """The identifier of the vendor bank."""

    vendor_id: Optional[str]
    """The identifier of the vendor bank."""

    vendor_name: Optional[str]
    """The name of the vendor bank."""


class InternalAccount(BaseModel):
    account_details: Optional[List[AccountDetails]]
    """An array of account detail objects."""

    account_type: Optional[Optional[Literal["checking", "other", "savings"]]]
    """Can be checking, savings or other."""

    connection: Optional[Connection]
    """Specifies which financial institution the accounts belong to."""

    created_at: Optional[str]

    currency: Optional[
        Literal[
            "AED",
            "AFN",
            "ALL",
            "AMD",
            "ANG",
            "AOA",
            "ARS",
            "AUD",
            "AWG",
            "AZN",
            "BAM",
            "BBD",
            "BCH",
            "BDT",
            "BGN",
            "BHD",
            "BIF",
            "BMD",
            "BND",
            "BOB",
            "BRL",
            "BSD",
            "BTC",
            "BTN",
            "BWP",
            "BYN",
            "BYR",
            "BZD",
            "CAD",
            "CDF",
            "CHF",
            "CLF",
            "CLP",
            "CNH",
            "CNY",
            "COP",
            "CRC",
            "CUC",
            "CUP",
            "CVE",
            "CZK",
            "DJF",
            "DKK",
            "DOP",
            "DZD",
            "EEK",
            "EGP",
            "ERN",
            "ETB",
            "EUR",
            "FJD",
            "FKP",
            "GBP",
            "GBX",
            "GEL",
            "GGP",
            "GHS",
            "GIP",
            "GMD",
            "GNF",
            "GTQ",
            "GYD",
            "HKD",
            "HNL",
            "HRK",
            "HTG",
            "HUF",
            "IDR",
            "ILS",
            "IMP",
            "INR",
            "IQD",
            "IRR",
            "ISK",
            "JEP",
            "JMD",
            "JOD",
            "JPY",
            "KES",
            "KGS",
            "KHR",
            "KMF",
            "KPW",
            "KRW",
            "KWD",
            "KYD",
            "KZT",
            "LAK",
            "LBP",
            "LKR",
            "LRD",
            "LSL",
            "LTL",
            "LVL",
            "LYD",
            "MAD",
            "MDL",
            "MGA",
            "MKD",
            "MMK",
            "MNT",
            "MOP",
            "MRO",
            "MRU",
            "MTL",
            "MUR",
            "MVR",
            "MWK",
            "MXN",
            "MYR",
            "MZN",
            "NAD",
            "NGN",
            "NIO",
            "NOK",
            "NPR",
            "NZD",
            "OMR",
            "PAB",
            "PEN",
            "PGK",
            "PHP",
            "PKR",
            "PLN",
            "PYG",
            "QAR",
            "RON",
            "RSD",
            "RUB",
            "RWF",
            "SAR",
            "SBD",
            "SCR",
            "SDG",
            "SEK",
            "SGD",
            "SHP",
            "SKK",
            "SLL",
            "SOS",
            "SRD",
            "SSP",
            "STD",
            "SVC",
            "SYP",
            "SZL",
            "THB",
            "TJS",
            "TMM",
            "TMT",
            "TND",
            "TOP",
            "TRY",
            "TTD",
            "TWD",
            "TZS",
            "UAH",
            "UGX",
            "USD",
            "UYU",
            "UZS",
            "VEF",
            "VES",
            "VND",
            "VUV",
            "WST",
            "XAF",
            "XAG",
            "XAU",
            "XBA",
            "XBB",
            "XBC",
            "XBD",
            "XCD",
            "XDR",
            "XFU",
            "XOF",
            "XPD",
            "XPF",
            "XPT",
            "XTS",
            "YER",
            "ZAR",
            "ZMK",
            "ZMW",
            "ZWD",
            "ZWL",
            "ZWN",
            "ZWR",
        ]
    ]
    """The currency of the account."""

    id: Optional[str]

    live_mode: Optional[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Optional[Dict[str, str]]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: Optional[Optional[str]]
    """A nickname for the account."""

    object: Optional[str]

    party_address: Optional[Optional[PartyAddress]]
    """The address associated with the owner or null."""

    party_name: Optional[str]
    """The legal name of the entity which owns the account."""

    party_type: Optional[Optional[Literal["business", "individual"]]]
    """Either individual or business."""

    routing_details: Optional[List[RoutingDetails]]
    """An array of routing detail objects."""

    updated_at: Optional[str]
