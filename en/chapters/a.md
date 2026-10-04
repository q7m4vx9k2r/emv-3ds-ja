---
layout: default
title: "3-D Secure Data Elements"
lang: en
---

# 3-D Secure Data Elements

[Home](../../index.md)

<a id="page-185"></a>

## PDF page 185

## Annex A

## 3-D Secure Data Elements

This annex contains an alphabetical listing of all EMV 3-D Secure data elements. Data element information and the Standards used to identify the information are as follows:

- Data Element Name—Identifies the data element

- Field Name—Identifies the field name for the data element

- Description—Identifies the data element purpose, and additional detail as applicable

- Source—Identifies the 3-D Secure component that is responsible to provide the data element in the message

- Length/Format/Values—Identifies the value length detail, JSON data format, and if applicable, the values associated with the data element. The term "character" in the Length Edit criteria refers to one UTF-8 character. The length of a JSON object is the length in characters of the overall string representing the object.

- Device Channel—Identifies the inclusion of a data element in a message based on the Device Channel used for a specific transaction. The following Standard is used to identify the Device Channel type:

o 01-APP—App-based Authentication

o 02-BRW—Browser-based Authentication

o 03-3RI—Deviceless Payment Authentication/Verification of Account

- Message Category—Identifies the inclusion of a data element in a Message based on the type of transaction. The following Standard is used to identify the Authentication type:

o 01-PA—Payment Authentication

o 02-NPA—Non-Payment Authentication

- Message Inclusion—Identifies the Message Type(s) that the data element is included in, and whether the inclusion of the data element in the Message Type is Required, Optional, or Conditional for both Message Categories. Unless explicitly noted otherwise in Table A.1, if a field is required for the Device Channel and Message Category of a specific transaction, the value must be present and not be empty or null.

---

<a id="page-186"></a>

## PDF page 186

The following Standards are used to identify Inclusion values:

o R = Required—Sender shall include the data element in the identified Message Type, Device Channel, and Message Category; Recipient shall check for data element presence and Validate data element contents.

o C = Conditional—Sender shall include the data element in the identified Message Type if the Conditional Inclusion requirements are met; Recipient shall check for data element presence and Validate data element contents. When no data is to be sent for an Optional data element (including a Conditional data element that is not required based on the contents of the message), the data element should be absent.

o O = Optional—Sender may include the data element in the identified Message Type; Recipient shall Validate the data element contents when present. When no data is to be sent for an Optional data element (including a Conditional data element that is not required based on the contents of the message), the data element should be absent.

- Conditional Inclusion—Identifies the applicable conditions for including the data element in the applicable Message Type with the responsibility of the Source component to meet the conditions.

Example:

| Data Element/Field<br>Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Requestor URL<br>Field Name:<br>threeDSRequestorURL | Fully Qualified URL of<br>3DS Requestor Website<br>or customer care site.<br>This data element<br>provides additional<br>information to the<br>receiving 3-D Secure<br>system if a problem arises<br>and should provide<br>contact information. | 3DS Server | Length: Variable, maximum<br>2048 characters<br>JSON Data Type: String<br>Value accepted:<br>• Fully Qualified URL<br>Example:<br>• https://server.domainna<br>me.com | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R |  |

In the example above, the 3DS Requestor URL is provided by the 3DS Server and is used for both App-based and Browser-based Authentication in the Authentication Request (AReq) message.

---

<a id="page-187"></a>

## PDF page 187

### A.1

### Missing Required Fields

A data field is missing if either:

- the name/value pair is absent, or

- the field name is present but the value is empty or null

Unless explicitly noted, if a required field is missing, the receiving component returns an Error Message as defined in Section A.9 with the applicable Error Component and Error Code = 201. This applies whether the field is always Required or Conditionally required.

### A.2

### Field Edit Criteria

Only the specified validations are to be performed. Do not reject a message based on any validation that is not listed in the tables in this annex. If a field is present, but its value does not conform to the edit criteria specified in Table A.1, the receiving component returns an Error Message as defined in Section A.9 with the applicable Error Component and Error Code = 203.

### A.3

### Encryption of AReq Data

The AReq message contains fields that are included without encryption (these are protected in transit by the secure links defined in Section 6.1). Additionally, the Device Information data element is encrypted by the 3DS SDK and passed to the 3DS Server before inclusion in the message to the DS. All data that is to be encrypted is sent as one block of encrypted data in the 3DS SDK Encrypted Data field as a JWE object. Only the 3DS SDK and DS process the JWE object before being broken down into its constituent fields. The resulting decrypted data will be placed into the AReq message to the ACS unencrypted in the Device Information data element.

---

<a id="page-188"></a>

## PDF page 188

### A.4

### EMV 3-D Secure Data Elements

Table A.1:  EMV 3-D Secure Data Elements

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Method<br>Completion<br>Indicator<br>Field Name:<br>threeDSCompInd | Indicates whether the 3DS<br>Method successfully<br>completed. | 3DS Server | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = Successfully completed<br>• N = Did not run or did not<br>successfully complete<br>• U = Unavailable – 3DS<br>Method URL was not present<br>in the PRes message data for<br>the card range associated with<br>the Cardholder Account<br>Number. | 02-BRW | 01-PA<br>02-NPA | AReq = R |  |
| 3DS Method ID<br>Field Name:<br>threeDSMethodId | Contains the 3DS Server<br>Transaction ID used during<br>the previous execution of<br>the 3DS Method. | 3DS Server | Length: 36 characters<br>JSON Data Type: String<br>Value accepted:<br>Canonical format as defined in<br>IETF RFC 4122. May use any of<br>the specified versions if the output<br>meets specified requirements. | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required if<br>3DS<br>Requestor<br>reuses<br>previous 3DS<br>Method<br>execution. |

---

<a id="page-189"></a>

## PDF page 189

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Requestor App<br>URL<br>Field Name:<br>threeDSRequesto<br>rAppURL | 3DS Requestor App<br>declaring its URL within<br>the CReq message so that<br>the Authentication App can<br>call the 3DS Requestor<br>App after OOB<br>authentication has<br>occurred.<br>Note: When providing the<br>3DS Requestor App URL,<br>the 3DS Requestor needs<br>to properly register the<br>URL with the Operating<br>System. | 3DS SDK | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Universal App Link<br>Example value:<br>https://appname.com<br>Refer to Table 1.3 for the<br>Universal App Link definition. | 01-APP | 01-PA<br>02-NPA | CReq = C | Required in all<br>CReq<br>messages if<br>3DS<br>Requestor<br>App URL is<br>provided by<br>the 3DS SDK. |
| 3DS Requestor App<br>URL Indicator<br>Field Name:<br>threeDSRequesto<br>rAppURLInd | Indicates whether the OOB<br>Authentication App used<br>by the ACS during a<br>challenge supports the<br>3DS Requestor App URL. | ACS | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = 3DS Requestor App URL<br>is supported by the OOB<br>Authentication App<br>• N = 3DS Requestor App URL<br>is NOT supported by the OOB<br>Authentication App | 01-APP | 01-PA<br>02-NPA | ARes = R |  |

3DS Requestor Authentication Indicator

Indicates the type of Authentication request.

3DS Server  Length: 2 characters

01-APP

01-PA

AReq = R

JSON Data Type: String

02-BRW

02-NPA

Values accepted:

- 01 = Payment transaction

- 02 = Recurring transaction

---

<a id="page-190"></a>

## PDF page 190

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Field Name:<br>threeDSRequesto<br>rAuthentication<br>Ind | This data element provides<br>additional information to<br>the ACS to determine the<br>best approach for handling<br>an authentication request. |  | • 03 = Instalment transaction<br>• 04 = Add card<br>• 05 = Maintain card<br>• 06 = Cardholder verification as<br>part of EMV token ID&V<br>• 07 = Billing Agreement<br>• 08 = Split shipment<br>• 09 = Delayed shipment<br>• 10 = Split payment<br>• 11–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use |  |  |  |  |
| 3DS Requestor<br>Authentication<br>Information<br>Field Name:<br>threeDSRequesto<br>rAuthentication<br>Info | Information about how the<br>3DS Requestor<br>authenticated the<br>Cardholder before or<br>during the transaction. | 3DS Server<br>DS | Size: 1–3 elements<br>JSON Data Type: Array of objects<br>Values accepted:<br>• Refer to Table A.12 for data<br>elements to include.<br>Note: Data will be formatted into a<br>JSON Array of objects prior to<br>being placed into the 3DS<br>Requestor Authentication<br>Information field of the message. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O | Optional,<br>recommended<br>to include. |

3DS Requestor Challenge Indicator

Indicates whether a challenge is requested for this transaction.

3DS Server

Size: 1–2 elements

01-APP

01-PA

AReq = O

DS

JSON Data Type: Array of string

02-BRW

02-NPA

String: 2 characters

03-3RI

Example:

---

<a id="page-191"></a>

## PDF page 191

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Field Name:<br>threeDSRequesto<br>rChallengeInd | For 01-PA, a 3DS<br>Requestor may have<br>concerns about the<br>transaction, and request a<br>challenge.<br>For 02-NPA, a challenge<br>may be necessary when<br>adding a new card to a<br>wallet.<br>Note: When providing two<br>preferences, the 3DS<br>Requestor ensures that<br>they are in preference<br>order and are not<br>conflicting. For example,<br>02 = No challenge<br>requested and 04 =<br>Challenge requested<br>(Mandate). |  | Values accepted:<br>• 01 = No preference<br>• 02 = No challenge requested<br>• 03 = Challenge requested<br>(3DS Requestor preference)<br>• 04 = Challenge requested<br>(Mandate)<br>• 05 = No challenge requested<br>(transactional risk analysis is<br>already performed)<br>• 06 = No challenge requested<br>(Data share only)<br>• 07 = No challenge requested<br>(strong consumer<br>authentication is already<br>performed)<br>• 08 = No challenge requested<br>(use Trust List exemption if no<br>challenge required)<br>• 09 = Challenge requested<br>(Trust List prompt requested if<br>challenge required)<br>• 10 = No challenge requested<br>(use low value exemption)<br>• 11 = No challenge requested<br>(Secure corporate payment<br>exemption) |  |  |  |  |

---

<a id="page-192"></a>

## PDF page 192

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | • 12 = Challenge requested<br>(Device Binding prompt<br>requested if challenge<br>required)<br>• 13 = Challenge requested<br>(Issuer requested)<br>• 14 = Challenge requested<br>(Merchant-initiated<br>transactions)<br>• 15–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use<br>Note: If the element is not<br>provided, the expected action is<br>that the ACS would interpret as 01<br>= No preference. |  |  |  |  |
| 3DS Requestor<br>Decoupled Max<br>Time<br>Field Name:<br>threeDSRequesto<br>rDecMaxTime | Indicates the maximum<br>amount of time that the<br>3DS Requestor will wait for<br>an ACS to provide the<br>results of a Decoupled<br>Authentication transaction<br>(in minutes). | 3DS Server | Length: 5 characters<br>JSON Data Type: String<br>Values accepted:<br>• Numeric values between<br>00001 and 10080 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if<br>3DS<br>Requestor<br>Decoupled<br>Request<br>Indicator = Y<br>or F or B. |

---

<a id="page-193"></a>

## PDF page 193

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Requestor<br>Decoupled Request<br>Indicator<br>Field Name:<br>threeDSRequesto<br>rDecReqInd | Indicates whether the 3DS<br>Requestor requests the<br>ACS to use Decoupled<br>Authentication and agrees<br>to use Decoupled<br>Authentication if the ACS<br>confirms its use.<br>Note: if the element is not<br>provided, the expected<br>action is for the ACS to<br>interpret as N (Do not use<br>Decoupled Authentication). | 3DS Server | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = Decoupled Authentication<br>is supported and is preferred<br>as a primary challenge method<br>if a challenge is necessary<br>(Transaction Status = D in<br>ARes).<br>• N = Do not use Decoupled<br>Authentication.<br>• F = Decoupled Authentication<br>is supported and is to be used<br>only as a fallback challenge<br>method if a challenge is<br>necessary (Transaction Status<br>= D in RReq).<br>• B = Decoupled Authentication<br>is supported and can be used<br>as a primary or fallback<br>challenge method if a<br>challenge is necessary<br>(Transaction Status = D in<br>either ARes or RReq). | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O |  |

---

<a id="page-194"></a>

## PDF page 194

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Requestor ID<br>Field Name:<br>threeDSRequesto<br>rID | DS-defined 3DS<br>Requestor identifier. | 3DS Server | Length: Variable, maximum 35<br>characters<br>JSON Data Type: String<br>Values accepted:<br>• Any individual DS may impose<br>specific formatting, character<br>and/or other requirements on<br>the contents of this field. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R |  |
| 3DS Requestor<br>Name<br>Field Name:<br>threeDSRequesto<br>rName | DS-defined 3DS<br>Requestor name. | 3DS Server | Length: Variable, maximum 40<br>characters<br>JSON Data Type: String<br>Values accepted:<br>• Any individual DS may impose<br>specific formatting, character<br>and/or other requirements on<br>the contents of this field. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R |  |
| 3DS Requestor<br>Prior Transaction<br>Authentication<br>Information<br>Field Name:<br>threeDSRequesto<br>rPriorAuthentic<br>ationInfo | Information about how the<br>3DS Requestor<br>authenticated the<br>Cardholder as part of a<br>previous 3DS transaction. | 3DS Server | Size: Variable, 1–3 elements<br>JSON Data Type: Array of objects<br>Values accepted:<br>• Refer to Table A.13 for data<br>elements to include.<br>Note: Data will be formatted into a<br>JSON object prior to being placed<br>into the 3DS Requestor Prior<br>Transaction Authentication<br>Information field of the message. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required for<br>3RI in the<br>case of<br>Decoupled<br>Authentication<br>Fallback or for<br>SPC |

---

<a id="page-195"></a>

## PDF page 195

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Requestor<br>SPC Support<br>Field Name:<br>threeDSRequesto<br>rSpcSupport | Indicate if the 3DS<br>Requestor supports the<br>SPC authentication.<br>Note: If present, this field<br>contains the value Y. | 3DS Server | JSON Data Type: String<br>Value accepted:<br>• Y = Supported | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required if<br>supported by<br>the 3DS<br>Requestor |
| 3DS Requestor<br>URL<br>Field Name:<br>threeDSRequesto<br>rURL | The Fully Qualified URL of<br>the 3DS Requestor<br>Website or customer care<br>site.<br>This data element provides<br>additional information to<br>the receiving 3-D Secure<br>system if a problem arises<br>and contact information<br>should be provided. | 3DS Server | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Fully Qualified URL<br>Example:<br>• https://server.domainname.co<br>m | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R |  |
| 3DS Server<br>Operator ID<br>Field Name:<br>threeDSServerOp<br>eratorID | DS-assigned 3DS Server<br>identifier.<br>Each DS can provide a<br>unique ID to each 3DS<br>Server on an individual<br>basis. | 3DS Server | Length: Variable, maximum 32<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Any individual DS may impose<br>specific formatting and<br>character requirements on the<br>contents of this field. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C<br>PReq = C | Requirements<br>for the<br>presence of<br>this field are<br>DS-specific. |

---

<a id="page-196"></a>

## PDF page 196

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Server<br>Reference Number<br>Field Name:<br>threeDSServerRe<br>fNumber | Unique identifier assigned<br>by the EMVCo Secretariat<br>upon testing and approval. | 3DS Server | Length: Variable, maximum 32<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Set by the EMVCo Secretariat. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R<br>PReq = R<br>ORes = C | Required in<br>the ORes<br>message for a<br>3DS Server<br>receiving an<br>OReq<br>message. |
| 3DS Server<br>Transaction ID<br>Field Name:<br>threeDSServerTr<br>ansID | Universally unique<br>transaction identifier<br>assigned by the 3DS<br>Server to identify a single<br>transaction. | 3DS Server | Length: 36 characters<br>JSON Data Type: String<br>Value accepted:<br>• Canonical format as defined in<br>IETF RFC 4122. May use any<br>of the specified versions if the<br>output meets specified<br>requirements. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R<br>ARes = R<br>CReq = R<br>CRes = R<br>ORes = C<br>PReq = R<br>PRes = R<br>RReq = R<br>RRes = R<br>Erro = C | • Required in<br>the Error<br>Message if<br>available<br>(e.g., can<br>be obtained<br>from a<br>message or<br>is being<br>generated).<br>• Required in<br>the ORes<br>message<br>for a 3DS<br>Server<br>receiving an<br>OReq<br>message. |

---

<a id="page-197"></a>

## PDF page 197

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Server URL<br>Field Name:<br>threeDSServerUR<br>L | Fully Qualified URL of the<br>3DS Server to which the<br>DS will send the RReq<br>message after the<br>challenge has completed.<br>Incorrect formatting will<br>result in a failure to deliver<br>the transaction results via<br>the RReq message. | 3DS Server | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Fully Qualified URL<br>Example value:<br>https://server.adomainname.net | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R |  |
| 3RI Indicator<br>Field Name:<br>threeRIInd | Indicates the type of 3RI<br>request.<br>This data element provides<br>additional information to<br>the ACS to determine the<br>best approach for handling<br>a 3RI request. | 3DS Server | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Recurring transaction<br>• 02 = Instalment transaction<br>• 03 = Add card<br>• 04 = Maintain card information<br>• 05 = Account verification<br>• 06 = Split shipment<br>• 07 = Top-up<br>• 08 = Mail Order<br>• 09 = Telephone Order<br>• 10 = Trust List status check<br>• 11 = Other payment<br>• 12 = Billing Agreement<br>• 13 = Device Binding status<br>check | 03-3RI | 01-PA<br>02-NPA | AReq = R |  |

---

<a id="page-198"></a>

## PDF page 198

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | • 14 = Card Security Code<br>status check<br>• 15 = Delayed shipment<br>• 16 = Split payment<br>• 17 = FIDO credential deletion<br>• 18 = FIDO credential<br>registration<br>• 19 = Decoupled Authentication<br>Fallback<br>• 20–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use |  |  |  |  |
| Accept Language<br>Field Name:<br>acceptLanguage | Value representing the<br>Browser language<br>preference present in the<br>HTTP header, as defined<br>in IETF BCP 47. | 3DS Server | Size: Variable, 1–99 elements<br>JSON Data Type: Array of string<br>String: Variable, maximum 100<br>characters | 02-BRW | 01-PA<br>02-NPA | AReq = R |  |

---

<a id="page-199"></a>

## PDF page 199

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Account Type<br>Field Name:<br>acctType | Indicates the type of<br>account. For example, for<br>a multi-account card<br>product. | 3DS Server | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Not applicable<br>• 02 = Credit<br>• 03 = Debit<br>• 04–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = DS or Payment<br>System-specific | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if<br>the 3DS<br>Requestor is<br>asking the<br>Cardholder<br>which<br>Account Type<br>they are using<br>before making<br>the purchase.<br>Required in<br>some markets<br>(for example,<br>for Merchants<br>in Brazil).<br>Otherwise,<br>Optional. |
| Acquirer BIN<br>Field Name:<br>acquirerBIN | Acquiring institution<br>identification code as<br>assigned by the DS<br>receiving the AReq<br>message. | 3DS Server | Length: Variable, maximum 11<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• This value correlates to the<br>Acquirer BIN as defined by<br>each Payment System. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | 01-PA:<br>AReq = R<br>02-NPA:<br>AReq = O |  |

---

<a id="page-200"></a>

## PDF page 200

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Acquirer Country<br>Code<br>Field Name:<br>acquirerCountry<br>Code | The code of the country<br>where the acquiring<br>institution is located (in<br>accordance with ISO<br>3166-1).<br>The DS may edit the value<br>provided by the 3DS<br>Server. | 3DS Server<br>DS | Length: 3 characters<br>JSON Data Type: String<br>Values accepted:<br>• ISO 3166-1 numeric three-digit<br>country code, other than<br>exceptions listed in Table A.5. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R |  |
| Acquirer Country<br>Code Source<br>Field Name:<br>acquirerCountry<br>CodeSource | This data element is<br>populated by the system<br>setting the Acquirer<br>Country Code.<br>The DS may edit the value<br>provided by the 3DS<br>Server. | 3DS Server<br>DS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = 3DS Server<br>• 02 = DS<br>• 03–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R |  |
| Acquirer Merchant<br>ID<br>Field Name:<br>acquirerMerchan<br>tID | Acquirer-assigned<br>Merchant identifier.<br>This may be the same<br>value that is used in<br>authorisation requests sent<br>on behalf of the 3DS<br>Requestor and is<br>represented in ISO 8583-1<br>formatting requirements. | 3DS Server | Length: Variable, maximum 35<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Individual Directory Servers<br>may impose specific format<br>and character requirements on<br>the contents of this field. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | 01-PA:<br>AReq = R<br>02-NPA<br>AReq = O |  |

---

<a id="page-201"></a>

## PDF page 201

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS Challenge<br>Mandated Indicator<br>Field Name:<br>acsChallengeMan<br>dated | Indication of whether a<br>challenge is required for<br>the transaction to be<br>authorised due to<br>local/regional mandates or<br>other variable. | ACS | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = Challenge is mandated<br>• N = Challenge is not<br>mandated | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = C | Required if<br>Transaction<br>Status = C or<br>D. |
| ACS Counter ACS<br>to SDK<br>Field Name:<br>acsCounterAtoS | Counter used as a security<br>measure in the ACS to<br>3DS SDK secure channel.<br>Note: The counter is the<br>decimal value equivalent<br>of the byte, encoded as a<br>numeric string. | ACS | Length: 3 characters<br>JSON Data Type: String<br>Values accepted:<br>• 000–255 | 01-APP | 01-PA<br>02-NPA | CRes = R |  |
| ACS Decoupled<br>Confirmation<br>Indicator<br>Field Name:<br>acsDecConInd | Indicates whether the ACS<br>confirms use of Decoupled<br>Authentication and agrees<br>to use Decoupled<br>Authentication to<br>authenticate the<br>Cardholder. | ACS | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = Confirms Decoupled<br>Authentication will be used<br>• N = Decoupled Authentication<br>will not be used<br>Note: if 3DS Requestor Decoupled<br>Request Indicator = N, a value of<br>Y cannot be returned in the ACS<br>Decoupled Confirmation Indicator.<br>Note: if Transaction Status = D, a<br>value of N is not valid. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = C | Required if<br>Transaction<br>Status = D |

---

<a id="page-202"></a>

## PDF page 202

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS Ephemeral<br>Public Key (QT)<br>Field Name:<br>acsEphemPubKey | Public key component of<br>the ephemeral key pair<br>generated by the ACS and<br>used to establish session<br>keys between the 3DS<br>SDK and the ACS.<br>See Section 6.2.3.2 for<br>additional detail. | ACS | Length: Variable, maximum 256<br>characters<br>JSON Data Type: Object | 01-APP | 01-PA<br>02-NPA | See ACS<br>Signed<br>Content | See ACS<br>Signed<br>Content. |
| ACS HTML<br>Field Name:<br>acsHTML | HTML provided by the<br>ACS in the CRes<br>message. Used when<br>HTML is specified in the<br>ACS UI Type during the<br>Cardholder challenge. | ACS | Length: Variable, maximum<br>300000 characters<br>JSON Data Type: String<br>Value accepted:<br>• Base64url-encoded HTML<br>This value will be Base64url-<br>encoded prior to being placed into<br>the CRes message. | 01-APP | 01-PA<br>02-NPA | CRes = C | Required if<br>ACS UI Type<br>= 05 or 06. |
| ACS Operator ID<br>Field Name:<br>acsOperatorID | DS assigned ACS<br>identifier.<br>Each DS can provide a<br>unique ID to each ACS on<br>an individual basis. | ACS | Length: Variable, maximum 32<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Any individual DS may impose<br>specific formatting and<br>character requirements on the<br>contents of this field. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = C | Requirements<br>for the<br>presence of<br>this field are<br>DS-specific. |

---

<a id="page-203"></a>

## PDF page 203

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS Reference<br>Number<br>Field Name:<br>acsReferenceNum<br>ber | Unique identifier assigned<br>by the EMVCo Secretariat<br>upon Testing and<br>Approval. | ACS | Length: Variable, maximum 32<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Set by the EMVCo Secretariat. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = R<br>ORes = C | Required in<br>the ORes<br>message for<br>an ACS<br>receiving an<br>OReq<br>message. |
| ACS Rendering<br>Type<br>Field Name:<br>acsRenderingTyp<br>e | Identifies the ACS<br>Interface and ACS UI<br>Template that the ACS will<br>first present to the<br>consumer. | ACS | JSON Data Type: Object<br>Values accepted:<br>• Refer to Table A.14 for data<br>elements to include.<br>Note: Data will be formatted into a<br>JSON object prior to being placed<br>into the acsRenderingType field<br>of the message. | 01-APP | 01-PA<br>02-NPA | ARes = C<br>RReq = C | • For ARes,<br>required if<br>Transaction<br>Status = C.<br>• For RReq,<br>required<br>unless ACS<br>Decoupled<br>Confirmatio<br>n Indicator<br>= Y. |

---

<a id="page-204"></a>

## PDF page 204

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS Signed<br>Content<br>Field Name:<br>acsSignedConten<br>t | Contains the JWS object<br>(represented as a string)<br>created by the ACS for the<br>ARes message.<br>See Section 6.2.3.2 for<br>details. | ACS | Length: Variable, maximum 16000<br>characters<br>JSON Data Type: String<br>Values accepted:<br>• The body of JWS object<br>(represented as a string) will<br>contain the following data<br>elements as defined in<br>Table A.1:<br>o ACS URL<br>o ACS Ephemeral Public Key<br>(QT)<br>o SDK Ephemeral Public Key<br>(QC) | 01-APP | 01-PA<br>02-NPA | ARes = C | Required if<br>Transaction<br>Status = C. |

---

<a id="page-205"></a>

## PDF page 205

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS Transaction ID<br>Field Name:<br>acsTransID | Universally Unique<br>transaction identifier<br>assigned by the ACS to<br>identify a single<br>transaction. | ACS | Length: 36 characters<br>JSON Data Type: String<br>Value accepted:<br>• Canonical format as defined in<br>IETF RFC 4122. May use any<br>of the specified versions if the<br>output meets specified<br>requirements. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = R<br>CReq = R<br>CRes = R<br>ORes = C<br>RReq = R<br>RRes = R<br>Erro = C | • Required in<br>the Error<br>Message if<br>available<br>(e.g., can<br>be obtained<br>from a<br>message or<br>is being<br>generated).<br>• Required<br>the in ORes<br>message<br>for an ACS<br>receiving an<br>OReq<br>message. |

---

<a id="page-206"></a>

## PDF page 206

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS UI Type<br>Field Name:<br>acsUiType | User interface type that the<br>3DS SDK will render,<br>which includes the specific<br>data mapping and<br>requirements. | ACS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Text<br>• 02 = Single Select<br>• 03 = Multi Select<br>• 04 = OOB<br>• 05 = HTML<br>• 06 = HTML OOB<br>• 07 = Information<br>• 08–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | 01-APP | 01-PA<br>02-NPA | CRes = C | Required<br>except for the<br>Final CRes<br>message. |

---

<a id="page-207"></a>

## PDF page 207

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS URL<br>Field Name:<br>acsURL | Fully Qualified URL of the<br>ACS to be used for the<br>challenge.<br>01-APP—3DS SDK will<br>send the Challenge<br>Request to this URL<br>02-BRW—3DS Requestor<br>will post the CReq to this<br>URL via the challenge<br>iframe.<br>For App-based, this data<br>element is contained within<br>the ACS Signed Content<br>JWS Object.<br>For Browser-based, this<br>data element is present as<br>its own object. | ACS | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Fully Qualified URL.<br>Example:<br>https://server.acsdomainname.co<br>m | 01-APP<br>02-BRW | 01-PA<br>02-NPA | 01-APP:<br>see ACS<br>Signed<br>Content<br>02-BRW:<br>ARes = C | • For 01-<br>APP, see<br>ACS Signed<br>Content.<br>• For 02-<br>BRW,<br>required if<br>Transaction<br>Status = C. |
| Address Match<br>Indicator<br>Field Name:<br>addrMatch | Indicates whether the<br>Cardholder Shipping<br>Address and Cardholder<br>Billing Address are the<br>same. | 3DS Server | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = Shipping Address matches<br>Billing Address<br>• N = Shipping Address does<br>not match Billing Address | 01-APP<br>02-BRW | 01-PA<br>02-NPA | AReq = O |  |

---

<a id="page-208"></a>

## PDF page 208

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| App IP Address<br>Field Name: appIp | External IP address (i.e.,<br>the device public IP<br>address) used by the 3DS<br>Requestor App when it<br>connects to the 3DS<br>Requestor environment. | 3DS Server | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String<br>Values accepted:<br>• IPv4 address. Refer to RFC<br>791.<br>• IPv6 address. Refer to RFC<br>4291. | 01-APP | 01-PA<br>02-NPA | AReq = C | Required<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |

- Required in the ARes message if Transaction Status = C or D.

Authentication Method

Indicates the list of authentication types the Issuer will use to challenge the Cardholder, when in the ARes message or what was used by the ACS when in the RReq message.

ACS Size: Variable, 1–99 elements

01-APP

01-PA

ARes = C

JSON Data Type: Array of string

02-BRW

02-NPA

RReq = C

Field Name: authenticationM ethod

String: 2 characters

03-3RI

Values accepted:

- Required in the RReq message if Transaction Status = Y or N.

- 01 = Static Passcode

- 02 = SMS OTP

Note: For 03-3RI, only present for Decoupled Authentication.

- 03 = Key fob or EMV card reader OTP

- 04 = App OTP

- 05 = OTP Other

- 06 = KBA

- 07 = OOB Biometrics

- 08 = OOB Login

- 09 = OOB Other

- 10 = Other

- 11 = Push Confirmation

- 12 = Decoupled

---

<a id="page-209"></a>

## PDF page 209

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | • 13 = WebAuthn<br>• 14 = SPC<br>• 15 = Behavioural biometrics<br>• 16 = Electronic ID<br>• 17–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use<br>If SDK Type = 02 and Split-SDK<br>Type/Limited Indicator = Y, a value<br>of 01 or 06 is not valid. |  |  |  |  |

---

<a id="page-210"></a>

## PDF page 210

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Authentication<br>Value<br>Field Name:<br>authenticationV<br>alue | Payment System-specific<br>value provided by the ACS<br>or the DS using an<br>algorithm defined by<br>Payment System.<br>Authentication Value may<br>be used to provide proof of<br>authentication. | ACS<br>DS | Length: Variable, maximum 4000<br>characters. Actual length defined<br>by Payment System rules.<br>JSON Data Type: String<br>Example:<br>A 20-byte value that has been<br>Base64-encoded, giving a 28-byte<br>result. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = C<br>RReq = C | 01-PA:<br>Required if<br>Transaction<br>Status = Y or<br>A<br>Conditional<br>based on DS<br>rules if<br>Transaction<br>Status = I<br>Omitted from<br>the RReq<br>message<br>when sent as<br>an<br>abandonment<br>notification<br>02-NPA:<br>Conditional<br>based on DS<br>rules. |
| Broadcast<br>Information<br>Field Name:<br>broadInfo | Structured information sent<br>between the 3DS Server,<br>the DS and the ACS. | 3DS Server<br>DS<br>ACS | Length: Variable, maximum 4096<br>characters<br>JSON Data Type: Object<br>Values accepted:<br>• Refer to Table A.27 for data<br>elements to include. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O<br>ARes = O |  |

---

<a id="page-211"></a>

## PDF page 211

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Browser Accept<br>Headers<br>Field Name:<br>browserAcceptHe<br>ader | Exact content of the HTTP<br>accept headers as sent to<br>the 3DS Requestor from<br>the Cardholder Browser. | 3DS Server | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• If the total length of the accept<br>header sent by the Browser<br>exceeds 2048 characters, the<br>3DS Server truncates the<br>excess portion.<br>Refer to Section A.6 for additional<br>detail. | 02-BRW | 01-PA<br>02-NPA | AReq = R |  |
| Browser IP Address<br>Field Name:<br>browserIP | IP address of the Browser<br>as returned by the HTTP<br>headers to the 3DS<br>Requestor. | 3DS Server | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String<br>Values accepted:<br>• IPv4 address. Refer to RFC<br>791.<br>• IPv6 address. Refer to RFC<br>4291. | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |

---

<a id="page-212"></a>

## PDF page 212

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Browser Java<br>Enabled<br>Field Name:<br>browserJavaEnab<br>led | Boolean that represents<br>the ability of the<br>Cardholder Browser to<br>execute Java.<br>Value is returned from the<br>navigator.javaEnabled<br>property.<br>Refer to Section A.6 for<br>additional detail. | 3DS Server | JSON Data Type: Boolean<br>Values accepted:<br>• true<br>• false | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required if<br>Browser<br>JavaScript<br>Enabled =<br>true;<br>otherwise<br>Optional. |
| Browser JavaScript<br>Enabled<br>Field Name:<br>browserJavascri<br>ptEnabled | Boolean that represents<br>the ability of the<br>Cardholder Browser to<br>execute JavaScript.<br>Refer to Section A.6 for<br>additional detail. | 3DS Server | JSON Data Type: Boolean<br>Values accepted:<br>• true<br>• false | 02-BRW | 01-PA<br>02-NPA | AReq = R |  |
| Browser Language<br>Field Name:<br>browserLanguage | Value representing the<br>Browser language as<br>defined in IETF BCP47.<br>Returned from<br>navigator.language<br>property.<br>Refer to Section A.6 for<br>additional detail. | 3DS Server | Length: Variable, maximum 35<br>characters<br>JSON Data Type: String | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required if<br>Browser<br>JavaScript<br>Enabled =<br>true;<br>otherwise<br>Optional. |

---

<a id="page-213"></a>

## PDF page 213

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Browser Screen<br>Color Depth<br>Field Name:<br>browserColorDep<br>th | Value representing the bit<br>depth of the colour palette<br>for displaying images, in<br>bits per pixel.<br>Obtained from the<br>Cardholder Browser using<br>the screen.colorDepth<br>property.<br>Refer to Section A.6 for<br>more details. | 3DS Server | Length: 1–2 characters; numeric<br>JSON Data Type: String<br>Values accepted:<br>• 1–99<br>Note: If an ACS does not support<br>the value provided, then the ACS<br>can use the closest supported<br>value. For example, if the value<br>provided = 30 and the ACS does<br>not support that value, then the<br>ACS could use the value = 24. | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required if<br>Browser<br>JavaScript<br>Enabled =<br>true;<br>otherwise<br>Optional. |
| Browser Screen<br>Height<br>Field Name:<br>browserScreenHe<br>ight | Total height of the<br>Cardholder’s screen in<br>pixels.<br>Value is returned from the<br>screen.height property.<br>Refer to Section A.6 for<br>additional detail. | 3DS Server | Length: Variable, 1–6 characters;<br>numeric<br>JSON Data Type: String | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required if<br>Browser<br>JavaScript<br>Enabled =<br>true;<br>otherwise<br>Optional. |
| Browser Screen<br>Width<br>Field Name:<br>browserScreenWi<br>dth | Total width of the<br>Cardholder’s screen in<br>pixels.<br>Value is returned from the<br>screen.width property.<br>Refer to Section A.6 for<br>additional detail. | 3DS Server | Length: Variable, 1–6 characters;<br>numeric<br>JSON Data Type: String | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required if<br>Browser<br>JavaScript<br>Enabled =<br>true;<br>otherwise<br>Optional. |

---

<a id="page-214"></a>

## PDF page 214

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Browser Time Zone<br>Field Name:<br>browserTZ | Time zone offset in<br>minutes between UTC and<br>the Cardholder Browser<br>local time.<br>Note that the offset is<br>positive if the local time<br>zone is behind UTC and<br>negative if it is ahead. | 3DS Server | Length: Variable, 1–5 characters<br>JSON Data Type: String<br>Value accepted:<br>• Value is returned from the<br>getTimezoneOffset() method.<br>Example time zone offset values in<br>minutes:<br>If UTC -5 hours:<br>• 300<br>• +300<br>If UTC +5 hours:<br>• -300<br>Refer to Section A.6 for additional<br>detail. | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required if<br>Browser<br>JavaScript<br>Enabled =<br>true;<br>otherwise<br>Optional. |
| Browser User-Agent<br>Field Name:<br>browserUserAgen<br>t | Exact content of the HTTP<br>user-agent header. | 3DS Server | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String<br>Value accepted:<br>Note: If the total length of the<br>User-Agent sent by the Browser<br>exceeds 2048 characters, the 3DS<br>Server truncates the excess<br>portion.<br>Refer to Section A.6 for additional<br>detail. | 02-BRW | 01-PA<br>02-NPA | AReq = R |  |

---

<a id="page-215"></a>

## PDF page 215

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Browser User<br>Device ID<br>Field Name:<br>deviceId | Unique and immutable<br>identifier linked to a device<br>that is consistent across<br>3DS transactions for the<br>specific user device.<br>Examples:<br>• Hardware Device ID<br>• Platform-calculated<br>device fingerprint<br>Refer to D021 in the SDK<br>Device Information | 3DS Server | Length: Variable, maximum 64<br>characters<br>JSON Data Type: String | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required if<br>available. |
| Browser User ID<br>Field Name:<br>userId | Identifier of the transacting<br>user’s Browser Account<br>ID.<br>This identifier is a unique<br>immutable hash of the<br>user’s account identifier for<br>the given Browser,<br>provided as a string.<br>Note: Cardholders may<br>have more than one<br>account on a given<br>Browser.<br>Refer to D026 in the SDK<br>Device Information | 3DS Server | Length: Variable, maximum 64<br>characters<br>JSON Data Type: String | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required if<br>available. |

---

<a id="page-216"></a>

## PDF page 216

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Card Range Data<br>Field Name:<br>cardRangeData | Card range data from the<br>DS indicating the most<br>recent Protocol Versions<br>supported by the ACS,<br>and, optionally, the DS that<br>hosts that range, and, if<br>configured, the ACS URL<br>for the 3DS Method.<br>Additionally, it identifies<br>the 3DS features<br>supported by the ACS,<br>such as Trust List or<br>Decoupled Authentication.<br>There may be as many<br>JSON objects as there are<br>stored card ranges in the<br>DS. | DS | Size: Variable, 1–200000 elements<br>JSON Data Type: Array of objects<br>Values accepted:<br>• See Table A.6 for Card Range<br>Data data elements. | N/A | N/A | PRes = C | Required if<br>the Serial<br>Number has<br>changed in<br>the prior PRes<br>message or is<br>absent in the<br>PReq<br>message<br>AND<br>Not present if<br>the Card<br>Range Data<br>File URL is<br>present |
| Card Range Data<br>Download Indicator<br>Field Name:<br>cardRangeDataDo<br>wnloadInd | Indicates if the 3DS Server<br>supports Card Range Data<br>from a file.<br>Note: If present, this field<br>contains the value Y. | 3DS Server | Length: 1 character<br>JSON Data Type: String<br>Value accepted:<br>• Y = Download supported | N/A | N/A | PReq = C | Present only if<br>the 3DS<br>Server<br>supports the<br>Card Range<br>Data File<br>download |

---

<a id="page-217"></a>

## PDF page 217

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Card Range Data<br>File URL<br>Field Name:<br>cardRangeDataFi<br>leURL | Fully Qualified URL of the<br>DS File containing the<br>Card Range Data for<br>download. | DS | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Fully Qualified URL<br>Example:<br>• https://server.dsdomainname.c<br>om/cardfile.json | N/A | N/A | PRes = C | Present only if<br>the 3DS<br>Server and<br>the DS are<br>using the<br>Card Range<br>Data File<br>download |
| Card/Token Expiry<br>Date<br>Field Name:<br>cardExpiryDate | Expiry Date of the PAN or<br>token supplied to the 3DS<br>Requestor by the<br>Cardholder. | 3DS Server | Length: 4 characters<br>JSON Data Type: String<br>Format accepted:<br>• YYMM | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | The<br>requirements<br>for the<br>presence of<br>this field are<br>DS-specific. |
| Card Security Code<br>Field Name:<br>cardSecurityCod<br>e | Three- or four-digit security<br>code printed on the card. | 3DS Server | Length: Variable, 3–4 characters,<br>numeric. Action defined by<br>Payment System rules.<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Conditional<br>based on DS<br>rules |

Card Security Code Status

Enables the communication of Card Security Code Status between the ACS, the DS and the 3DS Requestor

ACS

Length: 1 character

01-APP

01-PA

AReq = C

Conditional based on DS rules

DS

JSON Data Type: String

02-BRW

02-NPA

ARes = C

Field Name: cardSecurityCod eStatus

Values accepted:

03-3RI

- Y = Validated

- N = Failed validation

- U = Status unknown, unavailable, or does not apply

---

<a id="page-218"></a>

## PDF page 218

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Card Security Code<br>Status Source<br>Field Name:<br>cardSecurityCod<br>eStatusSource | This data element will be<br>populated by the system<br>setting Card Security Code<br>Status. | ACS<br>DS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = DS<br>• 02 = ACS<br>• 03–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C<br>ARes = C | Required if<br>the Card<br>Security Code<br>Status is<br>present. |
| Cardholder Account<br>Identifier<br>Field Name:<br>acctID | Additional information<br>about the account<br>optionally provided by the<br>3DS Requestor. | 3DS Server | Length: Variable, maximum 64<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O |  |
| Cardholder Account<br>Information<br>Field Name:<br>acctInfo | Additional information<br>about the Cardholder’s<br>account provided by the<br>3DS Requestor. | 3DS Server | Length: Variable<br>JSON Data Type: Object<br>Value accepted:<br>• Refer to Table A.10 for<br>Cardholder Account<br>Information data elements. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O | Optional, but<br>strongly<br>recommended<br>to include. |
| Cardholder Account<br>Number<br>Field Name:<br>acctNumber | Account number that will<br>be used in the<br>authorisation request for<br>payment transactions.<br>May be represented by<br>PAN, Payment Token. | 3DS Server | Length: Variable, 13–19<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Format represented ISO 7812. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R |  |

---

<a id="page-219"></a>

## PDF page 219

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cardholder Billing<br>Address City<br>Field Name:<br>billAddrCity | The city of the Cardholder<br>billing address associated<br>with the card used for this<br>purchase. | 3DS Server | Length: Variable, maximum 50<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | 01-PA:<br>Required<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information.<br>02-NPA:<br>Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |

---

<a id="page-220"></a>

## PDF page 220

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cardholder Billing<br>Address Country<br>Field Name:<br>billAddrCountry | The country of the<br>Cardholder billing address<br>associated with the card<br>used for this purchase. | 3DS Server | Length: 3 characters<br>JSON Data Type: String<br>Values accepted:<br>• ISO 3166-1 numeric three-digit<br>country code, other than<br>exceptions listed in Table A.5. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if<br>Cardholder<br>Billing<br>Address State<br>is present.<br>01-PA:<br>Required<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information.<br>02-NPA:<br>Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |

---

<a id="page-221"></a>

## PDF page 221

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cardholder Billing<br>Address Line 1<br>Field Name:<br>billAddrLine1 | First line of the street<br>address or equivalent local<br>portion of the Cardholder<br>billing address associated<br>with the card used for this<br>purchase. | 3DS Server | Length: Variable, maximum 50<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | 01-PA:<br>Required<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information.<br>02-NPA:<br>Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |
| Cardholder Billing<br>Address Line 2<br>Field Name:<br>billAddrLine2 | Second line of the street<br>address or equivalent local<br>portion of the Cardholder<br>billing address associated<br>with the card used for this<br>purchase. | 3DS Server | Length: Variable, maximum 50<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |

---

<a id="page-222"></a>

## PDF page 222

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cardholder Billing<br>Address Line 3<br>Field Name:<br>billAddrLine3 | Third line of the street<br>address or equivalent local<br>portion of the Cardholder<br>billing address associated<br>with the card used for this<br>purchase. | 3DS Server | Length: Variable, maximum 50<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |
| Cardholder Billing<br>Address Postal<br>Code<br>Field Name:<br>billAddrPostCod<br>e | ZIP or other postal code of<br>the Cardholder billing<br>address associated with<br>the card used for this<br>purchase. | 3DS Server | Length: Variable, maximum 16<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | 01-PA:<br>Required<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information.<br>02-NPA:<br>Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |

---

<a id="page-223"></a>

## PDF page 223

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cardholder Billing<br>Address State<br>Field Name:<br>billAddrState | The state or province of<br>the Cardholder billing<br>address associated with<br>the card used for this<br>purchase. | 3DS Server | Length: Variable, maximum 3<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Country subdivision code<br>defined in ISO 3166-2.<br>For example, using the ISO entry<br>US-CA (California, United States),<br>the correct value for this field =<br>CA. Note that the country and<br>hyphen are not included in this<br>value. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | 01-PA:<br>Required<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information, or<br>State is not<br>applicable for<br>this country.<br>02-NPA:<br>Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information, or<br>State is not<br>applicable for<br>this country. |

Cardholder Email Address

The email address associated with the account that is either entered by the Cardholder or is on file with the 3DS Requestor.

3DS Server Length: Variable, maximum 254 characters

01-APP

01-PA

AReq = C Required (if available) unless market or regional mandate restricts sending this information.

02-BRW

02-NPA

Field Name: email

JSON Data Type: String

03-3RI

Value accepted:

- Shall meet requirements of Section 3.4 of IETF RFC 5322.

---

<a id="page-224"></a>

## PDF page 224

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cardholder Home<br>Phone Number<br>Field Name:<br>homePhone | The home phone number<br>provided by the<br>Cardholder. | 3DS Server | Length: Variable<br>• cc: 1–3 characters<br>• subscriber: variable, maximum<br>15 characters<br>Format: JSON object; strings<br>Values accepted:<br>• Country Code and Subscriber<br>sections of the number<br>represented by the following<br>named fields:<br>o cc<br>o subscriber<br>Refer to ITU-E.164 for additional<br>information on format and length.<br>Example:<br>"homePhone": {<br>"cc": "1" ,<br>"subscriber": "1234567899"<br>} | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |

---

<a id="page-225"></a>

## PDF page 225

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cardholder<br>Information Text<br>Field Name:<br>cardholderInfo | Text provided by the<br>ACS/Issuer to Cardholder<br>during a Frictionless or<br>Decoupled transaction.<br>The Issuer can provide<br>information to Cardholder.<br>For example, “Additional<br>authentication is needed<br>for this transaction, please<br>contact (Issuer Name) at<br>xxx-xxx-xxxx” with<br>optionally the Issuer and<br>Payment System images.<br>Refer to A.20 for UI<br>example. | ACS | Length: Variable<br>JSON Data Type: Object<br>Required:<br>• text<br>o JSON Data Type: String<br>o Variable, 1–128 characters<br>Optional:<br>• issuerImage<br>o JSON Data Type: String<br>o Variable, maximum 256<br>characters<br>o Value accepted: Fully<br>Qualified URL<br>• paymentSystemImage<br>o JSON Data Type: String<br>o Variable, maximum 256<br>characters<br>o Value accepted: Fully<br>Qualified URL | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = C<br>RReq = O | Required if<br>ACS<br>Decoupled<br>Confirmation<br>Indicator = Y<br>Otherwise,<br>Optional for<br>the ACS. |

---

<a id="page-226"></a>

## PDF page 226

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cardholder Mobile<br>Phone Number<br>Field Name:<br>mobilePhone | The mobile phone number<br>provided by the<br>Cardholder. | 3DS Server | Length: Variable<br>• cc: 1–3 characters<br>• subscriber: variable, maximum<br>15 characters<br>Format: JSON object; strings<br>Values accepted:<br>• Country Code and Subscriber<br>sections of the number<br>represented by the following<br>named fields:<br>o cc<br>o subscriber<br>Refer to ITU-E.164 for additional<br>information on format and length.<br>Example:<br>"mobilePhone":{<br>"cc": "1" ,<br>"subscriber":"1234567899"<br>} | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |

---

<a id="page-227"></a>

## PDF page 227

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cardholder Name<br>Field Name:<br>cardholderName | Name of the Cardholder. | 3DS Server | Length: Variable, 1–45 characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |
| Cardholder<br>Shipping Address<br>City<br>Field Name:<br>shipAddrCity | City portion of the shipping<br>address requested by the<br>Cardholder. | 3DS Server | Length: Variable, maximum 50<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |
| Cardholder<br>Shipping Address<br>Country<br>Field Name:<br>shipAddrCountry | Country of the shipping<br>address requested by the<br>Cardholder. | 3DS Server | Length: 3 characters<br>JSON Data Type: String<br>Value accepted:<br>• ISO 3166-1 three-digit country<br>code, other than exceptions<br>listed in Table A.5. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if<br>Cardholder<br>Shipping<br>Address State<br>is present.<br>Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |

---

<a id="page-228"></a>

## PDF page 228

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cardholder<br>Shipping Address<br>Line 1<br>Field Name:<br>shipAddrLine1 | First line of the street<br>address or equivalent local<br>portion of the shipping<br>address requested by the<br>Cardholder. | 3DS Server | Length: Variable, maximum 50<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |
| Cardholder<br>Shipping Address<br>Line 2<br>Field Name:<br>shipAddrLine2 | The second line of the<br>street address or<br>equivalent local portion of<br>the shipping address<br>requested by the<br>Cardholder. | 3DS Server | Length: Variable, maximum 50<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |
| Cardholder<br>Shipping Address<br>Line 3<br>Field Name:<br>shipAddrLine3 | The third line of the street<br>address or equivalent local<br>portion of the shipping<br>address requested by the<br>Cardholder. | 3DS Server | Length: Variable, maximum 50<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |

---

<a id="page-229"></a>

## PDF page 229

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cardholder<br>Shipping Address<br>Postal Code<br>Field Name:<br>shipAddrPostCod<br>e | The ZIP or other postal<br>code of the shipping<br>address requested by the<br>Cardholder. | 3DS Server | Length: Variable, maximum 16<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |
| Cardholder<br>Shipping Address<br>State<br>Field Name:<br>shipAddrState | The state or province of<br>the shipping address<br>associated with the card<br>being used for this<br>purchase. | 3DS Server | Length: Variable, maximum 3<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Country subdivision code<br>defined in ISO 3166-2.<br>For example, using the ISO entry<br>US-CA (California, United States),<br>the correct value for this field =<br>CA. Note that the country and<br>hyphen are not included in this<br>value. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information, or<br>State is not<br>applicable for<br>this country. |

---

<a id="page-230"></a>

## PDF page 230

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cardholder Work<br>Phone Number<br>Field Name:<br>workPhone | The work phone number<br>provided by the<br>Cardholder. | 3DS Server | Length: Variable<br>• cc: 1–3 characters<br>• subscriber: Variable,<br>maximum 15 characters<br>JSON Data Type: String<br>Values accepted:<br>• Country Code and Subscriber<br>sections of the number<br>represented by the following<br>named fields:<br>o cc<br>o subscriber<br>Refer to ITU-E.164 for additional<br>information on format and length.<br>Example:<br>"workPhone":{<br>"cc":"1",<br>"subscriber":"1234567899"<br>} | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required (if<br>available)<br>unless market<br>or regional<br>mandate<br>restricts<br>sending this<br>information. |

---

<a id="page-231"></a>

## PDF page 231

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Challenge<br>Additional Code<br>Field Name:<br>challengeAddCod<br>e | Indicates to the ACS that<br>the Cardholder selected<br>the additional choice.<br>Note: If present, this field<br>contains the value Y. | 3DS SDK | Length: 1 character<br>JSON Data Type: String<br>Value accepted:<br>• Y = Additional choice selected | 01-APP | 01-PA<br>02-NPA | CReq = C | Required for<br>Native UI:<br>• if the<br>Challenge<br>Additional<br>Label was<br>present in<br>the CRes<br>message<br>AND<br>• if the<br>Challenge<br>Additional<br>choice is<br>selected. |
| Challenge<br>Additional Label<br>Field Name:<br>challengeAddLab<br>el | UI label for the additional<br>choice button provided by<br>the ACS. | ACS | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | CRes = C | See<br>Table A.20 for<br>presence<br>conditions. |

---

<a id="page-232"></a>

## PDF page 232

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Challenge<br>Cancelation<br>Indicator<br>Field Name:<br>challengeCancel | Indicator informing the<br>ACS and the DS that the<br>authentication has been<br>cancelled. | 3DS SDK<br>ACS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Cardholder selected<br>“Cancel”<br>• 02 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo).<br>• 03 = Transaction Timed Out –<br>Decoupled Authentication<br>• 04 = Transaction Timed Out at<br>ACS – other timeouts<br>• 05 = Transaction Timed Out at<br>ACS – First CReq not received<br>by ACS<br>• 06 = Transaction Error<br>• 07 = Unknown<br>• 08 = Transaction Timed Out at<br>3DS SDK<br>• 09 = Error Message in<br>response to the CRes<br>message sent by the ACS<br>• 10 = Error Message in<br>response to the CReq<br>message received by the ACS | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | CReq = C<br>RReq = C | • Required in<br>CReq for<br>01-APP if<br>the<br>authenticati<br>on<br>transaction<br>was<br>cancelled<br>by user<br>interaction<br>with the<br>cancellation<br>button in<br>the UI or for<br>other<br>reasons as<br>indicated.<br>• Required in<br>the RReq if<br>the ACS<br>identifies<br>that the<br>authenticati<br>on<br>transaction<br>was<br>cancelled<br>for reasons<br>as<br>indicated. |

---

<a id="page-233"></a>

## PDF page 233

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | • 11–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for future<br>DS use |  |  |  | Value of 04 or<br>05 is required<br>if Transaction<br>Status<br>Reason = 14. |
| Challenge<br>Completion<br>Indicator<br>Field Name:<br>challengeComple<br>tionInd | Indicator of the state of the<br>ACS challenge cycle and<br>whether the challenge has<br>completed or will require<br>additional messages. Shall<br>be populated in all CRes<br>messages to convey the<br>current state of the<br>transaction.<br>Note: If set to Y, the ACS<br>will populate the<br>Transaction Status in the<br>CRes message. | ACS | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = Challenge completed, and<br>no further challenge message<br>exchanges are required<br>• N = Challenge not completed<br>and additional challenge<br>message exchanges are<br>required | 01-APP | 01-PA<br>02-NPA | CRes = R |  |
| Challenge Data<br>Entry<br>Field Name:<br>challengeDataEn<br>try | Contains the data that the<br>Cardholder entered in the<br>Native UI text field.<br>Note: ACS UI Type = 04,<br>05, 06 and 07 are not<br>supported.<br>Example:<br>"challengeSelectInfo<br>":[ | 3DS SDK | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | CReq = C | Required if:<br>• ACS UI<br>Type = 01,<br>02, or 03;<br>AND<br>• Challenge<br>data has<br>been<br>entered in<br>the Native<br>UI text field;<br>AND |

---

<a id="page-234"></a>

## PDF page 234

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | {"phon":"Mobile ****<br>**** 321"},<br>{"mail":"Email<br>a*******g**@g***.com<br>"}]<br>The Cardholder selects the<br>phone option:<br>"challengeDataEntry"<br>:"phon" |  |  |  |  |  | • Challenge<br>Cancelation<br>Indicator is<br>not present;<br>AND<br>• Resend<br>Challenge<br>Information<br>Code is not<br>present;<br>AND<br>• Challenge<br>Additional<br>Code is not<br>present<br>See<br>Table A.16 for<br>Challenge<br>Data Entry<br>conditions. |
| Challenge Data<br>Entry 2<br>Field Name:<br>challengeDataEn<br>tryTwo | Contains the data that the<br>Cardholder entered in the<br>Native UI text field.<br>Note: Supported only for<br>ACS UI Type = 01. | 3DS SDK | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | CReq = C | Required if:<br>• ACS UI<br>Type = 01;<br>AND<br>• Challenge<br>Entry Box 2<br>object is<br>provided by<br>the ACS;<br>AND |

---

<a id="page-235"></a>

## PDF page 235

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  | • Challenge<br>data has<br>been<br>entered in<br>the second<br>entry<br>box/UI;<br>AND<br>• Challenge<br>Cancelation<br>Indicator is<br>not present;<br>AND<br>• Resend<br>Challenge<br>Information<br>Code is not<br>present;<br>AND<br>• Challenge<br>Additional<br>Code is not<br>present<br>See<br>Table A.16 for<br>Challenge<br>Data Entry<br>conditions. |

---

<a id="page-236"></a>

## PDF page 236

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Challenge Entry<br>Box<br>Field Name:<br>challengeEntryB<br>ox | Defines the setting of an<br>entry box in the Native UI<br>OTP/Text Template:<br>• Challenge Data Entry<br>Keyboard Type<br>• Challenge Data Entry<br>Autofill<br>• Challenge Data Entry<br>Autofill Type<br>• Challenge Data Entry<br>Length Maximum<br>• Challenge Data Entry<br>Label<br>• Challenge Data Entry<br>Masking<br>• Challenge Data Entry<br>Masking Toggle | ACS | Length: Variable<br>JSON Data Type: Object<br>Values accepted:<br>• Refer to Table A.26 | 01-APP | 01-PA<br>02-NPA | CRes = C | See<br>Table A.20 for<br>conditions. |

---

<a id="page-237"></a>

## PDF page 237

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Challenge Entry<br>Box 2<br>Field Name:<br>challengeEntryB<br>oxTwo | Defines the setting of an<br>entry box in the Native UI<br>OTP/Text Template:<br>• Challenge Data Entry<br>Keyboard Type<br>• Challenge Data Entry<br>Autofill<br>• Challenge Data Entry<br>Autofill Type<br>• Challenge Data Entry<br>Length Maximum<br>• Challenge Data Entry<br>Label<br>• Challenge Data Entry<br>Masking<br>• Challenge Data Entry<br>Masking Toggle | ACS | Length: Variable<br>JSON Data Type: Object<br>Values accepted:<br>• Refer to Table A.26 | 01-APP | 01-PA<br>02-NPA | CRes = C | See<br>Table A.20 for<br>conditions. |
| Challenge Error<br>Reporting<br>Field Name:<br>challengeErrorR<br>eporting | Copy of the Erro Message<br>sent or received by the<br>ACS in case of error in the<br>CReq/CRes messages. | ACS | Length: Variable<br>JSON Data Type: Object<br>Values accepted:<br>• Refer to Table B.12 for data<br>elements | 01-APP<br>02-BRW | 01-PA<br>02-NPA | RReq = C | Required if<br>Challenge<br>Cancelation<br>Indicator = 09<br>or 10. |

---

<a id="page-238"></a>

## PDF page 238

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Challenge HTML<br>Data Entry<br>Field Name:<br>challengeHTMLDa<br>taEntry | Data that the Cardholder<br>entered into the HTML UI.<br>Note: ACS UI Types 01,<br>02, 03, 04 and 07 are not<br>supported. | 3DS SDK | Length: Variable, maximum 256<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | CReq = C | Required if:<br>• ACS UI<br>Type = 05<br>or 06, AND<br>• Challenge<br>Cancelation<br>Indicator is<br>not present,<br>AND<br>• OOB<br>Continuatio<br>n Indicator<br>is NOT = 02 |
| Challenge<br>Information Header<br>Field Name:<br>challengeInfoHe<br>ader | Header text that for the<br>challenge information<br>screen that is being<br>presented. | ACS | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String<br>If the field is populated, this<br>information is displayed to the<br>Cardholder. | 01-APP | 01-PA<br>02-NPA | CRes = C | See<br>Table A.20 for<br>presence<br>conditions. |
| Challenge<br>Information Label<br>Field Name:<br>challengeInfoLa<br>bel | Text provided to the<br>Cardholder by the<br>ACS/Issuer to specify the<br>expected challenge entry. | ACS | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String<br>If the field is populated, this<br>information is displayed to the<br>Cardholder. | 01-APP | 01-PA<br>02-NPA | CRes = C | See<br>Table A.20 for<br>presence<br>conditions. |

---

<a id="page-239"></a>

## PDF page 239

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Challenge<br>Information Text<br>Field Name:<br>challengeInfoTe<br>xt | Text provided by the<br>ACS/Issuer to the<br>Cardholder during the<br>Challenge Message<br>exchange. | ACS | Length: Variable, maximum 350<br>characters<br>JSON Data Type: String<br>If the field is populated, this<br>information is displayed to the<br>Cardholder.<br>Note: Carriage return is supported<br>in this data element and is<br>represented by an “\n”.<br>Note: Bold text is supported in this<br>data element and is enclosed<br>between **.<br>Example:<br>• “This is **bold** text” is<br>rendered as “This is bold<br>text”. | 01-APP | 01-PA<br>02-NPA | CRes = C | See<br>Table A.20 for<br>presence<br>conditions. |
| Challenge<br>Information Text<br>Indicator<br>Field Name:<br>challengeInfoTe<br>xtIndicator | Indicates when the<br>Issuer/ACS would like a<br>warning icon or similar<br>visual indicator to draw<br>attention to the “Challenge<br>Information Text” that is<br>being displayed. | ACS | Length: 1 character<br>JSON Data Type: String<br>Value accepted:<br>• Y = Display indicator<br>• N = Do not display indicator<br>Note: If the field is populated, this<br>information is displayed to the<br>Cardholder. | 01-APP | 01-PA<br>02-NPA | CRes = C | See<br>Table A.20 for<br>presence<br>conditions. |

---

<a id="page-240"></a>

## PDF page 240

Data Element/

Description Source Length/Format/Values Device Channel

Message Category

Message Inclusion

Conditional

Field Name

Inclusion

Challenge No Entry

Indicator informing that the Cardholder submits an empty response (no data entered in the UI).

3DS SDK Length = 1 character

01-APP 01-PA

CReq = C Required if:

Field Name: challengeNoEntr y

JSON Data Type = String

02-NPA

- ACS UI Type = 01, 02, or 03, AND

Value accepted:

Note: If present this field contains the value Y.

- Y = No Data Entry

- Challenge Data Entry is not present, AND

- Challenge Data Entry 2 is not present when Challenge Entry Box 2 object was provided by the ACS, AND

- Challenge Cancelation Indicator is not present, AND

- Resend Challenge Information Code is not present, AND

---

<a id="page-241"></a>

## PDF page 241

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  | • Challenge<br>Additional<br>Code is not<br>present |
| Challenge Selection<br>Information<br>Field Name:<br>challengeSelect<br>Info | Selection information that<br>will be presented to the<br>Cardholder if the option is<br>single- or multi-select. The<br>variables will be sent in a<br>JSON Array and parsed by<br>the 3DS SDK for display in<br>the user interface.<br>Example:<br>"challengeSelectInfo<br>":[<br>{"phon":"Mobile ****<br>**** 321" },<br>{"mail":"Email<br>a*******g**@g***.com<br>"}<br>] | ACS | Size: Variable, 1–8 elements<br>JSON Data Type: Array of objects<br>Object: String key/value pair<br>Key length: Variable, maximum 4<br>characters<br>Value length: Variable, maximum<br>45 characters<br>Note: If the field is populated, this<br>information is displayed to the<br>Cardholder. | 01-APP | 01-PA<br>02-NPA | CRes = C | See<br>Table A.20 for<br>presence<br>conditions. |

---

<a id="page-242"></a>

## PDF page 242

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Challenge Window<br>Size<br>Field Name:<br>challengeWindow<br>Size | Dimensions of the<br>challenge iframe that has<br>been displayed to the<br>Cardholder. The ACS shall<br>reply with content that is<br>formatted to appropriately<br>render in this iframe to<br>provide the best possible<br>user experience.<br>Preconfigured sizes are<br>width x height in pixels of<br>the challenge iframe<br>displayed in the<br>Cardholder Browser<br>window. | 3DS<br>Requestor | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = 250 x 400<br>• 02 = 390 x 400<br>• 03 = 500 x 600<br>• 04 = 600 x 400<br>• 05 = Full screen | 02-BRW | 01-PA<br>02-NPA | CReq = R |  |

---

<a id="page-243"></a>

## PDF page 243

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Default-SDK Type<br>Field Name:<br>defaultSdkType | Indicates the<br>characteristics of a<br>Default-SDK.<br>SDK Variant: SDK<br>implementation<br>characteristics<br>Wrapped Indicator: If the<br>Default-SDK is embedded<br>as a wrapped component<br>in the 3DS Requestor App<br>Example:<br>"defaultSdkType":{<br>"sdkVariant":"01",<br>"wrappedInd":"Y"<br>} | 3DS Server | JSON Data Type: Object<br>sdkVariant<br>Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Native<br>• 02–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use<br>wrappedInd<br>Length: 1 character<br>JSON Data Type: String<br>Value accepted:<br>• Y = Wrapped<br>Only present if value = Y | 01-APP | 01-PA<br>02-NPA | AReq = C | Required if<br>SDK Type =<br>01 |

---

<a id="page-244"></a>

## PDF page 244

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Device Binding<br>Data Entry<br>Field Name:<br>deviceBindingDa<br>taEntry | Indicator provided by the<br>3DS SDK to the ACS to<br>confirm whether the<br>Cardholder gives consent<br>to bind the device. | 3DS SDK | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = Consent given to bind<br>device<br>• N = Consent not given to bind<br>device | 01-APP | 01-PA<br>02-NPA | CReq = C | Required if<br>• Device<br>Binding<br>Information<br>Text was<br>present in<br>the previous<br>CRes<br>message<br>AND<br>• Challenge<br>Cancelation<br>Indicator is<br>not present |
| Device Binding<br>Information Text<br>Field Name:<br>deviceBindingIn<br>foText | Text provided by the ACS<br>to the Cardholder during<br>the Device Binding<br>process.<br>Example:<br>• “Would you like to be<br>remembered on this<br>device?” | ACS | Length: Variable, maximum 64<br>characters | 01-APP | 01-PA<br>02-NPA | CRes = C | See<br>Table A.20 for<br>presence<br>conditions. |

---

<a id="page-245"></a>

## PDF page 245

Device Binding Status

Enables the communication of Device Binding Status between the ACS, the DS and the 3DS Requestor.

3DS Server

Length: 2 characters

01-APP

01-PA

AReq = O

DS

JSON Data Type: String

02-BRW

02-NPA

ARes = O

Field Name: deviceBindingSt atus

ACS

Values accepted:

03-3RI

RReq = O

- 01 = Device is not bound by Cardholder

For bound devices (value = 11–14), Device Binding Status also conveys the type of binding that was performed.

- 02 = Not eligible as determined by Issuer

- 03 = Pending confirmation by Cardholder

- 04 = Cardholder rejected

- 05 = Device Binding Status unknown, unavailable, or does not apply

- 06–10 = Reserved for EMVCo future use (values invalid until defined by EMVCo)

- 11 = Device is bound by Cardholder (device is bound using hardware / SIM internal to the Consumer Device. For instance, keys stored in a secure element on the device)

- 12 = Device is bound by Cardholder (device is bound using hardware external to the Consumer Device.  For example, an external FIDO Authenticator

- 13 = Device is bound by Cardholder (Device is bound using data that includes dynamically generated data

---

<a id="page-246"></a>

## PDF page 246

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | and could include a unique<br>device ID)<br>• 14 = Device is bound by<br>Cardholder (Device is bound<br>using static device data that<br>has been obtained from the<br>Consumer Device<br>• 15 = Device is bound by<br>Cardholder (Other method)<br>• 16–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use |  |  |  |  |
| Device Binding<br>Status Source<br>Field Name:<br>deviceBindingSt<br>atusSource | This data element will be<br>populated by the system<br>setting Device Binding<br>Status. | 3DS Server<br>DS<br>ACS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = 3DS Server<br>• 02 = DS<br>• 03 = ACS<br>• 04–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C<br>ARes = C<br>RReq = C | Required if<br>Device<br>Binding<br>Status is<br>present. |

---

<a id="page-247"></a>

## PDF page 247

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Device Channel<br>Field Name:<br>deviceChannel | Indicates the type of<br>channel interface being<br>used to initiate the<br>transaction. | 3DS Server | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = App-based (APP)<br>• 02 = Browser (BRW)<br>• 03 = 3DS Requestor Initiated<br>(3RI)<br>• 04–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R |  |
| Device Information<br>Field Name:<br>deviceInfo | Device information<br>gathered by the 3DS SDK<br>from a Consumer Device.<br>This is JSON name/value<br>pairs that as a whole is<br>Base64url-encoded.<br>This will be populated by<br>the DS as unencrypted<br>data to the ACS obtained<br>from SDK Encrypted Data. | DS | Length: Variable, maximum 64000<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Base64url-encoded JSON<br>object (represented as a<br>string)<br>Refer to EMV 3-D Secure SDK—<br>Device Information for values. | 01-APP | 01-PA<br>02-NPA | AReq = C | Required<br>between the<br>DS and the<br>ACS, but will<br>not be present<br>from the 3DS<br>Server to the<br>DS. |

---

<a id="page-248"></a>

## PDF page 248

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Device Information<br>Recognised Version<br>Field Name:<br>deviceInfoRecog<br>nisedVersion | Indicates the highest Data<br>Version of the Device<br>Information supported by<br>the ACS. | ACS | Length: Variable, minimum 3<br>characters<br>JSON Data Type: String<br>Values accepted:<br>• Any active Device Information<br>Data Version is considered a<br>valid value.<br>Refer to EMV Specification Bulletin<br>255 for values. | 01-APP | 01-PA<br>02-NPA | ARes = R |  |
| Device Rendering<br>Options Supported<br>Field Name:<br>deviceRenderOpt<br>ions | Identifies the SDK<br>Interface and SDK UI Type<br>that the device supports<br>for displaying specific<br>challenge user interfaces<br>within the 3DS SDK.<br>Note: As established in<br>[Req 314], all Device<br>Rendering Options must<br>be supported by the 3DS<br>SDK. | 3DS Server | Length: Variable<br>JSON Data Type: Object<br>Values accepted:<br>• Refer to Table A.15 for data<br>elements to include.<br>Note: Data will be formatted into a<br>JSON object prior to being placed<br>into the Device Rendering Options<br>Supported field of the message. | 01-APP | 01-PA<br>02-NPA | AReq = R |  |
| DS Protocol<br>Versions<br>Field Name:<br>dsProtocolVersi<br>ons | Contains the list of active<br>Protocol Versions<br>supported by the DS.<br>Note: Optional within the<br>Card Range Data (as<br>defined in Table A.6). | DS | Size: Variable,1–10 elements<br>JSON Data Type: Array of string<br>String: 5–8 characters<br>Values accepted:<br>• Refer to EMV Specification<br>Bulletin 255. | N/A | N/A | PRes = R |  |

---

<a id="page-249"></a>

## PDF page 249

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DS Reference<br>Number<br>Field Name:<br>dsReferenceNumb<br>er | EMVCo-assigned unique<br>identifier to track approved<br>DS. | DS | Length: Variable, maximum 32<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C<br>ARes = R<br>OReq = R | The DS will<br>populate the<br>AReq<br>message with<br>this data<br>element prior<br>to passing to<br>the ACS. |
| DS Transaction ID<br>Field Name:<br>dsTransID | Universally unique<br>transaction identifier<br>assigned by the DS to<br>identify a single<br>transaction. | DS | Length: 36 characters<br>JSON Data Type: String<br>Value accepted:<br>• Canonical format as defined in<br>IETF RFC 4122. May use any<br>of the specified versions as<br>long as the output meets<br>specified requirements. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C<br>ARes = R<br>OReq = R<br>ORes = R<br>RReq = R<br>RRes = R<br>PRes = R<br>Erro = C | The DS will<br>populate the<br>AReq with this<br>data element<br>prior to<br>passing to the<br>ACS.<br>Required in<br>the Error<br>Message if<br>available<br>(e.g., can be<br>obtained from<br>a message or<br>is being<br>generated). |

---

<a id="page-250"></a>

## PDF page 250

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DS URL<br>Field Name: dsURL | URL of the DS to which<br>the ACS will send the<br>RReq if a challenge<br>occurs.<br>The ACS is responsible for<br>storing this value for later<br>use in the transaction for<br>sending the RReq to the<br>DS. | DS | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Fully Qualified URL<br>Example:<br>• https://server.domainname.com | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required<br>between the<br>DS and the<br>ACS, but will<br>not be present<br>from the 3DS<br>Server to the<br>DS. |
| DS URL List<br>Field Name:<br>dsUrlList | List of DS URLs to which<br>the 3DS Server will send<br>the AReq message.<br>The DS optionally provides<br>this list in case there are<br>preferred DS URLs for<br>some countries. | DS | Size: Variable, 1–99 elements<br>JSON Data Type: Array of objects<br>Values accepted:<br>• See Table A.7 for DS URL List. | N/A | N/A | PRes = O |  |
| Electronic<br>Commerce Indicator<br>(ECI)<br>Field Name: eci | Payment System-specific<br>value provided by the ACS<br>or DS to indicate the<br>results of the attempt to<br>authenticate the<br>Cardholder. | ACS<br>DS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• Payment System-specific | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = C<br>RReq = C | The<br>requirements<br>for the<br>presence of<br>this field are<br>DS-specific. |
| Error Code<br>Field Name:<br>errorCode | Code indicating the type of<br>problem identified in the<br>message. |  | Length: 3 characters<br>JSON Data Type: String<br>Values accepted:<br>• See Table A.4 for values. | N/A | N/A | Erro = R |  |

---

<a id="page-251"></a>

## PDF page 251

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Error Component<br>Field Name:<br>errorComponent | Code indicating the 3-D<br>Secure component that<br>identified the error. |  | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• C = 3DS SDK<br>• S = 3DS Server<br>• D = DS<br>• A = ACS | N/A | N/A | Erro = R |  |
| Error Description<br>Field Name:<br>errorDescriptio<br>n | Text describing the<br>problem identified in the<br>message. |  | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String | N/A | N/A | Erro = R |  |
| Error Detail<br>Field Name:<br>errorDetail | Additional detail regarding<br>the problem identified in<br>the message. |  | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String | N/A | N/A | Erro = R |  |
| Error Message<br>Type<br>Field Name:<br>errorMessageTyp<br>e | Identifies the Message<br>Type that was identified as<br>erroneous. |  | Length: 4 characters<br>JSON Data Type: String<br>Values accepted:<br>• See Message Type | N/A | N/A | Erro = C | Conditional on<br>Message<br>Type being<br>recognisable. |

---

<a id="page-252"></a>

## PDF page 252

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EMV Payment<br>Token Indicator<br>Field Name:<br>payTokenInd | A value of True indicates<br>that the transaction was<br>detokenised prior to being<br>received by the ACS.<br>This data element will be<br>populated by the system<br>residing in the 3-D Secure<br>domain where the<br>detokenisation occurs (i.e.,<br>the 3DS Server or the DS).<br>Note: The Boolean value<br>of true is the only valid<br>response for this field<br>when it is present. | 3DS Server<br>DS | JSON Data Type: Boolean<br>Value accepted:<br>• true | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if<br>there is a<br>detokenisatio<br>n of an<br>Account<br>Number. |
| EMV Payment<br>Token Information<br>Field Name:<br>payTokenInfo | Information about<br>detokenised Payment<br>Token. | 3DS Server<br>DS | Length: Variable<br>JSON Data Type: Object<br>Values accepted:<br>• Refer to Table A.25 for data<br>elements to include.<br>Note: Data will be formatted into a<br>JSON object prior to being placed<br>into the EMV Payment Token field<br>of the message. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O |  |

---

<a id="page-253"></a>

## PDF page 253

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EMV Payment<br>Token Source<br>Field Name:<br>payTokenSource | This data element will be<br>populated by the system<br>residing in the 3-D Secure<br>domain where the<br>detokenisation occurs. | 3DS Server<br>DS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = 3DS Server<br>• 02 = DS<br>• 03–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if<br>EMV Payment<br>Token<br>Indicator =<br>true. |
| Expandable<br>Information Label<br>Field Name:<br>expandInfoLabel | Label displayed to the<br>Cardholder for the content<br>in Expandable Information<br>Text. | ACS | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | CRes = O |  |
| Expandable<br>Information Text<br>Field Name:<br>expandInfoText | Text provided by the<br>Issuer from the ACS to be<br>displayed to the<br>Cardholder for additional<br>information and the format<br>will be an expandable text<br>field. | ACS | Length: Variable, maximum 256<br>characters<br>JSON Data Type: String<br>Note: Carriage return is supported<br>in this data element and is<br>represented by an “\n”.<br>Note: Bold text is supported in this<br>data element and is enclosed<br>between **. For example “This is<br>**bold** text” is rendered as This is<br>bold text. | 01-APP | 01-PA<br>02-NPA | CRes = O |  |

---

<a id="page-254"></a>

## PDF page 254

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Information<br>Continuation<br>Indicator<br>Field Name:<br>infoContinueInd<br>icator | Indicator notifying the ACS<br>that the Cardholder<br>selected the Information<br>Continuation button in the<br>Information UI template.<br>Note: The Boolean value<br>of true is the only valid<br>response for this field<br>when it is present. | 3DS SDK | JSON Data Type: Boolean<br>Value accepted:<br>• true | 01-APP | 01-PA<br>02-NPA | CReq = C | Required for<br>ACS UI Type<br>= 07 if the<br>Cardholder<br>selects the<br>Information<br>Continuation<br>button on the<br>device. |
| Information<br>Continuation Label<br>Field Name:<br>infoContinueLab<br>el | UI label used for the button<br>that the Cardholder selects<br>in the Information UI<br>template. | ACS | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | CRes = C | See<br>Table A.20 for<br>presence<br>conditions. |

---

<a id="page-255"></a>

## PDF page 255

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Instalment Payment<br>Data<br>Field Name:<br>purchaseInstalD<br>ata | Indicates the maximum<br>number of authorisations<br>permitted for instalment<br>payments. | 3DS Server | Length: Variable, maximum 3<br>characters<br>JSON Data Type: String<br>Values accepted:<br>• Value shall be greater than 1<br>Example values accepted:<br>• 2<br>• 02<br>• 002 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | • Required if<br>the<br>Merchant<br>and the<br>Cardholder<br>have<br>agreed to<br>instalment<br>payments,<br>i.e., if 3DS<br>Requestor<br>Authenticati<br>on Indicator<br>= 03.<br>Omitted if<br>not an<br>instalment<br>payment<br>authenticati<br>on<br>• Required<br>for 03-3RI if<br>3RI<br>Indicator =<br>02. |

---

<a id="page-256"></a>

## PDF page 256

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Interaction Counter<br>Field Name:<br>interactionCoun<br>ter | Indicates the number of<br>authentication cycles<br>(excluding Decoupled<br>Authentication) attempted<br>by the Cardholder.<br>Value to be tracked by the<br>ACS. | ACS | Length: 2 characters<br>JSON Data Type: String | 01-APP<br>02-BRW | 01-PA<br>02-NPA | RReq = C | Required<br>unless ACS<br>Decoupled<br>Confirmation<br>Indicator = Y. |
| Issuer Image<br>Field Name:<br>issuerImage | Sent in the initial CRes<br>message from the ACS to<br>the 3DS SDK to provide<br>the URL(s) of the Issuer<br>logo or image to be used<br>in the Native UI. | ACS | Format: JSON object<br>Values accepted:<br>• Refer to Table A.21 for data<br>elements. | 01-APP | 01-PA<br>02-NPA | CRes = C | Presence of<br>this field is<br>Payment<br>System-<br>specific. |
| Merchant Category<br>Code<br>Field Name: mcc | DS-specific code<br>describing the Merchant’s<br>type of business, product<br>or service. | 3DS Server | Length: 4 characters<br>JSON Data Type: String<br>This value correlates to the<br>Merchant Category Code as<br>defined by each Payment System<br>or DS. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | 01-PA:<br>AReq = R<br>02-NPA:<br>AReq = O | Optional but<br>strongly<br>recommended<br>to include for<br>02-NPA if the<br>Merchant is<br>also the 3DS<br>Requestor. |

---

<a id="page-257"></a>

## PDF page 257

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Merchant Country<br>Code<br>Field Name:<br>merchantCountry<br>Code | Country Code of the<br>Merchant.<br>This value correlates to the<br>Merchant Country Code as<br>defined by each Payment<br>System or DS. | 3DS Server | Length: 3 characters<br>JSON Data Type: String<br>Values accepted:<br>• ISO 3166-1 numeric three-digit<br>country code, other than<br>exceptions listed in Table A.5.<br>Note: The same value must be<br>used in the authorisation request. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | 01-PA:<br>AReq = R<br>02-NPA:<br>AReq = O | Optional but<br>strongly<br>recommended<br>to include for<br>02-NPA if the<br>Merchant is<br>also the 3DS<br>Requestor. |
| Merchant Name<br>Field Name:<br>merchantName | Merchant name assigned<br>by the Acquirer or<br>Payment System. | 3DS Server | Length: Variable, maximum 40<br>characters<br>JSON Data Type: String<br>Same name used in the<br>authorisation message as defined<br>in ISO 8583-1. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | 01-PA:<br>AReq = R<br>02-NPA:<br>AReq = O | Optional but<br>strongly<br>recommended<br>to include for<br>02-NPA if the<br>Merchant is<br>also the 3DS<br>Requestor. |
| Merchant Risk<br>Indicator<br>Field Name:<br>merchantRiskInd<br>icator | Merchant’s assessment of<br>the level of fraud risk for<br>the specific authentication<br>for both the Cardholder<br>and the authentication<br>being conducted. | 3DS Server | Length: Variable<br>JSON Data Type: Object<br>Values accepted:<br>• Refer to Table A.11 for data<br>elements.<br>Note: Data will be formatted into a<br>JSON object prior to being placed<br>into the Merchant Risk Indicator<br>field of the message. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O | Optional, but<br>strongly<br>recommended<br>to include. |

---

<a id="page-258"></a>

## PDF page 258

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Message Category<br>Field Name:<br>messageCategory | Identifies the category of<br>the message for a specific<br>use case. | 3DS Server | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = PA<br>• 02 = NPA<br>• 03–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R<br>RReq = R |  |
| Message Extension<br>Field Name:<br>messageExtensio<br>n | Data necessary to support<br>requirements not<br>otherwise defined in the<br>3-D Secure message are<br>carried in a Message<br>Extension. | 3DS Server<br>3DS SDK<br>ACS<br>DS | Size: Variable, 1–15 elements<br>JSON Data Type: Array of objects<br>Values accepted:<br>• Refer to Table A.9 for data<br>elements. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C<br>ARes = C<br>CReq = C<br>CRes = C<br>OReq = C<br>ORes = C<br>PReq = C<br>PRes = C<br>RReq = C<br>RRes = C | Conditions to<br>be set by<br>each DS. |

---

<a id="page-259"></a>

## PDF page 259

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Message Type<br>Field Name:<br>messageType | Identifies the type of<br>message that is passed. | 3DS Server<br>3DS SDK<br>DS<br>ACS | Length: 4 characters<br>JSON Data Type: String<br>Values accepted:<br>• AReq<br>• ARes<br>• CReq<br>• CRes<br>• OReq<br>• ORes<br>• PReq<br>• PRes<br>• RReq<br>• RRes<br>• Erro | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R<br>ARes = R<br>CReq = R<br>CRes = R<br>OReq = R<br>ORes = R<br>PReq = R<br>PRes = R<br>RReq = R<br>RRes = R<br>Erro = R |  |

---

<a id="page-260"></a>

## PDF page 260

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Message Version<br>Number<br>Field Name:<br>messageVersion | Protocol Version identifier<br>This shall be the Protocol<br>Version Number of the<br>specification used by the<br>system creating this<br>message.<br>The Message Version<br>Number is set by the 3DS<br>Server which originates<br>the protocol with the AReq<br>message. The Message<br>Version Number does not<br>change during a 3DS<br>transaction. | 3DS Server | Length: Variable, 5–8 characters<br>JSON Data Type: String<br>Value accepted:<br>• Major.minor.patch<br>Example:<br>• 99.99.99<br>Refer to EMV Specification Bulletin<br>255. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R<br>ARes = R<br>CReq = R<br>CRes = R<br>OReq = R<br>ORes = R<br>PReq = R<br>PRes = R<br>RReq = R<br>RRes = R<br>Erro = R |  |
| Multi-Transaction<br>Field Name:<br>multiTransactio<br>n | Additional transaction<br>information in case of<br>multiple transactions or<br>Merchants. | 3DS Server | Length: Variable<br>JSON Data Type: Object<br>Values accepted:<br>• Refer to Table A.18 for data<br>elements to include. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O |  |

---

<a id="page-261"></a>

## PDF page 261

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Notification URL<br>Field Name:<br>notificationURL | Fully Qualified URL of the<br>system that receives the<br>CRes message or Error<br>Message. The CRes<br>message is posted by the<br>ACS through the<br>Cardholder Browser at the<br>end of the challenge and<br>receipt of the RRes<br>message. | 3DS Server | Length: Variable, maximum 256<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Fully Qualified URL | 02-BRW | 01-PA<br>02-NPA | AReq = R |  |
| OOB App Label<br>Field Name:<br>oobAppLabel | Label to be displayed for<br>the link to the OOB App<br>URL.<br>Example:<br>"oobAppLabel": "Open<br>Your Bank App" | ACS | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | CRes = C | Only present<br>for ACS UI<br>Type = 04 if:<br>• OOB App<br>URL<br>Indicator =<br>01 in the<br>CReq<br>message<br>AND<br>• the ACS<br>uses the<br>OOB<br>Authenticati<br>on App<br>automatic<br>switching<br>feature for<br>this<br>transaction |

---

<a id="page-262"></a>

## PDF page 262

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OOB App Status<br>Field Name:<br>oobAppStatus | Status code indicating the<br>type of problem<br>encountered when using<br>the OOB App URL. | 3DS SDK | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Open OOB App URL<br>failed<br>• 02–99 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo) | 01-APP | 01-PA<br>02-NPA | CReq = C | Required if<br>the<br>Cardholder<br>encountered<br>an error when<br>selecting the<br>OOB App<br>URL for ACS<br>UI Type = 04<br>or 06. |

---

<a id="page-263"></a>

## PDF page 263

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OOB App URL<br>Field Name:<br>oobAppURL | Universal App Link to an<br>Authentication App used in<br>the OOB authentication.<br>The OOB App URL will<br>open the appropriate<br>location within the OOB<br>Authentication App.<br>Refer to Table 1.3 for the<br>Universal App Link<br>definition. | ACS | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Universal App Link | 01-APP | 01-PA<br>02-NPA | CRes = C | Only present<br>for<br>[ ACS UI Type<br>= 04 if the<br>OOB App<br>Label is<br>present<br>OR<br>ACS UI Type<br>= 06 ]<br>AND if:<br>• OOB App<br>URL<br>Indicator =<br>01 in the<br>CReq<br>message;<br>AND<br>• the ACS<br>uses the<br>OOB<br>Authenticati<br>on App<br>automatic<br>switching<br>feature for<br>this<br>transaction |

---

<a id="page-264"></a>

## PDF page 264

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OOB App URL<br>Indicator<br>Field Name:<br>oobAppURLInd | Indicates if the 3DS SDK<br>supports the OOB App<br>URL. | 3DS SDK | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Supported<br>• 02 = Not supported by the<br>device<br>• 03 = Not supported by the 3DS<br>Requestor<br>• 04–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use<br>If SDK Type = 02 and Split-SDK<br>Type = 02, the OOB App URL<br>Indicator is set to 02.<br>Note: OOB App URL does not<br>work for the Split-SDK/Browser. | 01-APP | 01-PA<br>02-NPA | CReq = R |  |

---

<a id="page-265"></a>

## PDF page 265

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OOB Continuation<br>Indicator<br>Field Name:<br>oobContinue | Indicator notifying the ACS<br>that the Cardholder has<br>selected the OOB<br>Continuation button in an<br>OOB authentication<br>method, or that the 3DS<br>SDK automatically<br>completes without any<br>Cardholder interaction. | 3DS SDK | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Cardholder clicks the<br>button<br>• 02 = Automatic complete<br>• 03–99 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo) | 01-APP | 01-PA<br>02-NPA | CReq = C | Required if:<br>• ACS UI<br>Type = 04<br>unless<br>Challenge<br>Additional<br>Code is<br>present;<br>OR<br>• ACS UI<br>Type = 06 |
| OOB Continuation<br>Label<br>Field Name:<br>oobContinueLabe<br>l | Label to be used in the UI<br>for the button that the<br>Cardholder selects when<br>they have completed the<br>OOB authentication. | ACS | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | CRes = C | Required for<br>ACS UI Type<br>= 04 if the<br>OOB App<br>Label is not<br>present. |

---

<a id="page-266"></a>

## PDF page 266

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Operation Category<br>Field Name:<br>opCategory | Indicates the category/type<br>of information. | DS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = General<br>• 02 = Operational alert<br>• 03 = Public Key Certificate<br>expiry<br>• 04 = LOA/AOC expiry<br>• 05 = Fraud<br>• 06 = Other<br>• 07–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | N/A | N/A | OReq = R |  |
| Operation<br>Description<br>Field Name:<br>opDescription | Describes the reason for<br>the operational<br>communication or the<br>response to an action<br>taken by the recipient. | DS | Length: Variable, maximum 20000<br>characters<br>JSON Data Type: String | N/A | N/A | OReq = R |  |
| Operation<br>Expiration Date<br>Field Name:<br>opExpDate | The date after which the<br>relevance of the<br>operational information<br>(e.g., certificate expiration<br>dates, SLAs, etc.) expires. | DS | Length: 8 characters<br>JSON Data Type: String<br>Format accepted:<br>• YYYYMMDD | N/A | N/A | OReq = R |  |

---

<a id="page-267"></a>

## PDF page 267

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Operation Message<br>Status<br>Field Name:<br>opStatus | Indicates the status of the<br>Operation Request<br>message sequence from<br>the source of the OReq. | 3DS Server<br>ACS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Successfully received<br>messages<br>• 02 = Message sequence is<br>broken<br>• 03 = Requested action is not<br>supported or not executed by<br>the 3DS Server or ACS when<br>OReq message was received<br>• 04–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | N/A | N/A | ORes = R |  |

---

<a id="page-268"></a>

## PDF page 268

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Operation Prior<br>Transaction<br>Reference<br>Field Name:<br>opPriorTransRef | This data element provides<br>additional information<br>enabling the recipient to<br>reference a prior<br>transaction. | DS | JSON Data Type: Object<br>• transIdType: 2 characters<br>o 01 = 3DS Server<br>o 02 = DS<br>o 03 = ACS<br>• transId: 36 characters<br>o Canonical format as<br>defined in IETF RFC 4122.<br>May use any of the<br>specified versions as long<br>as the output meets<br>specified requirements.<br>For example, a prior DS<br>Transaction ID would be<br>represented as:<br>"opPriorTransRef":<br>{<br>"transIdType":"02",<br>"transId":"4317fdc3-ad24-<br>5443-8000-000000000891"<br>} | N/A | N/A | OReq = O |  |

---

<a id="page-269"></a>

## PDF page 269

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Operation<br>Sequence<br>Field Name: opSeq | Indicates the current and<br>total messages in an<br>OReq message sequence.<br>seqId: This element<br>uniquely identifies a<br>message sequence and<br>will remain constant in the<br>sequence of messages.<br>seqNum: This element<br>represents the current<br>message in the sequence.<br>seqTotal: This element<br>represents the total<br>number of messages in<br>the sequence and will<br>remain constant in the<br>sequence of messages. | DS | JSON Data Type: Object<br>• seqId: 36 characters<br>o Canonical format as<br>defined in IETF RFC 4122.<br>May use any of the<br>specified versions as long<br>as the output meets<br>specified requirements.<br>• seqNum: 2 characters<br>Values accepted:<br>o 01–99<br>• seqTotal: 2 characters<br>Values accepted<br>o 01–99<br>For example, the first of three<br>messages in an OReq sequence<br>would be represented as:<br>"opSeq":{<br>"seqId":"4317fdc3-ad24-<br>5443-8000-000000000891",<br>"seqNum":"01",<br>"seqTotal":"03"} | N/A | N/A | OReq = R |  |

---

<a id="page-270"></a>

## PDF page 270

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Operation Severity<br>Field Name:<br>opSeverity | Indicates the importance/<br>severity level of the<br>operational information.<br>Critical = Immediate action<br>to be taken by recipient<br>Major = Major impact;<br>Upcoming action to be<br>taken by recipient<br>Minor = Minor impact;<br>Upcoming action to be<br>taken by recipient<br>Informational =<br>Informational only, with no<br>immediate action by<br>recipient | DS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Critical<br>• 02 = Major<br>• 03 = Minor<br>• 04 = Informational<br>• 05–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | N/A | N/A | OReq = R |  |
| Payee Origin<br>Field Name:<br>payeeOrigin | The origin of the payee<br>that will be provided in the<br>SPC Transaction Data<br>Refer to Secure Payment<br>Confirmation. | 3DS Server | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Fully Qualified URL | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required if<br>3DS<br>Requestor<br>SPC Support<br>= Y |
| Payment System<br>Image<br>Field Name:<br>psImage | Sent in the initial CRes<br>message from the ACS to<br>the 3DS SDK to provide<br>the URL(s) of the DS or<br>Payment System logo or<br>image to be used in the<br>Native UI. | ACS | JSON Data Type: Object<br>Values accepted:<br>• Refer to Table A.22 for data<br>elements. | 01-APP | 01-PA<br>02-NPA | CRes = C | Presence of<br>this field is<br>Payment<br>System-<br>specific. |

---

<a id="page-271"></a>

## PDF page 271

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Purchase Amount<br>Field Name:<br>purchaseAmount | Purchase amount in minor<br>units of currency with all<br>punctuation removed.<br>When used in conjunction<br>with the Purchase<br>Currency Exponent field,<br>proper punctuation can be<br>calculated. | 3DS Server | Length: Variable, maximum 48<br>characters<br>JSON Data Type: String<br>Example:<br>Purchase amount is USD 123.45<br>Example values accepted:<br>• 12345<br>• 012345<br>• 0012345 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | 01-PA:<br>AReq = R<br>02-NPA:<br>AReq = C | • Required<br>for 02-NPA<br>if 3DS<br>Requestor<br>Authenticati<br>on Indicator<br>= 02, 03,<br>07, 08, 09<br>• Required<br>for 02-NPA<br>if 3RI<br>Indicator =<br>01, 02, 06,<br>07, 08, 09,<br>11, 15 |
| Purchase Currency<br>Field Name:<br>purchaseCurrenc<br>y | Currency in which<br>purchase amount is<br>expressed. | 3DS Server | Length: 3 characters; numeric<br>JSON Data Type: String<br>Values accepted:<br>• ISO 4217 three-digit currency<br>code, other than those listed in<br>Table A.5. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | 01-PA:<br>AReq = R<br>02-NPA:<br>AReq = C | • Required<br>for 02-NPA<br>if 3DS<br>Requestor<br>Authenticati<br>on Indicator<br>= 02, 03,<br>07, 08, 09<br>• Required<br>for 02-NPA<br>if 3RI<br>Indicator =<br>01, 02, 06,<br>07, 08, 09,<br>11, 15 |

---

<a id="page-272"></a>

## PDF page 272

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Purchase Currency<br>Exponent<br>Field Name:<br>purchaseExponen<br>t | Minor units of currency as<br>specified in the ISO 4217<br>currency exponent.<br>Example:<br>• USD = 2<br>• JPY = 0 | 3DS Server | Length: 1 character<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | 01-PA:<br>AReq = R<br>02-NPA:<br>AReq = C | • Required<br>for 02-NPA<br>if 3DS<br>Requestor<br>Authenticati<br>on Indicator<br>= 02, 03,<br>07, 08, 09<br>• Required<br>for 02-NPA<br>if 3RI<br>Indicator =<br>01, 02, 06,<br>07, 08, 09,<br>11, 15 |
| Purchase Date &<br>Time<br>Field Name:<br>purchaseDate | Date and time of the<br>authentication converted<br>into UTC. | 3DS Server | Length: 14 characters<br>JSON Data Type: String<br>Format accepted:<br>YYYYMMDDHHMMSS | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | 01-PA:<br>AReq = R<br>02-NPA:<br>AReq = C | • Required<br>for 02-NPA<br>if 3DS<br>Requestor<br>Authenticati<br>on Indicator<br>= 02, 03,<br>07, 08, 09<br>• Required<br>for 02-NPA<br>if 3RI<br>Indicator =<br>01, 02, 06,<br>07, 08, 09,<br>11, 15 |

---

<a id="page-273"></a>

## PDF page 273

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Read Order<br>Field Name:<br>readOrder | Indicates the order in<br>which to process the card<br>range records from the<br>PRes message. | DS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Direct order/FIFO (First In<br>First Out)<br>• 02 = Reverse order/LIFO (Last<br>In First Out<br>• 03–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | N/A | N/A | PRes = R |  |

---

<a id="page-274"></a>

## PDF page 274

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Recurring Amount<br>Field Name:<br>recurringAmount | Recurring amount in minor<br>units of currency with all<br>punctuation removed. | 3DS Server | Length: Variable, maximum 48<br>characters<br>JSON Data Type: String<br>Example:<br>• Purchase amount is USD<br>123.45<br>Example values accepted:<br>• 12345<br>• 012345<br>• 0012345 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if:<br>• [ 3DS<br>Requestor<br>Authenticat<br>ion<br>Indicator =<br>02 or 03;<br>OR<br>3RI<br>Indicator =<br>01 or 02 ]<br>AND<br>• Recurring<br>Indicator/<br>Amount<br>Indicator =<br>01 |
| Recurring Currency<br>Field Name:<br>recurringCurren<br>cy | Currency in which the<br>Recurring Amount is<br>expressed. | 3DS Server | Length: 3 characters; numeric<br>JSON Data Type: String<br>Values accepted:<br>• ISO 4217 three-digit currency<br>code, other than those listed in<br>Table A.5. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if<br>the Recurring<br>Amount is<br>present. |

---

<a id="page-275"></a>

## PDF page 275

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Recurring Currency<br>Exponent<br>Field Name:<br>recurringExpone<br>nt | Minor units of currency as<br>specified in the ISO 4217<br>currency exponent.<br>Examples:<br>• USD = 2<br>• JPY = 0 | 3DS Server | Length: 1 character; numeric<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if<br>the Recurring<br>Amount is<br>present. |
| Recurring Date<br>Field Name:<br>recurringDate | Effective date of the new<br>authorised amount<br>following the<br>first/promotional payment<br>in a recurring or instalment<br>transaction. | 3DS Server | Length: 8 characters<br>JSON Data Type: String<br>Date format accepted:<br>• YYYYMMDD | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if<br>Recurring<br>Indicator/<br>Frequency<br>Indicator = 01. |
| Recurring Expiry<br>Field Name:<br>recurringExpiry | Date after which no further<br>authorisations are<br>performed. | 3DS Server | Length: 8 characters<br>JSON Data Type: String<br>Date format accepted:<br>• YYYYMMDD | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if<br>there is an<br>end date. |

---

<a id="page-276"></a>

## PDF page 276

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Recurring<br>Frequency<br>Field Name:<br>recurringFreque<br>ncy | Indicates the minimum<br>number of days between<br>authorisations for a<br>recurring or instalment<br>transaction. | 3DS Server | Length: Variable, maximum 4<br>characters<br>JSON Data Type: String<br>Values accepted:<br>• Numeric values between 1 and<br>9999<br>Example values accepted:<br>• 31<br>• 031<br>• 0031 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if<br>Recurring<br>Indicator/<br>Frequency<br>Indicator =<br>01. |

---

<a id="page-277"></a>

## PDF page 277

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Recurring Indicator<br>Field Name:<br>recurringInd | Indicates whether the<br>recurring or instalment<br>payment has a fixed or<br>variable amount and<br>frequency.<br>The Recurring Indicator<br>object contains:<br>• the Amount Indicator<br>• the Frequency<br>Indicator<br>Example:<br>{"recurringInd":{<br>"amountInd":"01",<br>"frequencyInd":"02"}<br>} | 3DS Server | JSON Data Type: Object<br>Amount Indicator<br>Field Name: amountInd<br>Values accepted:<br>• 01 = Fixed Purchase Amount<br>• 02 = Variable Purchase<br>Amount<br>• 03–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use<br>Frequency Indicator<br>Field Name: frequencyInd<br>Values accepted:<br>• 01 = Fixed Frequency<br>• 02 = Variable or Unknown<br>Frequency<br>• 03–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Required if:<br>• 3DS<br>Requestor<br>Authenticati<br>on Indicator<br>= 02 or 03;<br>OR<br>• 3RI<br>Indicator =<br>01 or 02 |

---

<a id="page-278"></a>

## PDF page 278

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Resend Challenge<br>Information Code<br>Field Name:<br>resendChallenge | Indicator to the ACS that<br>the Cardholder selected<br>the Resend Information<br>button. | 3DS SDK | Length: 1 character<br>JSON Data Type: String<br>Value accepted:<br>• Y = Resend | 01-APP | 01-PA<br>02-NPA | CReq = C | Required if<br>the<br>Cardholder is<br>requesting the<br>ACS to<br>resend<br>challenge<br>information<br>(value = Y)<br>AND ACS UI<br>Type = 01. |
| Resend Information<br>Label<br>Field Name:<br>resendInformati<br>onLabel | Label to be used in the UI<br>for the button that the<br>Cardholder selects when<br>they would like to have the<br>authentication information<br>resent. | ACS | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | CRes = C | See<br>Table A.20 for<br>inclusion<br>conditions. |

---

<a id="page-279"></a>

## PDF page 279

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Results Message<br>Status<br>Field Name:<br>resultsStatus | Indicates the status of the<br>Results Request message<br>from the 3DS Server to<br>provide additional data to<br>the ACS.<br>This will indicate if the<br>message was successfully<br>received for further<br>processing or will be used<br>to provide more detail on<br>why the Challenge could<br>not be completed from the<br>3DS Client to the ACS. | 3DS Server | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = RReq received for further<br>processing<br>• 02 = CReq not sent to ACS by<br>3DS Requestor (3DS Server<br>or 3DS Requestor opted out of<br>the challenge)<br>• 03 = ARes (Transaction Status<br>= C or D) not delivered to the<br>3DS Requestor due to<br>technical error<br>• 04 = 3DS Server will process<br>Decoupled Authentication in a<br>subsequent authentication<br>• 05–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | RRes = R |  |

---

<a id="page-280"></a>

## PDF page 280

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SDK App ID<br>Field Name:<br>sdkAppID | Universally unique ID<br>created upon all<br>installations of the 3DS<br>Requestor App on a<br>Consumer Device. This<br>will be newly generated<br>and stored by the 3DS<br>SDK for each installation.<br>Note: In case of Split-<br>SDK/Browser, the SDK<br>App ID value is not<br>reliable, and may change<br>for each transaction. | 3DS SDK<br>(sent via<br>3DS<br>Server) | Length: 36 characters<br>JSON Data Type: String<br>Canonical format as defined in<br>IETF RFC 4122. This may use any<br>of the specified versions as long<br>as the output meets specified<br>requirements. | 01-APP | 01-PA<br>02-NPA | AReq = R |  |
| SDK Counter SDK<br>to ACS<br>Field Name:<br>sdkCounterStoA | Counter used as a security<br>measure in the 3DS SDK<br>to ACS secure channel.<br>Note: The counter is the<br>decimal value equivalent<br>of the byte, encoded as a<br>numeric string. | 3DS SDK | Length: 3 characters<br>JSON Data Type: String<br>Values accepted:<br>• 000–255 | 01-APP | 01-PA<br>02-NPA | CReq = R |  |
| SDK Encrypted<br>Data<br>Field Name:<br>sdkEncData | JWE Object (represented<br>as a string) as defined in<br>Section 6.2.2.1 containing<br>data encrypted by the 3DS<br>SDK for the DS to decrypt. | 3DS SDK<br>(sent via<br>3DS<br>Server) | Length: Variable, maximum 64000<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | AReq = C | Required from<br>the 3DS<br>Server to the<br>DS, but will<br>not be<br>present from<br>the DS to the<br>ACS. |

---

<a id="page-281"></a>

## PDF page 281

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SDK Ephemeral<br>Public Key (QC)<br>Field Name:<br>sdkEphemPubKey | Public key component of<br>the ephemeral key pair<br>generated by the 3DS<br>SDK and used to establish<br>session keys between the<br>3DS SDK and ACS.<br>In AReq, this data element<br>is present as its own<br>object.<br>In ARes, this data element<br>is contained within the<br>ACS Signed Content JWS<br>Object.<br>See Section 6.2.3.1 for<br>additional detail. | 3DS SDK | Length: Variable, maximum 256<br>characters<br>JSON Data Type: Object<br>JWK | 01-APP | 01-PA<br>02-NPA | AReq = R<br>ARes =<br>See ACS<br>Signed<br>Content. | For the ARes<br>message, see<br>ACS Signed<br>Content. |
| SDK Maximum<br>Timeout<br>Field Name:<br>sdkMaxTimeout | Indicates the maximum<br>amount of time (in<br>minutes) for all exchanges. | 3DS SDK | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• Greater than or = 05 | 01-APP | 01-PA<br>02-NPA | AReq = R |  |
| SDK Reference<br>Number<br>Field Name:<br>sdkReferenceNum<br>ber | Identifies the vendor and<br>version of the 3DS SDK<br>that is used for a specific<br>transaction. The value is<br>assigned by EMVCo when<br>the LOA of the specific<br>3DS SDK is issued. | 3DS SDK<br>(sent via<br>3DS<br>Server) | Length: Variable, maximum 32<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | AReq = R |  |

---

<a id="page-282"></a>

## PDF page 282

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SDK Server Signed<br>Content<br>Field Name:<br>sdkServerSigned<br>Content | Contains the JWS object<br>(represented as a string)<br>created by the Split-SDK<br>Server for the AReq<br>message.<br>See Section 6.2.2.3 for<br>details. | 3DS SDK | Length: Variable<br>JSON Data Type: String<br>Values accepted:<br>• The body of the JWS object<br>(represented as a string) will<br>contain the following data<br>elements as defined in<br>Table A.1:<br>o SDK Reference Number<br>o SDK Signature Timestamp<br>o SDK Transaction ID<br>o Split-SDK Server ID | 01-APP | 01-PA<br>02-NPA | AReq = C | Required if<br>SDK Type =<br>02. |
| SDK Signature<br>Timestamp<br>Field Name:<br>sdkSignatureTim<br>estamp | Date and time indicating<br>when the 3DS SDK<br>generated the Split-SDK<br>Server Signed Content<br>converted into UTC. | 3DS SDK | Length: 14 characters<br>JSON Data Type: String<br>Date format accepted:<br>YYYYMMDDHHMMSS | 01-APP | 01-PA<br>02-NPA | See SDK<br>Server<br>Signed<br>Content | See SDK<br>Server Signed<br>Content. |
| SDK Transaction ID<br>Field Name:<br>sdkTransID | Universally unique<br>transaction identifier<br>assigned by the 3DS SDK<br>to identify a single<br>transaction. | 3DS SDK<br>(sent via<br>3DS<br>Server) | Length: 36 characters<br>JSON Data Type: String<br>Canonical format as defined in<br>IETF RFC 4122. This may use any<br>of the specified versions if the<br>output meets specified<br>requirements. | 01-APP | 01-PA<br>02-NPA | AReq = R<br>ARes = R<br>CReq = R<br>CRes = R<br>RReq = R<br>RRes = R<br>Erro = C | Required in<br>the Error<br>Message if<br>available<br>(e.g., can be<br>obtained from<br>a message or<br>is being<br>generated). |

---

<a id="page-283"></a>

## PDF page 283

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SDK Type<br>Field Name:<br>sdkType | Indicates the type of 3DS<br>SDK.<br>This data element provides<br>additional information to<br>the DS and ACS to<br>determine the best<br>approach for handling the<br>transaction. | 3DS Server | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Default-SDK<br>• 02 = Split-SDK<br>• 03–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | 01-APP | 01-PA<br>02-NPA | AReq = R |  |
| Seller Information<br>Field Name:<br>sellerInfo | Additional transaction<br>information for<br>transactions where<br>Merchants submit<br>transaction details on<br>behalf of another entity,<br>i.e., individual sellers in a<br>marketplace or drivers in a<br>ridesharing platform. | 3DS Server | Size: Variable, 1–50 elements<br>JSON Data Type: Array of objects<br>Values accepted:<br>• Refer to Table A.19 for data<br>elements to include. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O |  |

---

<a id="page-284"></a>

## PDF page 284

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Serial Number<br>Field Name:<br>serialNum | If present in PReq<br>message, the DS returns<br>Card Range Data that has<br>been updated since the<br>time of the PRes message.<br>If absent, the DS returns<br>all card ranges.<br>If present in the PRes<br>message, indicates the<br>current state of the Card<br>Range Data (the specific<br>value is only meaningful to<br>the DS). The 3DS Server<br>should retain this value for<br>submission in a future<br>PReq message to request<br>only changes that have<br>been made to the Card<br>Range Data since the<br>PRes message was<br>generated.<br>Note: Serial Number is not<br>provided when the DS and<br>the 3DS Server select the<br>Card Range Data File<br>download option. | DS<br>3DS Server | Length: Variable, maximum 20<br>characters, alphanumeric<br>JSON Data Type: String | N/A | N/A | PReq = O<br>PRes = C | PRes: Absent<br>if the Card<br>Range Data<br>File URL is<br>present. |

---

<a id="page-285"></a>

## PDF page 285

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPC Incompletion<br>Indicator<br>Field Name:<br>spcIncompInd | Reason that the SPC<br>authentication was not<br>completed. | 3DS Server | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = SPC did not run or did<br>not successfully complete<br>• 02 = Cardholder cancelled the<br>SPC authentication<br>• 03 = SPC timed out<br>• 04–99 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo) | 02-BRW | 01-PA<br>02-NPA | AReq = C | Required if<br>the 3DS<br>Requestor<br>attempts to<br>invoke the<br>SPC API and<br>there is an<br>error. |
| SPC Transaction<br>Data<br>Field Name:<br>spcTransData | Information that the 3DS<br>Requestor passes in the<br>SPC API for display in the<br>Smart Modal Window | ACS<br>DS | JSON Data Type: Object<br>Values accepted:<br>• Refer to Table A.28 for data<br>elements.<br>Note: For NPA, Amount is set to 0<br>and Currency is set to any valid<br>value. | 02-BRW | 01-PA<br>02-NPA | ARes = C | Required if<br>Transaction<br>Status = S |

See SDK Server Signed Content.

Split-SDK Server ID

DS assigned Split-SDK Server identifier.

Split-SDK Server

Length: Variable, maximum 32 characters

01-APP 01-PA

See SDK Server Signed Content

Field Name: splitSdkServerI D

02-NPA

Each DS can provide a unique ID to each Split- SDK Server on an individual basis.

JSON Data Type: String

Value accepted:

- Any individual DS may impose specific formatting and character requirements on the contents of this field.

---

<a id="page-286"></a>

## PDF page 286

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Split-SDK Type<br>Field Name:<br>splitSdkType | Indicates the<br>characteristics of a Split-<br>SDK.<br>Split-SDK Variant:<br>Implementation<br>characteristics of the Split-<br>SDK client<br>Limited Split-SDK<br>Indicator: If the Split-SDK<br>client has limited<br>capabilities<br>Example:<br>"splitSdkType":{<br>"sdkVariant":"01",<br>"limitedInd":"Y"<br>} | 3DS Server | Length: Variable<br>JSON Data Type: Object<br>sdkVariant<br>Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Native Client<br>• 02 = Browser<br>• 03 = Shell<br>• 04–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use<br>limitedInd<br>Length: 1 character<br>JSON Data Type: String<br>Value accepted:<br>• Y = Limited<br>Only present if value = Y | 01-APP | 01-PA<br>02-NPA | AReq = C | Required if<br>SDK Type =<br>02 |

---

<a id="page-287"></a>

## PDF page 287

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Submit<br>Authentication<br>Label<br>Field Name:<br>submitAuthentic<br>ationLabel | Label to be used in the UI<br>for the button that the<br>Cardholder selects when<br>they have completed the<br>authentication.<br>Note: This data element is<br>not used for OOB<br>authentication. | ACS | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | CRes = C | Required if<br>ACS UI Type<br>= 01, 02, or<br>03. |
| Tax ID<br>Field Name: taxId | Cardholder’s tax<br>identification. | 3DS Server | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | Conditional<br>based on DS<br>rules. |
| Toggle Position<br>Indicator<br>Field Name:<br>togglePositionI<br>nd | Indicates if the Trust List<br>and/or Device Binding<br>prompt should be<br>presented below or above<br>the action buttons (Submit<br>Authentication, OOB App,<br>OOB Continuation,<br>Information Continuation,<br>Challenge Additional). | ACS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Above the buttons<br>Only present if value = 01<br>If the Toggle Position Indicator<br>is not present, the Trust List or<br>Device Binding are below the<br>action buttons.<br>• 02–99 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo) | 01-APP | 01-PA<br>02-NPA | CRes = O |  |

---

<a id="page-288"></a>

## PDF page 288

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Transaction<br>Challenge<br>Exemption<br>Field Name:<br>transChallengeE<br>xemption | Exemption applied by the<br>ACS to authenticate the<br>transaction without<br>requesting a challenge. | ACS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 05 = Transaction Risk Analysis<br>exemption<br>• 08 = Trust List exemption<br>• 10 = Low Value exemption<br>• 11 = Secure Corporate<br>Payments exemption<br>• 79 = No exemption applied<br>• 01–04, 06, 07, 09 and 12–78 =<br>Reserved for EMVCo future<br>use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = O |  |
| Transaction Status<br>Field Name:<br>transStatus | Indicates whether a<br>transaction qualifies as an<br>authenticated transaction<br>or account verification.<br>The Final CRes message<br>can only contain a value of<br>Y or N or D.<br>Transaction Status = C or<br>S is not allowed for Device<br>Channel = 3RI. | ACS<br>DS | Length: 1 character<br>JSON Data Type: String<br>• Y = Authentication Verification<br>Successful.<br>• N = Not Authenticated /<br>Account Not Verified;<br>Transaction denied.<br>• U = Authentication / Account<br>Verification Could Not Be<br>Performed; Technical or other<br>problem, as indicated in ARes<br>or RReq. | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | 01-PA:<br>ARes = R<br>RReq = R<br>Final CRes<br>= R<br>02-NPA:<br>ARes = C<br>RReq = C | For 01-PA,<br>see<br>Table A.17 for<br>Transaction<br>Status<br>presence<br>conditions.<br>For 02-NPA,<br>requirements<br>for the<br>presence and<br>values of<br>Transaction<br>Status are |

---

<a id="page-289"></a>

## PDF page 289

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | • A = Attempts Processing<br>Performed; Not Authenticated/<br>Verified, but a proof of<br>attempted<br>authentication/verification is<br>provided.<br>• C = Challenge Required;<br>Additional authentication is<br>required using the<br>CReq/CRes.<br>• D = Challenge Required;<br>Decoupled Authentication<br>confirmed.<br>• R = Authentication / Account<br>Verification Rejected; Issuer is<br>rejecting<br>authentication/verification and<br>request that authorisation not<br>be attempted.<br>• I = Informational Only; 3DS<br>Requestor challenge<br>preference acknowledged.<br>• S = Challenge using SPC |  |  | Final CRes<br>= C | DS-specific. |

Transaction Status Reason

Provides information on why the Transaction Status field has the specified value.

ACS

Length: 2 characters

01-APP

01-PA

ARes = C

For 01-PA, required if Transaction Status = N, U, or R.

DS

JSON Data Type: String

02-BRW

02-NPA

RReq = C

Field Name: transStatusReas on

Values accepted:

03-3RI

- 01 = Card authentication failed

For 02-NPA, requirements for the presence and

- 02 = Unknown device

- 03 = Unsupported device

---

<a id="page-290"></a>

## PDF page 290

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | • 04 = Exceeds authentication<br>frequency limit<br>• 05 = Expired card<br>• 06 = Invalid card number<br>• 07 = Invalid transaction<br>• 08 = No card record<br>• 09 = Security failure<br>• 10 = Stolen card<br>• 11 = Suspected fraud<br>• 12 = Transaction not permitted<br>to Cardholder<br>• 13 = Cardholder not enrolled<br>in service<br>• 14 = Transaction timed out at<br>the ACS<br>• 15 = Low confidence<br>• 16 = Medium confidence<br>• 17 = High confidence<br>• 18 = Very high confidence<br>• 19 = Exceeds ACS maximum<br>challenges<br>• 20 = Non-Payment transaction<br>not supported<br>• 21 = 3RI transaction not<br>supported<br>• 22 = ACS technical issue<br>• 23 = Decoupled Authentication<br>required by ACS but not |  |  |  | values of<br>Transaction<br>Status are<br>DS-specific. |

---

<a id="page-291"></a>

## PDF page 291

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | requested by 3DS Requestor<br>• 24 = 3DS Requestor<br>Decoupled Max Expiry Time<br>exceeded<br>• 25 = Decoupled Authentication<br>was provided insufficient time<br>to authenticate Cardholder.<br>ACS will not make attempt<br>• 26 = Authentication attempted<br>but not performed by the<br>Cardholder<br>• 27 = Preferred Authentication<br>Method not supported<br>• 28 = Validation of content<br>security policy failed<br>• 29 = Authentication attempted<br>but not completed by the<br>Cardholder. Fall back to<br>Decoupled Authentication<br>• 30 = Authentication completed<br>successfully but additional<br>authentication of the<br>Cardholder required.<br>Reinitiate as Decoupled<br>Authentication<br>• 31–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use |  |  |  |  |

---

<a id="page-292"></a>

## PDF page 292

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Transaction Status<br>Reason Information<br>Field Name:<br>transStatusReas<br>onInfo | Provides additional<br>information on the<br>Transaction Status<br>Reason. | ACS<br>DS | Length: Variable, maximum 256<br>characters<br>JSON Data Type: String | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = O<br>RReq = O |  |
| Transaction Type<br>Field Name:<br>transType | Identifies the type of<br>transaction being<br>authenticated. | 3DS Server | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Goods/ Service Purchase<br>• 03 = Check Acceptance<br>• 10 = Account Funding<br>• 11 = Quasi-Cash Transaction<br>• 28 = Prepaid Activation and<br>Load<br>Note: Values derived from ISO<br>8583-1. | 01-APP<br>02-BRW<br>03-3RI | 01-PA | AReq = C | This field is<br>required in<br>some markets<br>(e.g., for<br>Merchants in<br>Brazil).<br>Otherwise,<br>optional. |

---

<a id="page-293"></a>

## PDF page 293

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Trust List Data<br>Entry<br>Field Name:<br>trustListDataEn<br>try | Indicator provided by the<br>3DS SDK to the ACS to<br>confirm whether the<br>Cardholder gives consent<br>to Trust List. | 3DS SDK | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = Consent given to Trust List<br>• N = Consent not given to Trust<br>List<br>Note: If the Cardholder action<br>changes the default value, then<br>the value = Y. Otherwise the value<br>= N. | 01-APP | 01-PA<br>02-NPA | CReq = C | Required if<br>• Trust List<br>Information<br>Text was<br>present in<br>the<br>preceding<br>CRes<br>message<br>AND<br>• Challenge<br>Cancelation<br>Indicator is<br>not present |
| Trust List<br>Information Text<br>Field Name:<br>trustListInfoTe<br>xt | Text provided by the ACS<br>to the Cardholder during a<br>Trust List transaction.<br>Example:<br>• “Would you like to add<br>this Merchant to your<br>Trust List?” | ACS | Length: Variable, maximum 64<br>characters | 01-APP | 01-PA<br>02-NPA | CRes = O | See<br>Table A.20 for<br>presence<br>conditions. |

---

<a id="page-294"></a>

## PDF page 294

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Trust List Status<br>Field Name:<br>trustListStatus | Enables the<br>communication of trust list<br>status between the ACS,<br>the DS and the 3DS<br>Requestor. | 3DS Server<br>DS<br>ACS | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = 3DS Requestor is Trust<br>Listed by Cardholder<br>• N = 3DS Requestor is not<br>Trust Listed by Cardholder<br>• E = Not eligible as determined<br>by Issuer<br>• P = Pending confirmation by<br>Cardholder<br>• R = Cardholder rejected<br>• U = Trust List status unknown,<br>unavailable, or does not apply<br>Note: Valid values in the AReq<br>message are Y or N | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O<br>ARes = O<br>RReq = O |  |

Trust List Status Source

This data element will be populated by the system setting Trust List Status.

3DS Server

Length: 2 characters

01-APP

01-PA

AReq = C

Required if the Trust List Status is present.

DS

JSON Data Type: String

02-BRW

02-NPA

ARes = C

Field Name: trustListStatus Source

ACS

Values accepted:

03-3RI

RReq = C

- 01 = 3DS Server

- 02 = DS

- 03 = ACS

- 04–79 = Reserved for EMVCo future use (values invalid until defined by EMVCo)

- 80–99 = Reserved for DS use

---

<a id="page-295"></a>

## PDF page 295

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WebAuthn<br>Credential List<br>Field Name:<br>webAuthnCredLis<br>t | List of credential IDs<br>registered for the<br>Cardholder Account<br>Number. | ACS | Size: Variable, 1–10 elements<br>JSON Data Type: Array of objects<br>The object contains:<br>• Relying Party ID<br>Field Name:<br>rpID<br>Length: Variable, maximum<br>2048 characters<br>• WebAuthn Credential<br>Field Name:<br>credentialIds<br>Length: Variable, 16–1000<br>characters<br>Base64url-encoded | 02-BRW | 01-PA<br>02-NPA | ARes = C | Required if<br>Transaction<br>Status = S |
| Why Information<br>Label<br>Field Name:<br>whyInfoLabel | Label to be displayed to<br>the Cardholder for the<br>“why” information section. | ACS | Length: Variable, maximum 45<br>characters<br>JSON Data Type: String | 01-APP | 01-PA<br>02-NPA | CRes = O |  |

---

<a id="page-296"></a>

## PDF page 296

| Data Element/<br>Field Name | Description | Source | Length/Format/Values | Device<br>Channel | Message<br>Category | Message<br>Inclusion | Conditional<br>Inclusion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Why Information<br>Text<br>Field Name:<br>whyInfoText | Text provided by the<br>Issuer to be displayed to<br>the Cardholder to explain<br>why the Cardholder is<br>being asked to perform the<br>authentication task. | ACS | Length: Variable, maximum 256<br>characters<br>JSON Data Type: String<br>Note: Carriage return is supported<br>in this data element and is<br>represented by an “\n”.<br>Note: Bold text is supported in this<br>data element and is enclosed<br>between **. For example, “This is<br>**bold** text” is rendered as This is<br>bold text. | 01-APP | 01-PA<br>02-NPA | CRes = O |  |

The following sections provide additional details on the values for some data elements listed in Table A.1.

### A.5

### Device Information—01-APP Only

The Device Information is gathered by the 3DS SDK as defined in the EMV 3-D Secure SDK—Device Information specification. This data is placed into a JWE object that will encrypt the data using the DS public key.

### A.6

### Browser Information—02-BRW Only

Accurate Browser information is obtained in the AReq message for an ACS to determine the ability to support authentication on a particular Cardholder Browser for each transaction. The 3DS Server needs to accurately populate the Browser information for each transaction. This data can be obtained by 3DS software provided to the 3DS Requestor or through, for example, remote JavaScript calls. It is the responsibility of the 3DS Server to ensure that the data is not altered or hard-coded and that it is unique to each transaction. The specific fields captured from the Cardholder Browser for each transaction are:

---

<a id="page-297"></a>

## PDF page 297

- Browser Accept Headers

- Browser IP Address

- Browser Java Enabled

- Browser Language

- Browser Screen Color Depth

- Browser Screen Height

- Browser Screen Width

- Browser Time Zone

- Browser User-Agent

Refer to Table A.1 for data element specifications.

### A.7

### 3DS Method Data

The following table defines the data elements sent in the 3DS Method. The data is exchanged between the 3DS Requestor and the ACS via the Cardholder Browser. The HTTP field name is threeDSMethodData.

---

<a id="page-298"></a>

## PDF page 298

Table A.2:  3DS Method Data

| Data Element/Field Name | Description | Length/Format/Values | Recipient | Message<br>Category | Message<br>Inclusion |
| --- | --- | --- | --- | --- | --- |
| 3DS Method Notification URL<br>Field Name:<br>threeDSMethodNotification<br>URL | The URL that will receive the<br>notification of 3DS Method<br>completion from the ACS. This is<br>sent in the initial request to the<br>ACS from the 3DS Requestor<br>executing the 3DS Method. | Length: Variable, maximum 2048<br>characters<br>JSON Data Type: String<br>Value accepted:<br>• Fully Qualified URL | ACS | 01-PA<br>02-NPA | R |
| 3DS Server Transaction ID<br>Field Name:<br>threeDSServerTransID | A unique identifier for the<br>transaction that will be the same<br>as the 3DS Server Transaction ID<br>in the AReq message and will<br>have the same format as<br>specified in Table A.1.<br>This will be sent to the ACS in the<br>3DS Method HTTP POST and will<br>be returned in the POST to the<br>3DS Method Notification URL. | Refer to 3DS Server Transaction<br>ID in Table A.1. | ACS<br>3DS<br>Requestor | 01-PA<br>02-NPA | R |

---

<a id="page-299"></a>

## PDF page 299

3DS Method Data Examples

- Example 1: threeDSMethodData to be sent to ACS in the 3DS Method HTTP form POST from 3DS Requestor

<form name="frm" method="POST" action="Rendering URL">

<input type="hidden" name="threeDSMethodData" value="eyJ0aHJlZURTU2VydmVyVHJhbnNJRCI6IjNhYzdjYWE3LWFhNDItMjY2My03OTFiLTJhYzA1YTU0MmM0YSIsInRocmVlRFNNZX Rob2ROb3RpZmljYXRpb25VUkwiOiJ0aHJlZURTTWV0aG9kTm90aWZpY2F0aW9uVVJMIn0">

</form>

Decoded threeDSMethodData:

{"threeDSServerTransID":"3ac7caa7-aa42-2663-791b- 2ac05a542c4a","threeDSMethodNotificationURL":"threeDSMethodNotificationURL"}

- Example 2: threeDSMethodData to be sent to 3DS Method Notification URL from the ACS

<form name="frm" method="POST" action="threeDSMethodNotificationURL">

<input type="hidden" name="threeDSMethodData" value="eyJ0aHJlZURTU2VydmVyVHJhbnNJRCI6IjNhYzdjYWE3LWFhNDItMjY2My03OTFiLTJhYzA1YTU0MmM0YSJ9">

</form>

Decoded threeDSMethodData:

{"threeDSServerTransID":"3ac7caa7-aa42-2663-791b-2ac05a542c4a"}

### A.8

### Browser CReq and CRes POST

The following table defines the data elements sent in the Browser POST to the ACS for the CReq flow, and to the Notification URL in the CRes flow. An HTML form is used within the Cardholder Browser and the data is redirected via the Cardholder Browser in an HTTP POST.

---

<a id="page-300"></a>

## PDF page 300

Note:  The end result of the redirection must be similar as if an HTML tag was used.

Table A.3:  3DS CReq/CRes POST Data

| Data Element /<br>Field Name | Description | Recipient | Length/Format/Values | Message<br>Inclusion |
| --- | --- | --- | --- | --- |
| 3DS Requestor Session<br>Data<br>Field Name:<br>threeDSSessionData | The 3DS Requestor may provide the 3DS Requestor<br>Session Data with the CReq message to the ACS. The 3DS<br>Requestor Session Data is optionally used to accommodate<br>the different methods that 3DS Requestor systems use to<br>handle session information.<br>The ACS returns the 3DS Requestor Session Data with the<br>CRes message POST to the 3DS Requestor. If the 3DS<br>Requestor system can associate the final post with the<br>original session without further assistance, the 3DS<br>Requestor Session Data field may be missing.<br>If the 3DS Requestor system does not maintain a session<br>for a given authentication session, the 3DS Requestor<br>Session Data field can carry any data the 3DS Requestor<br>needs to continue the session.<br>Because the content of this field varies by 3DS Requestor<br>implementation, the ACS preserves the content unchanged<br>and without assumptions.<br>If provided by the 3DS Requestor, the Session Data must<br>be returned by the ACS. | ACS<br>3DS Requestor | Length: Variable,<br>maximum 1024<br>characters<br>Format: Alphanumeric<br>Base64url-encoded<br>The size of the field (after<br>Base64url-encoding, if<br>applicable) is limited to<br>1024 bytes. | • O in HTML<br>form with the<br>CReq<br>message<br>• R in HTML<br>form with the<br>CRes<br>message if<br>received<br>with the<br>CReq<br>message |
| CReq<br>Field Name: creq | The entire CReq message, as defined in Table B.3, that<br>has been Base64url-encoded. | ACS | Length: Variable,<br>Base64url-encoded | R |
| CRes<br>Field Name: cres | The entire CRes message, as defined in Table B.4, that<br>has been Base64url-encoded. | 3DS Requestor |  | R |

---

<a id="page-301"></a>

## PDF page 301

Browser CReq–CRes Data Examples

- Example 1: threeDSSessionData sent by the 3DS Requestor in the CReq message to the ACS

3DS Requestor Session Data from the 3DS Requestor = "merchant.com-ID-adac2434-df78-4bfa-bcd9- 11ca4ccd5dca"

3DS Requestor Session Data base64URL encoded = "bWVyY2hhbnQuY29tLUlELWFkYWMyNDM0LWRmNzgtNGJmYS1iY2Q5LTExY2E0Y2NkNWRjYQ"

CReq message

{

"threeDSServerTransID":"8a880dc0-d2d2-4067-bcb1-b08d1690b26e",

"acsTransID":"d7c1ee99-9478-44a6-b1f2-391e29c6b340",

"threeDSRequestorURL":"https://merchant.com/url",

"messageType":"CReq",

"messageVersion":"2.3.1"

}

CReq message base64URL encoded

"eyJ0aHJlZURTU2VydmVyVHJhbnNJRCI6IjhhODgwZGMwLWQyZDItNDA2Ny1iY2IxLWIwOGQxNjkwYjI2ZSIsCSJhY3NUcmFuc0lEIjoi ZDdjMWVlOTktOTQ3OC00NGE2LWIxZjItMzkxZTI5YzZiMzQwIiwidGhyZWVEU1JlcXVlc3RvclVybCI6Imh0dHBzOi8vbWVyY2hhbnQuY 29tL3VybCIsIm1lc3NhZ2VUeXBlIjoiQ1JlcSIsIm1lc3NhZ2VWZXJzaW9uIjoiMi4zLjAifQ"

HTML form

"htmlCreq": "<form action=\'https://acs.com.creq\' method=\'post\'>

<input type=\'hidden\' name=\'creq\' value=\ 'eyJ0aHJlZURTU2VydmVyVHJhbnNJRCI6IjhhODgwZGMwLWQyZDItNDA2Ny1iY2IxLWIwOGQxNjkwYjI2ZSIsCSJhY3NUcmFuc0lEIjoi ZDdjMWVlOTktOTQ3OC00NGE2LWIxZjItMzkxZTI5YzZiMzQwIiwidGhyZWVEU1JlcXVlc3RvclVybCI6Imh0dHBzOi8vbWVyY2hhbnQuY 29tL3VybCIsIm1lc3NhZ2VUeXBlIjoiQ1JlcSIsIm1lc3NhZ2VWZXJzaW9uIjoiMi4zLjAifQ' />

---

<a id="page-302"></a>

## PDF page 302

<input type=\'hidden\' name=\'threeDSSessionData\' value=\'b\' bWVyY2hhbnQuY29tLUlELWFkYWMyNDM0LWRmNzgtNGJmYS1iY2Q5LTExY2E0Y2NkNWRjYQ'\' /></form>"

- Example 2: threeDSSessionData sent by the ACS in the CRes message to the 3DS Requestor

Base64url decoded 3DS Requestor Session Data: "merchant.com-ID-adac2434-df78-4bfa-bcd9-11ca4ccd5dca"

CRes message

{

"threeDSServerTransID":"8a880dc0-d2d2-4067-bcb1-b08d1690b26e",

"acsTransID":"d7c1ee99-9478-44a6-b1f2-391e29c6b340",

"transStatus":"Y",

"messageType":"CRes",

"messageVersion":"2.3.1

}

Base64 URL encoded CRes message

"eyJ0aHJlZURTU2VydmVyVHJhbnNJRCI6IjhhODgwZGMwLWQyZDItNDA2Ny1iY2IxLWIwOGQxNjkwYjI2ZSIsImFjc1RyYW5zSUQiOiJk N2MxZWU5OS05NDc4LTQ0YTYtYjFmMi0zOTFlMjljNmIzNDAiLCJ0cmFuc1N0YXR1cyI6IlkiLCJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZ XNzYWdlVmVyc2lvbiI6IjIuMy4wIix9"

3DS Requestor Session Data base64URL encoded = "bWVyY2hhbnQuY29tLUlELWFkYWMyNDM0LWRmNzgtNGJmYS1iY2Q5LTExY2E0Y2NkNWRjYQ"

HTML form

"htmlCres": "<form action=\'https://3dss.com.cres\' method=\'post\'>

---

<a id="page-303"></a>

## PDF page 303

<input type=\'hidden\' name=\'cres\' value=\'eyJ0aHJlZURTU2VydmVyVHJhbnNJRCI6IjhhODgwZGMwLWQyZDItNDA2Ny1iY2IxLWIwOGQxNjkwYjI2ZSIsImFjc1RyYW5zS UQiOiJkN2MxZWU5OS05NDc4LTQ0YTYtYjFmMi0zOTFlMjljNmIzNDAiLCJ0cmFuc1N0YXR1cyI6IlkiLCJtZXNzYWdlVHlwZSI6IkNSZX MiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMy4wIix9'/>

<input type=\'hidden\' name=\'threeDSSessionData\' value=\'b\' bWVyY2hhbnQuY29tLUlELWFkYWMyNDM0LWRmNzgtNGJmYS1iY2Q5LTExY2E0Y2NkNWRjYQ'\' /></form>"

### A.9

### Error Code, Error Description, and Error Detail

Error Messages are used to determine how to formulate a response when a system receives a message that cannot be processed, or when the error is required as part of receiving a response message from another system. For example, a 3DS Server receives an ARes message from a DS that contains an error, and the 3DS Server responds with an Error Message to the DS using the 3DS Server Transaction ID of the transaction that had an error. The following table identifies the Error Code values and specifies the associated content for Error Description and Error Detail. The information provided in the Error Description and Error Detail are guidelines on the expected content. In Error Detail if there is a mention of listing required elements, the expectation is that those data elements will be listed appropriately.

---

<a id="page-304"></a>

## PDF page 304

Table A.4:  Error Code, Error Description, and Error Detail

| Value | Error Code | Error Description | Error Detail |
| --- | --- | --- | --- |
| 101 | Message Received Invalid | One of the following:<br>• Message is not AReq, ARes, CReq, CRes,<br>PReq, PRes, OReq, ORes, RReq, or RRes.<br>• Valid Message Type is sent to or from an<br>inappropriate component (such as AReq<br>message being sent to the 3DS Server).<br>• Message not recognised. | One of the following:<br>• Invalid Message Type<br>• Invalid Message for the receiving<br>component<br>• Invalid Formatted Message |
| 102 | Message Version Number Not<br>Supported | One of the following:<br>• Message Version Number received is not valid<br>for the receiving component.<br>• Error in the Message Version Number in the<br>Card Range Data.<br>• Message Version Number provided for a<br>Payment Token is not supported by the actual<br>PAN when detokenised. | • Message Version Number in the Card<br>Range Data is not active.<br>• Message Version Number received is not<br>supported by the receiving component.<br>Note: All supported Protocol Version Numbers<br>are provided in a comma-delimited list. |
| 103 | Sent Messages Limit Exceeded | Exceeded maximum number of PReq messages<br>sent to the DS. | For example, the 3DS Server sends two PReq<br>messages to the DS within one hour. |
| 201 | Required Data Element Missing | A message element required as defined in<br>Table A.1 is missing from the message. | Name of required element(s) that was omitted; if<br>more than one element is detected, this is a<br>comma-delimited list.<br>Parent Example:<br>messageType<br>Parent/Child Example:<br>acctInfo.chAccAgeInd |

---

<a id="page-305"></a>

## PDF page 305

| Value | Error Code | Error Description | Error Detail |
| --- | --- | --- | --- |
| 202 | Critical Message Extension Not<br>Recognised | Critical message extension not recognised. | ID of critical Message Extension(s) that was not<br>recognised; if more than one extension is<br>detected, this is a comma-delimited list of<br>message identifiers that were not recognised. |
| 203 | Format or value of one or more<br>Data Elements is Invalid<br>according to the Specification | • Data element not in the required format or value<br>is invalid as defined in Table A.1, or<br>• Message Version Number does not match the<br>value set by the 3DS Server in the AReq<br>message, or<br>• Data element is present in a message where<br>the conditional inclusion does not apply, or<br>• UTC date and time data element is not using<br>UTC. | Name of invalid element(s); if more than one<br>invalid data element is detected, this is a<br>comma-delimited list. |
| 204 | Duplicate Data Element | Valid data element presents more than once in the<br>message. | Name of duplicated data element; if more than<br>one duplicate data element is detected, this is a<br>comma-delimited list. |
| 205 | Card Range Overlap | Overlap in the card ranges provided by the DS in<br>the PRes message.<br>For example, the two card ranges 11000–15000 and<br>13000–17000 overlap from 13000–15000. | List of Card Ranges that overlap. |
| 206 | Card Range Action Indicator | Action is not possible for the card range.<br>For example, Delete or Modify a card range that<br>does not exist, or Add an already existing card<br>range. | List the Card Range and Action Indicator that is<br>causing the error. |
| 207 | Value in the Reserved Value<br>range | Data Element value is in the range of “Reserved for<br>DS use” or “Reserved for EMVCo future use” and is<br>not recognised. | Name of invalid element(s); if more than one<br>invalid data element is detected, this is a<br>comma-delimited list. |

---

<a id="page-306"></a>

## PDF page 306

| Value | Error Code | Error Description | Error Detail |
| --- | --- | --- | --- |
| 301 | Transaction ID Not Recognised | Transaction ID received is not valid for the receiving<br>component. | The Transaction ID received was invalid.<br>Invalid meaning Transaction ID not recognised. |
| 302 | Data Decryption Failure | Data could not be decrypted by the receiving system<br>due to technical or other reason. | Description of the failure. |
| 303 | Access Denied, Invalid Endpoint | Access denied, invalid endpoint. | Description of the failure. |
| 304 | ISO Code Invalid | ISO code not valid per ISO tables (for either country<br>or currency), or code is one of the excluded values<br>listed in Table A.5. | Name of invalid element(s); if more than one<br>invalid element is detected, this is a comma-<br>delimited list.<br>If Challenge Request.Purchase.currency and<br>Challenge Request.Purchase.exponent form an<br>invalid pair, list both as Error Description. |
| 305 | Transaction Data Not Valid | If in response to an AReq message:<br>• Cardholder Account Number is not in a range<br>belonging to Issuer<br>If in response to a CReq, and a CReq message was<br>incorrectly sent:<br>• CReq message was received by the wrong<br>ACS, OR<br>• CReq message was not sent, based on the<br>values in the ARes message | Name of element(s) that caused the ACS to<br>decide that the AReq message or CReq<br>message was incorrectly sent; if more than one<br>invalid element is detected this is a comma-<br>delimited list. |
| 306 | Merchant Category Code (MCC)<br>Not Valid for Payment System | Merchant Category Code (MCC) not valid for<br>Payment System. | For example, invalid MCC received in the AReq<br>message. |
| 307 | Serial Number Not Valid | Serial Number not valid. | For example, invalid Serial Number in the<br>PReq/PRes message (e.g., too old, not found). |

---

<a id="page-307"></a>

## PDF page 307

| Value | Error Code | Error Description | Error Detail |
| --- | --- | --- | --- |
| 308 | Signature Verification Failure | SDK Server Signed Content could not be verified. | Description of the failure. |
| 309 | Validation against content<br>security policies Failure | Validation against content security policies failed. | For example, which element prevented<br>successful validation. |
| 310 | Incorrect Cryptographic<br>Algorithm | The use of a specific cryptographic algorithm is not<br>allowed in the specific context. | For example, which cryptographic algorithm was<br>expected. |
| 311 | Incorrect kid | The DS detects an error for the key identifier (kid)<br>present in the SDK Encrypted Data. | For example:<br>• The provided kid is not recognised<br>• The kid is not present |
| 312 | Duplicate message | A message with the same Transaction ID was<br>already received. | The Transaction ID is recognised as a duplicate.<br>For example, the DS receives multiple RReq<br>messages with the same Transaction ID. |
| 313 | Inconsistent RReq message | An RReq message is received although there was<br>no challenge (Transaction Status not equal to C or<br>D or S) for this transaction. | The ACS sends an RReq message but the<br>Transaction Status in the corresponding ARes<br>message was not = C or D or S. |
| 314 | Multiple CReq messages not<br>supported | During a challenge for the Browser flow, the ACS<br>does not accept multiple CReq messages. | The Cardholder requests a Browser page<br>refresh during a challenge, the 3DS Server<br>sends a second CReq message to the ACS. |
| 315 | CReq message received after<br>the RReq message | During a challenge for the Browser flow, the ACS<br>receives a CReq message, after having sent the<br>RReq message. | The Cardholder requests a Browser page<br>refresh during a challenge after the ACS has<br>sent the RReq message to complete the<br>transaction. |
| 402 | Transaction Timed Out | Transaction timed out. | For example, timeout expiry reached for the<br>transaction as defined in Section 5.5. |

---

<a id="page-308"></a>

## PDF page 308

| Value | Error Code | Error Description | Error Detail |
| --- | --- | --- | --- |
| 403 | Transient System Failure | Transient system failure. | For example, a slowly processing back-end<br>system. |
| 404 | Permanent System Failure | Permanent system failure. | For example, a critical database cannot be<br>accessed. |
| 405 | System Connection Failure | System connection failure. | For example, the sending component is unable<br>to establish a connection to the receiving<br>component. |

---

<a id="page-309"></a>

## PDF page 309

### A.10 Excluded ISO Currency and Country Code Values

The following table lists exclusions from the ISO values for Currency Code (ISO 4217) and Country Code (ISO 3166).

Table A.5:  Excluded Currency Code and Country Code Values

| ISO Code | Numeric value<br>not permitted<br>for 3-D Secure | Alphabetic value<br>not permitted<br>for 3-D Secure | Definition |
| --- | --- | --- | --- |
| ISO 4217 | 955 | XBA | European Composite Unit |
| ISO 4217 | 956 | XBB | European Monetary Unit |
| ISO 4217 | 957 | XBC | European Unit of Account 9 |
| ISO 4217 | 958 | XBD | European Unit of Account 17 |
| ISO 4217 | 959 | XAU | Gold |
| ISO 4217 | 960 | XDR | I.M.F. |
| ISO 4217 | 961 | XAG | Silver |
| ISO 4217 | 962 | XPT | Platinum |
| ISO 4217 | 963 | XTS | Reserved for testing |
| ISO 4217 | 964 | XPD | Palladium |
| ISO 4217 | 999 | XXX | No currency is involved |

ISO 3166-1 901–999 Reserved by ISO to designate country names not otherwise defined

---

<a id="page-310"></a>

## PDF page 310

### A.11 Card Range Data

The Card Range Data data element contains information returned in a PRes message to the 3DS Server from the specific DS that indicates the most recent EMV 3-D Secure versions supported by the ACS that hosts that card range. Card Range Data may optionally also contain the ACS URL for the 3DS Method if supported by the ACS Protocol Version and the DS Protocol Version list which support that card range. The detailed data elements are outlined in Table A.6. Note:  The Card Range Data is an array containing as many JSON objects as there are stored card ranges in the DS being called.

Table A.6:  Card Range Data

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Ranges<br>Field Name: ranges | The Ranges array contains the Start Range and End<br>Range. It contains one or more card ranges.<br>Refer to the following elements:<br>• Start Range<br>• End Range | Size: Variable, 1–5000 elements<br>JSON Data Type: Array of objects | R |
| Start Range<br>Field Name: start | Start of the card range. | Length: 13–19 characters<br>JSON Data Type: String | R |

---

<a id="page-311"></a>

## PDF page 311

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| End Range<br>Field Name: end | End of the card range. | Length: 13–19 characters<br>JSON Data Type: String | R |
| Action Indicator<br>Field Name: actionInd | Indicates the action to take with the card range.<br>Note: M (Modify the Card Range Data) is used only to<br>modify or update data associated with the card ranges,<br>not to modify the Start Range and End Range. | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• A = Add the card range to the cache<br>(default value)<br>• D = Delete the card range from the cache<br>• M = Modify the Card Range Data | O |
| Issuer Country Code<br>Field Name: issuerCountryCode | Specifies the Issuer country for the Ranges. | Length: 3 characters<br>JSON Data Type: String<br>Values accepted:<br>• ISO 3166-1 numeric three-digit country<br>code, other than exceptions listed in Table<br>A.5. | O |
| DS Protocol Versions<br>Field Name:<br>dsProtocolVersions | Contains the list of active Protocol Versions supported<br>by the DS. If the DS Protocol Version is present in the<br>Card Range Data data element, it overrides the DS<br>Protocol Versions in the PRes message. | Size: Variable, 1–10 elements<br>JSON Data Type: Array of string<br>String: 5–8 characters<br>Values accepted:<br>• Refer to EMV Specification Bulletin 255 | O |

---

<a id="page-312"></a>

## PDF page 312

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| ACS Protocol Versions<br>Field Name:<br>acsProtocolVersions | Array of objects containing the list of Protocol Versions<br>supported by the ACS for the card range, with their<br>associated ACS Information Indicator, the 3DS Method<br>URL and the list of Supported Message Extension.<br>• Version<br>• ACS Information Indicator<br>• 3DS Method URL<br>• Supported Message Extension | Size: Variable, 1–10 elements<br>JSON Data Type: Array of objects<br>Values accepted:<br>• Refer to the data elements:<br>o Version<br>o ACS Information Indicator<br>o 3DS Method URL<br>o Supported Message Extension | R |
| Version<br>Field Name: version | The Protocol Version supported by the ACS for the<br>card range. | Length: 5–8 characters<br>JSON Data Type: String<br>Values accepted:<br>• Refer to EMV Specification Bulletin 255 | R |

---

<a id="page-313"></a>

## PDF page 313

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| ACS Information Indicator<br>Field Name: acsInfoInd | Provides additional information for a particular Protocol<br>Version to the 3DS Server. The element lists all<br>applicable values for the card range.<br>Example:<br>{<br>"acsInfoInd":["01","02","03","04",<br>"05","06","07"]<br>} | Size: Variable, 1–99 elements<br>JSON Data Type: Array of string<br>String: 2 characters<br>Values accepted:<br>• 01 = Authentication Available at ACS<br>• 02 = Attempts Supported by ACS or DS<br>• 03 = Decoupled Authentication Supported<br>• 04 = Trust List Supported<br>• 05 = Device Binding Supported<br>• 06 = WebAuthn Authentication Supported<br>• 07 = SPC Authentication Supported<br>• 08 = Transaction Risk Analysis Exemption<br>Supported<br>• 09 = Trust List Exemption Supported<br>• 10 = Low Value Exemption Supported<br>• 11 = Secure Corporate Payments<br>Exemption Supported<br>• 12–79 = Reserved for EMVCo future use<br>(values invalid until defined by EMVCo)<br>• 80–99 = Reserved for DS use | O |
| 3DS Method URL<br>Field Name:<br>threeDSMethodURL | The ACS URL that will be used by the 3DS Method for<br>a particular Protocol Version.<br>Note: The 3DSMethodURL data element may be<br>omitted if not supported by the ACS for this specific<br>card range. | Length: Variable, maximum 2048 characters<br>JSON Data Type: String<br>Value accepted:<br>• Fully Qualified URL | O |

---

<a id="page-314"></a>

## PDF page 314

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Supported Message<br>Extension<br>Field Name:<br>supportedMsgExt | List of message extensions supported by the ACS that<br>contains the Assigned Extension Group Identifier and<br>the Extension Version Number. | Size: Variable, 1–15 elements<br>JSON Data Type: Array of objects<br>Value accepted:<br>• Refer to Table A.8<br>o Assigned Extension Group Identifier<br>o Extension Version Number | C<br>Present if<br>not empty |

Card Range Data Example

{"cardRangeData": [

{"ranges": [

{"start": "1000000000000000",

"end": "1000000000005000"},

{"start": "1000000000006000",

"end": "1000000000007000"}

],

"actionInd": "A",

"issuerCountryCode": "356",

"dsProtocolVersions": ["2.2.0", "2.3.1"],

"acsProtocolVersions": [

{"version": "2.2.0",

"acsInfoInd": ["01", "02"],

"threeDSMethodURL": "https://www.acs.com/script1",

---

<a id="page-315"></a>

## PDF page 315

"supportedMsgExt": [

{"id": "A000000802-001","version": "2.0"},

{"id": "A000000802-004","version": "1.0"}

]},

{"version": "2.3.1",

"acsInfoInd": ["01", "02", "03", "04", "81"],

"threeDSMethodURL": "https://www.acs.com/script3"

}

]

}

]

}

The DS URL List data element contains information returned in a PRes message to the 3DS Server from the specific DS that contains the list of URLs that the 3DS Server can use to communicate with a DS. The 3DS Server replaces the previous DS URL List with the latest received in the PRes message. If the DS URL List is absent from the PRes message, the 3DS Server deletes all existing DS URLs. Its JSON Data Type: Array of objects contains:

- the 3DS Server to DS URL

- the DS Country Code (optional)

The detailed data elements are outlined in Table A.7.

---

<a id="page-316"></a>

## PDF page 316

Table A.7:  DS URL List

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| 3DS Server to DS URL<br>Field Name:<br>threeDSServerToDsUrl | URL that the 3DS Server uses to communicate with a<br>DS for a particular card range.<br>If the DS Country Code is absent, the 3DS Server can<br>use this URL for all card ranges. | Length: Variable, maximum 2048 characters<br>JSON Data Type: String<br>Value accepted:<br>• Fully Qualified URL | R |
| DS Country Code<br>Field Name: dsCountryCode | Specifies the country for which the 3DS Server to DS<br>URL can be used.<br>For a Card Range Data, if the Issuer Country Code<br>matches the DS Country Code, the 3DS Server uses<br>this 3DS Server to DS URL to communicate with the<br>DS. If there is no match, the 3DS Server uses the<br>default 3DS Server to DS URL. | Length: 3 characters<br>JSON Data Type: String<br>Value accepted:<br>• ISO 3166-1 numeric three-digit country<br>code, other than exceptions listed in Table<br>A.5. | O |

DS URL List Data Example

{"dsUrlList": [ {"dsCountryCode": "356", "threeDSServerToDsUrl": "https://www.india-ds.com/3ds/"}, {"threeDSServerToDsUrl": "https://www.ds.com/3ds/"} ] }

---

<a id="page-317"></a>

## PDF page 317

### A.11.1 Supported Message Extension Data Element

The Supported Message Extension data element contains information about the message extension and message extension version that a specific ACS supports. Its JSON Data Type: Array of objects contains:

- the Assigned Extension Group Identifier

- the Extension Version Number

The detailed data elements are outlined in Table A.8.

Table A.8:  Supported Message Extension

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Assigned Extension Group<br>Identifier<br>Field Name: id | A unique identifier for the extension. | Length: 14 characters<br>JSON Data Type: String<br>Value accepted:<br>• Refer to EMV Specification Bulletin 255 | R |
| Extension Version Number<br>Field Name: version | Version number of the message extension. | Length: 3 characters<br>JSON Data Type: String<br>Value accepted:<br>• Refer to the Extension Version Number in<br>the message extension with the<br>corresponding Assigned Extension Group<br>Identifier | R |

---

<a id="page-318"></a>

## PDF page 318

Supported Message Extension Data Example

{"supportedMsgExt": [ {"id": "A000000802-001","version": "2.0"}, {"id": "A000000802-004","version": "1.0"} ]}

---

<a id="page-319"></a>

## PDF page 319

### A.12 Message Extension Data

Message Extensions are used to carry additional data that is not defined in this Core Specification. The party defining the Message Extension shall define the format of the data. Examples of data to be sent via extensions:

- Data represented in JSON objects

- Binary data

- Single data elements

Data shall be sent in the Message Extension field with the data populated within a JSON array. Multiple extensions represented as JSON objects may be within the JSON array if required. A maximum of 15 extensions (objects) are supported within the Message Extension data element, totalling a maximum of 81920 characters. The specific elements that shall comprise the extension are:

- Extension name (name)

- Assigned extension group identifier (id)

- Criticality indicator (criticalityIndicator)

- Data (data)

---

<a id="page-320"></a>

## PDF page 320

For example (with multiple extensions defined):

{"messageExtension":

[

{

"name":"extension1",

"id":"ID1",

"criticalityIndicator":true,

"data":{

"valueOne":"value"

}

},

{

"name":"extension2",

"id":"ID2",

"criticalityIndicator":true,

"data":{

"valueOne":"value1",

"valueTwo":"value2"

}

},

{

"name":"sharedData",

"id": "ID3",

"criticalityIndicator":false,

---

<a id="page-321"></a>

## PDF page 321

"data":{

"value3":"IkpTT05EYXRhIjogew0KImRhdGExIjogInNvbWUgZGF0YSIsDQoiZGF0YTIiOiAic29tZSBvdGhlciB kYXRhIg0KfQ=="

}

}

]}

### A.12.1 Message Extension Attributes

Table A.9:  Message Extension Attributes

| Attribute Name | Description | Length/Format/Value | Inclusion |
| --- | --- | --- | --- |
| criticalityIndicator | A Boolean value indicating whether the recipient must understand the<br>contents of the extension to interpret the entire message. | JSON Data Type: Boolean<br>Values accepted:<br>• true<br>• false | R |
| data | The data carried in the extension. | Length: Variable, maximum 8059<br>characters<br>JSON Data Type: Object | R |
| id | A unique identifier for the extension.<br>Note: Payment System Registered Application Provider Identifier (RID)<br>is required as prefix of the ID. | Length: Variable, maximum 64<br>characters<br>JSON Data Type: String | R |
| name | The name of the extension data set as defined by the extension owner. | Length: Variable, maximum 64<br>characters<br>JSON Data Type: String | R |

---

<a id="page-322"></a>

## PDF page 322

### A.12.2 Identification

Each Message Extension defined for use in 3-D Secure must have a unique identifier assigned. Examples of unique identifiers include:

- EMVCo-assigned IDs

- Object IDs (OID)

- Uniform Resource Identifiers (URI)

- DS-assigned IDs

The party defining the message extension specifies the format of the identifier and the value.

### A.12.3 Criticality

The data in a Message Extension may affect the meaning of the rest of the data such that the entire message can only be understood in the context of the extension data. When this occurs, the extension is deemed to be critical and the value of the criticality attribute must = true. When an extension is critical, recipients of the message must recognise and be able to process the extension. If a 3-D Secure application receives a message containing a critical extension that it does not recognise, it must treat the message as invalid and return Error Code = 202. When an extension is non-critical, recipients that cannot recognise the extension must ignore the data and pass it to the destination system unaltered. All critical Message Extensions shall be assigned by EMVCo.

### A.13 3DS Requestor Risk Information

3DS Requestor Risk Information are specific data elements within the AReq message that the 3DS Requestor provides to the ACS in support of the ACS risk assessment. The data elements are optional in the AReq message. However, the presence of the data elements in the AReq message will make the risk-based authentication more precise. By evaluating these data elements, the ACS has data available that can reduce the number of unnecessary challenges. The data elements include the following types of information:

- Cardholder Account—Cardholder’s account at the 3DS Requestor (if the Cardholder is not a Guest)

- Merchant Risk Indicator—Purchase and its risk

- 3DS Requestor Authentication—How the 3DS Requestor authenticated the Cardholder

---

<a id="page-323"></a>

## PDF page 323

- 3DS Requestor Prior Transaction Authentication—How the 3DS Requestor previously used 3DS to authenticate the Cardholder

These data elements are included in Table A.1 as individual data elements with a JSON object format. The following sections provide detailed information of each name/value pair (NVP) data element.

### A.13.1 Cardholder Account Information

The Cardholder Account Information contains optional information about the Cardholder Account. The detailed data elements which are optional are outlined in Table A.10. Note: Cardholder Account Information data elements used to define a time period can be included as either the specific date or an approximate indicator for when the action occurred. 3DS Requestors can use either format.

Table A.10:  Cardholder Account Information

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| Cardholder Account Age Indicator<br>Field Name: chAccAgeInd | Length of time that the Cardholder has had the<br>account with the 3DS Requestor. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = No account (guest checkout)<br>• 02 = Created during this transaction<br>• 03 = Less than 30 days<br>• 04 = 30–60 days<br>• 05 = More than 60 days |
| Cardholder Account Change<br>Field Name: chAccChange | Date converted into UTC that the Cardholder’s<br>account with the 3DS Requestor was last changed,<br>including Billing or Shipping address, new payment<br>account, or new user(s) added. | Length: 8 characters<br>JSON Data Type: String<br>Format accepted:<br>• Date format = YYYYMMDD |

---

<a id="page-324"></a>

## PDF page 324

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| Cardholder Account Change Indicator<br>Field Name: chAccChangeInd | Length of time since the Cardholder’s account<br>information with the 3DS Requestor was last<br>changed, including Billing or Shipping address, new<br>payment account, or new user(s) added. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Changed during this transaction<br>• 02 = Less than 30 days<br>• 03 = 30–60 days<br>• 04 = More than 60 days |
| Cardholder Account Date<br>Field Name: chAccDate | Date converted into UTC that the Cardholder<br>opened the account with the 3DS Requestor. | Length: 8 characters<br>JSON Data Type: String<br>Format accepted:<br>• Date format = YYYYMMDD |
| Cardholder Account Password Change<br>Field Name: chAccPwChange | Date converted into UTC that Cardholder’s account<br>with the 3DS Requestor had a password change or<br>account reset. | Length: 8 characters<br>JSON Data Type: String<br>Format accepted:<br>• Date format = YYYYMMDD |
| Cardholder Account Password Change<br>Indicator<br>Field Name: chAccPwChangeInd | Indicates the length of time since the Cardholder’s<br>account with the 3DS Requestor had a password<br>change or account reset. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = No change<br>• 02 = Changed during this transaction<br>• 03 = Less than 30 days<br>• 04 = 30–60 days<br>• 05 = More than 60 days |

---

<a id="page-325"></a>

## PDF page 325

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| Cardholder Account Purchase Count<br>Field Name: nbPurchaseAccount | Number of purchases with this Cardholder account<br>during the previous six months.<br>If the Cardholder Account Purchase Count reaches<br>the value 999, it remains set at 999. | Length: Variable, maximum 4 characters<br>JSON Data Type: String<br>Values accepted:<br>• 0–999 |
| Cardholder Account Requestor ID<br>Field Name: chAccReqID | The 3DS Requestor assigned account identifier of<br>the transacting Cardholder.<br>This identifier is coded as the SHA-256 + Base64url<br>of the account identifier for the 3DS Requestor and<br>is provided as a String. | Length: Variable, maximum 64 characters<br>JSON Data Type: String |
| Number of Provisioning Attempts Per Day<br>Field Name: provisionAttemptsDay | Number of Add Card attempts in the last 24 hours.<br>Example values:<br>• 2<br>• 02<br>• 002 | Length: Variable, maximum 3 characters<br>JSON Data Type: String |
| Number of Transactions Per Day<br>Field Name: txnActivityDay | Number of transactions (successful and<br>abandoned) for this Cardholder account with the<br>3DS Requestor across all payment accounts in the<br>previous 24 hours.<br>Example values:<br>• 2<br>• 02<br>• 002 | Length: Variable, maximum 3 characters<br>JSON Data Type: String |

---

<a id="page-326"></a>

## PDF page 326

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| Number of Transactions Per Year<br>Field Name: txnActivityYear | Number of transactions (successful and<br>abandoned) for this Cardholder account with the<br>3DS Requestor across all payment accounts in the<br>previous year.<br>If the maximum value is reached, the Number of<br>Transactions Per Year remains set at 999.<br>Example values:<br>• 2<br>• 02<br>• 002 | Length: Variable, maximum 3 characters<br>JSON Data Type: String<br>Values accepted:<br>• 0–999 |
| Payment Account Age<br>Field Name: paymentAccAge | Date converted into UTC that the payment account<br>was enrolled in the Cardholder’s account with the<br>3DS Requestor. | Length: 8 characters<br>JSON Data Type: String<br>Format accepted:<br>• Date format = YYYYMMDD |
| Payment Account Age Indicator<br>Field Name: paymentAccInd | Indicates the length of time that the payment<br>account was enrolled in the Cardholder’s account<br>with the 3DS Requestor. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = No account (guest checkout)<br>• 02 = During this transaction<br>• 03 = Less than 30 days<br>• 04 = 30–60 days<br>• 05 = More than 60 days |

---

<a id="page-327"></a>

## PDF page 327

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| Shipping Address Usage<br>Field Name: shipAddressUsage | Date converted into UTC when the shipping<br>address used for this transaction was first used with<br>the 3DS Requestor. | Length: 8 characters<br>JSON Data Type: String<br>Format accepted:<br>• Date format = YYYYMMDD |
| Shipping Address Usage Indicator<br>Field Name: shipAddressUsageInd | Indicates when the shipping address used for this<br>transaction was first used with the 3DS Requestor. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = This transaction<br>• 02 = Less than 30 days<br>• 03 = 30–60 days<br>• 04 = More than 60 days |
| Shipping Name Indicator<br>Field Name: shipNameIndicator | Indicates if the Cardholder Name on the account is<br>identical to the shipping Name used for this<br>transaction. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Account Name identical to shipping Name<br>• 02 = Account Name different than shipping Name |
| Suspicious Account Activity<br>Field Name: suspiciousAccActivity | Indicates whether the 3DS Requestor has<br>experienced suspicious activity (including previous<br>fraud) on the Cardholder account. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = No suspicious activity has been observed<br>• 02 = Suspicious activity has been observed |

---

<a id="page-328"></a>

## PDF page 328

### A.13.2 Merchant Risk Indicator

The Merchant Risk Indicator contains optional information about the specific purchase by the Cardholder. The detailed data elements which are optional are outlined in Table A.11.

Table A.11:  Merchant Risk Indicator

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| Delivery Email Address<br>Field Name: deliveryEmailAddress | For electronic delivery, the email address to which the<br>merchandise was delivered. | Length: Variable, maximum 254 characters<br>JSON Data Type: String |
| Delivery Timeframe<br>Field Name: deliveryTimeframe | Indicates the merchandise delivery timeframe. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Electronic delivery<br>• 02 = Same-day shipping<br>• 03 = Overnight shipping<br>• 04 = Two-day or more shipping |
| Gift Card Amount<br>Field Name: giftCardAmount | For prepaid or gift card purchase, the purchase amount total<br>of prepaid or gift card(s) in major units (for example, USD<br>123.45 is 123).<br>Example: gift card amount is USD 123.45:<br>Values accepted:<br>• 123<br>• 0123<br>• 00123 | Length: Variable, maximum 15 characters<br>JSON Data Type: String |

---

<a id="page-329"></a>

## PDF page 329

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| Gift Card Count<br>Field Name: giftCardCount | For prepaid or gift card purchase, total count of individual<br>prepaid or gift cards/codes purchased. | Length: 2 characters<br>JSON Data Type: String |
| Gift Card Currency<br>Field Name: giftCardCurr | For prepaid or gift card purchase, ISO 4217 three-digit<br>currency code of the gift card, other than those listed in<br>Table A.5. | Length: 3 characters; numeric<br>JSON Data Type: String |
| Pre-Order Date<br>Field Name: preOrderDate | For a pre-ordered purchase, the expected date that the<br>merchandise will be available. | Length: 8 characters<br>JSON Data Type: String<br>Format accepted:<br>• Date format = YYYYMMDD |
| Pre-Order Purchase Indicator<br>Field Name: preOrderPurchaseInd | Indicates whether the Cardholder is placing an order for<br>merchandise with a future availability or release date. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Merchandise available<br>• 02 = Future availability |
| Reorder Items Indicator<br>Field Name: reorderItemsInd | Indicates whether the Cardholder is reordering previously<br>purchased merchandise. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = First time ordered<br>• 02 = Reordered |

---

<a id="page-330"></a>

## PDF page 330

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| Shipping Indicator<br>Field Name: shipIndicator | Indicates shipping method chosen for the transaction.<br>Merchants must choose the Shipping Indicator code that most<br>accurately describes the Cardholder’s specific transaction, not<br>their general business.<br>If one or more items are included in the sale, use the Shipping<br>Indicator code for the physical goods, or if all digital goods,<br>use the Shipping Indicator code that describes the most<br>expensive item. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Ship to the Cardholder’s billing<br>address<br>• 02 = Ship to another verified address on file<br>with the Merchant<br>• 03 = Ship to an address that is different<br>than the Cardholder’s billing address<br>• 04 = “Ship to Store” / Pick-up at a local<br>store (Store address shall be populated in<br>shipping address fields)<br>• 05 = Digital goods (includes online services,<br>electronic gift cards and redemption codes)<br>• 06 = Travel and event tickets, not shipped<br>• 07 = Other (for example, gaming, digital<br>services not shipped, emedia subscriptions,<br>etc.)<br>• 08 = Pick-up and go delivery<br>• 09 = Locker delivery (or other automated<br>pick-up) |
| Transaction Characteristics<br>Field Name: transChar | Indicates to the ACS specific transactions identified by the<br>Merchant. | Size: Variable, 1–2 elements<br>JSON Data Type: Array of string<br>String: 2 characters<br>Value accepted:<br>• 01 = Cryptocurrency transaction<br>• 02 = NFT transaction |

---

<a id="page-331"></a>

## PDF page 331

### A.13.3 3DS Requestor Authentication Information

The 3DS Requestor Authentication Information contains optional information about how the Cardholder authenticated during login to their 3DS Requestor account. The 3DS Requestor Authentication Information format is an array of objects, the object contains the optional data elements, as outlined in Table A.12.

Table A.12:  3DS Requestor Authentication Information

| Data Element/Field Name | Source | Description | Length/Format/Values |
| --- | --- | --- | --- |
| 3DS Requestor<br>Authentication Data<br>Field Name:<br>threeDSReqAuthData | 3DS<br>Server | Data that documents and supports a specific authentication process.<br>In the current version of the specification, this data element is not defined in<br>detail. However, the intention is that, for each 3DS Requestor Authentication<br>Method, this field carry data that the ACS can use to verify the authentication<br>process.<br>For example, if the 3DS Requestor Authentication Method is:<br>• 03, then this element can carry information about the provider of the<br>federated ID and related information.<br>• 06, then this element can carry the FIDO Assertion and/or Attestation<br>Data.<br>• 07, then this element can carry FIDO Assertion and/or Attestation. Data<br>with the FIDO Assurance Data signed by a trusted third party.<br>• 08, then this element can carry the SRC Assurance Data.<br>For 3DS Requestor Authentication Method = 06 or 07, refer to the EMV® 3-D<br>Secure White Paper – Use of FIDO® Data in 3-D Secure Messages for the<br>3DS Requestor Authentication Data content and format. | Length: Variable, maximum<br>50000 characters<br>JSON Data Type: String or<br>Object |

3DS Requestor Authentication Method

3DS Server

Mechanism used by the Cardholder to authenticate to the 3DS Requestor.

Length: 2 characters

Note: For 09 = SPC Authentication, the Assertion Data is provided as a JSON object returned by the SPC API.

JSON Data Type: String

Field Name: threeDSReqAuthMethod

Values accepted:

---

<a id="page-332"></a>

## PDF page 332

Data Element/Field Name Source Description Length/Format/Values

- 01 = No 3DS Requestor authentication occurred (i.e., Cardholder “logged in” as guest)

- 02 = Login to the Cardholder account at the 3DS Requestor system using 3DS Requestor’s own credentials

- 03 = Login to the Cardholder account at the 3DS Requestor system using federated ID

- 04 = Login to the Cardholder account at the 3DS Requestor system using Issuer credentials

- 05 = Login to the Cardholder account at the 3DS Requestor system using third-party authentication

- 06 = Login to the Cardholder account at the 3DS Requestor system using FIDO Authenticator

- 07 = Login to the Cardholder account at the 3DS Requestor system using FIDO Authenticator (FIDO Assertion or Attestation data signed)

- 08 = SRC Assurance Data

- 09 = SPC Authentication

---

<a id="page-333"></a>

## PDF page 333

| Data Element/Field Name | Source | Description | Length/Format/Values |
| --- | --- | --- | --- |
|  |  |  | • 10 = Electronic ID<br>Authentication Data<br>• 11–79 = Reserved for<br>EMVCo future use (values<br>invalid until defined by<br>EMVCo)<br>• 80–99 = Reserved for DS<br>use |
| 3DS Requestor<br>Authentication Timestamp<br>Field Name:<br>threeDSReqAuthTimestam<br>p | 3DS<br>Server | Date and time of the Cardholder authentication converted into UTC. | Length: 12 characters<br>JSON Data Type: String<br>Format accepted:<br>• Date format =<br>YYYYMMDDHHMM |
| DS Authentication Information<br>Verification Indicator<br>Field Name:<br>dsAuthInfVerifInd | DS | Value that represents the signature verification performed by the DS on the<br>mechanism (e.g., FIDO) used by the Cardholder to authenticate to the 3DS<br>Requestor.<br>The DS populates this data element prior to passing to the ACS. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Verified<br>• 02 = Failed<br>• 03 = Not performed<br>• 04–79 = Reserved for<br>EMVCo future use (values<br>invalid until defined by<br>EMVCo)<br>• 80–99 = Reserved for DS<br>use |

---

<a id="page-334"></a>

## PDF page 334

### A.13.4 3DS Requestor Prior Transaction Authentication Information

The 3DS Requestor Prior Transaction Authentication Information contains optional information about a 3DS Cardholder authentication that occurred prior to the current transaction. The 3DS Requestor Prior Authentication Information format is an array of objects, the objects contain the optional data elements as outlined in Table A.13.

Table A.13:  3DS Requestor Prior Transaction Authentication Information

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| 3DS Requestor Prior DS Transaction ID<br>Field Name:<br>threeDSReqPriorDsTransId | This data element provides the prior DS Transaction ID to the ACS to<br>determine the best approach for handling a request. | Length: 36 characters<br>JSON Data Type: String<br>Value accepted:<br>• This data element contains a DS<br>Transaction ID for a prior<br>authenticated transaction (for<br>example, the first recurring<br>transaction that was authenticated<br>with the Cardholder). |
| 3DS Requestor Prior Transaction<br>Authentication Data<br>Field Name:<br>threeDSReqPriorAuthData | Data that documents and supports a specific authentication process.<br>In the current version of the specification this data element is not<br>defined in detail. However, the intention is that for each 3DS<br>Requestor Authentication Method, this field carry data that the ACS<br>can use to verify the authentication process. In future versions of the<br>specification, these details are expected to be included. | Length: Variable, maximum 20000<br>characters<br>JSON Data Type: String |

---

<a id="page-335"></a>

## PDF page 335

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| 3DS Requestor Prior Transaction<br>Authentication Method<br>Field Name:<br>threeDSReqPriorAuthMethod | Mechanism used by the Cardholder to previously authenticate to the<br>3DS Requestor. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Frictionless authentication<br>occurred by ACS<br>• 02 = Cardholder challenge occurred<br>by ACS<br>• 03 = AVS verified<br>• 04 = Other Issuer methods<br>• 05 = SPC authentication<br>• 06–79 = Reserved for EMVCo future<br>use (values invalid until defined by<br>EMVCo)<br>• 80–99 = Reserved for DS use |
| 3DS Requestor Prior Transaction<br>Authentication Timestamp<br>Field Name:<br>threeDSReqPriorAuthTimestamp | Date and time converted into UTC of the prior Cardholder<br>authentication. | Length: 12 characters<br>JSON Data Type: String<br>Format accepted:<br>• Date format = YYYYMMDDHHMM |

---

<a id="page-336"></a>

## PDF page 336

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| 3DS Requestor Prior Transaction<br>Reference<br>Field Name: threeDSReqPriorRef | This data element provides additional information to the ACS to<br>determine the best approach for handing a request. | Length: 36 characters<br>JSON Data Type: String<br>Value accepted:<br>• This data element contains an ACS<br>Transaction ID for a prior<br>authenticated transaction (for<br>example, the first recurring<br>transaction that was authenticated<br>with the Cardholder). |

### A.13.5 ACS Rendering Type

The ACS Rendering Type identifies required elements and provides information about the rendering type that the ACS is sending for the Cardholder authentication. The detailed data elements are outlined in Table A.14.

Table A.14:  ACS Rendering Type

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| ACS Interface<br>Field Name: acsInterface | This the ACS interface that the challenge will present to the<br>Cardholder. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Native UI<br>• 02 = HTML UI | R |

---

<a id="page-337"></a>

## PDF page 337

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| ACS UI Template<br>Field Name: acsUiTemplate | Identifies the UI Template format that the ACS first presents to the<br>Cardholder.<br>Valid values for each Interface:<br>• Native UI = 01–04, 07<br>• HTML UI = 01–07<br>Note: HTML Other and HTML OOB are only valid in combination with<br>02 = HTML UI. If used with 01 = Native UI, the DS will respond with<br>Error = 203 as described in Sections 5.9.3 and 5.9.8. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Text<br>• 02 = Single Select<br>• 03 = Multi Select<br>• 04 = OOB<br>• 05 = HTML Other<br>• 06 = HTML OOB<br>• 07 = Information | R |
| Device User Interface Mode<br>Field Name:<br>deviceUserInterfaceMode | Indicates the user interface mode the ACS will present to the<br>Cardholder for a challenge. | Length: 2 characters; numeric<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Portrait<br>• 02 = Landscape<br>• 03 = Voice<br>• 04 = Other | R |

JSON Object Example

{

"acsRenderingType":{ "acsInterface":"02","acsUiTemplate":03","deviceUserInterfaceMode":"02" }

}

---

<a id="page-338"></a>

## PDF page 338

### A.13.6 Device Rendering Options Supported

The Device Rendering Options Supported contains information about the rendering types and interface that the device supports. The detailed data elements are outlined in Table A.15. Note:  All Device Rendering Options must be supported by all components.

Table A.15:  Device Rendering Options Supported

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| SDK Authentication Type<br>Field Name:<br>sdkAuthenticationType | Authentication methods preferred by the 3DS<br>SDK in order of preference. | Size: 1–99 elements<br>JSON Data Type: Array of string<br>String: 2 characters<br>Values accepted:<br>• 01 = Static Passcode<br>• 02 = SMS OTP<br>• 03 = Key fob or EMV card reader OTP<br>• 04 = App OTP<br>• 05 = OTP Other<br>• 06 = KBA<br>• 07 = OOB Biometrics<br>• 08 = OOB Login<br>• 09 = OOB Other<br>• 10 = Other<br>• 11 = Push Confirmation<br>• 12–79 = Reserved for EMVCo future use (values<br>invalid until defined by EMVCo)<br>• 80–99 = Reserved for DS use | O |

---

<a id="page-339"></a>

## PDF page 339

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| SDK Interface<br>Field Name: sdkInterface | Lists all of the SDK Interface types that the<br>device supports for displaying specific<br>challenge user interfaces within the 3DS SDK. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Native<br>• 02 = HTML<br>• 03 = Both | R |
| SDK UI Type<br>Field Name: sdkUiType | Lists all UI types that the device supports for<br>displaying specific challenge user interfaces<br>within the 3DS SDK.<br>Valid values for each Interface:<br>• Native UI = 01–04, 07<br>• HTML UI = 01–07<br>Note: Currently, all 3DS SDKs need to<br>support all UI Types. In the future, however,<br>this may change (for example, smart watches<br>may support a UI Type not yet defined by this<br>specification). | Size: Variable, 1–7 elements<br>JSON Data Type: Array of string<br>String: 2 characters<br>Values accepted:<br>• 01 = Text<br>• 02 = Single Select<br>• 03 = Multi Select<br>• 04 = OOB<br>• 05 = HTML Other (valid only for HTML UI)<br>• 06 = HTML OOB (valid only for HTML UI)<br>• 07 = Information | R |

{

"deviceRenderOptions":{ "sdkInterface":"03", "sdkAuthenticationType":["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"], "sdkUiType":["01", "02", "03", "04", "05", "06", "07"] }

}

---

<a id="page-340"></a>

## PDF page 340

### A.13.7 Challenge Data Entry

The Challenge Data Entry (challengeDataEntry) contains the data that the Cardholder entered in the Native UI text field. Table A.16 identifies the 3-D Secure message handling when this element is missing, assuming that no other errors are found. For ACS UI Type = 01, the Challenge Data Entry is considered as missing in the table when both the Challenge Data Entry (challengeDataEntry) and the optional Challenge Data Entry 2 (challengeDataEntryTwo) are missing.

Table A.16:  Challenge Data Entry

| Challenge<br>Data Entry | ACS UI<br>Type | Challenge<br>Cancelation<br>Indicator | Resend<br>Challenge<br>Information<br>Code | Challenge<br>Additional<br>Code | Challenge No<br>Entry | Response |
| --- | --- | --- | --- | --- | --- | --- |
| Missing | 01, 02, or<br>03 | Missing | Missing | Missing | Present<br>• Value = Y | The ACS assumes that the Cardholder has not<br>entered challenge data in the UI and therefore the<br>ACS does not send the 3DS SDK an Error Message,<br>but instead sends a CRes message. |
| Missing | 01, 02, or<br>03 | Present | Missing | Missing | Missing | The ACS sends the 3DS SDK a CRes message. |
| Missing | 01, 02, or<br>03 | Missing | Present<br>• Value = Y | Missing | Missing | The ACS sends the 3DS SDK a CRes message. |
| Missing | 01, 02, or<br>03 | Missing | Missing | Present<br>• Value = Y | Missing | The ACS sends the 3DS SDK a CRes message. |
| Missing | 01, 02, or<br>03 | Present | Present | Missing | Present<br>• Value = Y | If at least two of the fields Challenge Cancelation<br>Indicator, Resend Challenge Information Code<br>and/or Challenge No Data Entry are present, the<br>ACS sends the 3DS SDK an Error Message. |

---

<a id="page-341"></a>

## PDF page 341

Note: For all the combinations of Challenge Data Entry, Challenge Cancelation Indicator, Resend Challenge Information Code, Challenge Additional Code and Challenge No Entry not present in Table A.16, the ACS sends an Error Message (as defined in Section A.9) with Error Code = 203 to the 3DS SDK.

### A.13.8 Transaction Status Conditions

The Transaction Status (transStatus) indicates whether a transaction qualifies as an authenticated transaction or account verification. The conditions on which indicators are valid within the 3-D Secure messages are outlined in Table A.17.

Table A.17:  Transaction Status Conditions

| Transaction Status | ARes | Final<br>CRes | RReq | Error Response |
| --- | --- | --- | --- | --- |
| Y = Authentication Verification Successful | Valid | Valid | Valid | Not applicable |
| N = Not Authenticated/Account Not Verified; Transaction denied | Valid | Valid | Valid | Not applicable |
| U = Authentication/Account Verification Could Not Be Performed;<br>Technical or other problem, as indicated in the ARes or RReq | Valid | Invalid | Valid | Final CRes: End processing (no Error) |
| A = Attempts Processing Performed; Not Authenticated/Verified,<br>but a proof of attempted authentication/verification is provided | Valid | Invalid | Valid | Final CRes: End processing (no Error) |
| C = Challenge Required; Additional authentication is required<br>using the CReq/CRes | Valid 9 | Invalid | Invalid | • ARes: Refer to Section 5.9.3 and use Error Code = 203<br>if Condition not met<br>• Final CRes: End processing (no Error) |

9 This indicator (C) is not valid if Device Channel = 03, or if the 3DS Requestor Challenge Indicator = 06 (No challenge requested; Data share only) within the AReq message.

---

<a id="page-342"></a>

## PDF page 342

| Transaction Status | ARes | Final<br>CRes | RReq | Error Response |
| --- | --- | --- | --- | --- |
| D = Challenge Required; Decoupled Authentication confirmed | Valid10 | Valid11 | Valid11 | • ARes: Refer to Section 5.9.3 and use Error Code = 203<br>if Condition not met<br>• Final CRes: Not applicable<br>• RReq: Refer to Section 5.9.8 and use Error Code = 203<br>if Condition not met |
| R = Authentication/ Account Verification Rejected; Issuer is<br>rejecting authentication/verification and request that authorisation<br>not be attempted | Valid | Invalid | Valid | Final CRes: End processing (no Error) |
| I = Informational Only; 3DS Requestor challenge preference<br>acknowledged | Valid 12 | Invalid | Invalid | • ARes: Refer to Section 5.9.3 and use Error Code = 203<br>if Condition not met<br>• Final CRes: End processing (no Error)<br>• RReq: Refer to Section 5.9.8 and use Error Code = 203 |
| S = Challenge using SPC | Valid13 | Invalid | Invalid | • ARes: Refer to Section 5.9.3 and use Error Code = 203<br>if Condition not met<br>• Final CRes: End processing (no Error)<br>• RReq: Refer to Section 5.9.8 and use Error Code = 203 |

10 This indicator (D) can be sent only if 3DS Requestor Decoupled Request Indicator = Y or B within the AReq message.

11 This indicator (D) can be sent only if 3DS Requestor Decoupled Request Indicator = F or B within the AReq message.

12 This indicator (I) can be sent only if 3DS Requestor Challenge Indicator = 05, 06, or 07 within the AReq message (or as specified by DS rules).

13 This indicator (S) can be sent only if 3DS Requestor SPC Support = Y within the AReq message.

---

<a id="page-343"></a>

## PDF page 343

### A.13.9 Multi-Transaction

The Multi-Transaction object contains optional information about a specific purchase by the Cardholder invoking multiple transactions or Merchants. The detailed data elements are outlined in Table A.18.

Table A.18:  Multi-Transaction

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Merchant List<br>Field Name: merchantList | Contains the details of each Merchant<br>involved in the transaction.<br>JSON array of objects containing:<br>• Merchant Name Listed<br>• Acquirer Merchant ID Listed<br>• Merchant Amount<br>• Merchant Currency Code<br>• Merchant Currency Exponent<br>• Seller ID | Size: Variable, 1–50 elements<br>JSON Data Type: Array of objects<br>Values accepted:<br>• Refer to the following data elements:<br>o Merchant Name Listed<br>o Acquirer Merchant ID Listed<br>o Merchant Amount<br>o Merchant Currency Code<br>o Merchant Currency Exponent<br>o Seller ID | Required |
| Merchant Name Listed<br>Field Name: merchantNameListed | Name of the listed Merchant | Length: Variable, maximum 40 characters<br>JSON Data Type: String<br>Value accepted:<br>• Name used in the authorisation<br>message as defined in ISO 8583-1. | Required |

Acquirer Merchant ID Listed

Acquirer-assigned Merchant Listed Identifier.

Length: Variable, maximum 15 characters

Optional

Field Name: acquirerMerchantIdListed

This may be the same value that is used in authorisation requests sent on behalf of the 3DS Requestor and is represented in ISO 8583-1 formatting requirements.

JSON Data Type: String

---

<a id="page-344"></a>

## PDF page 344

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Merchant Amount<br>Field Name: merchantAmount | Purchase amount for the Merchant in minor<br>units of currency with all punctuation<br>removed.<br>When used in conjunction with the Purchase<br>Currency Exponent field, proper punctuation<br>can be calculated. | Length: Variable, maximum 48 characters<br>JSON Data Type: String | Optional |
| Merchant Currency Code<br>Field Name: merchantCurrency | Currency Code in which purchase Merchant<br>Amount is expressed.<br>ISO 4217 three-digit currency code, other<br>than those listed in Table A.5. | Length: 3 characters, numeric<br>JSON Data Type: String | Required if<br>Merchant<br>Amount is<br>present |
| Merchant Currency Exponent<br>Field Name: merchantExponent | Minor units of Merchant Currency as specified<br>in the ISO 4217 currency exponent. | Length: 1 character<br>JSON Data Type: String | Required if<br>Merchant<br>Amount is<br>present |
| Seller ID<br>Field Name: sellerId | Merchant-assigned Seller identifier that links<br>additional Seller Information outlined in<br>Table A.19.<br>Note: If this data element is present, this must<br>match the Seller ID field in the Seller<br>Information object. | Length: Variable, maximum 50 characters<br>JSON Data Type: String | Optional |
| AV Validity Time<br>Field Name: avValidityTime | Number of days that the AV (Authentication<br>Value) is valid. | Length: 1–3 characters; numeric<br>JSON Data Type: String<br>Values accepted:<br>• 0–999 | Conditional<br>based on DS<br>rules |

---

<a id="page-345"></a>

## PDF page 345

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| AV Number Use<br>Field Name: avNumberUse | Number of times that the AV (Authentication<br>Value) is valid. | Length: 1–2 characters; numeric<br>JSON Data Type: String<br>Values accepted:<br>• 0–99 | Conditional<br>based on DS<br>rules |

---

<a id="page-346"></a>

## PDF page 346

JSON Object Example

{

"merchantList": [

{

"merchantNameListed": "Merchant 1",

"acquirerMerchantIdListed": "Acquirer Merchant Id Merchant 1",

"merchantAmount": "100",

"merchantCurrency": "840",

"merchantExponent": "2",

"sellerId": "Seller Id 1"

},

{

"merchantNameListed": "Merchant 2",

"acquirerMerchantIdListed": "Acquirer Merchant Id Merchant 2",

"merchantAmount": "20000",

"merchantCurrency": "392",

"merchantExponent": "0",

"sellerId": "Seller Id 2",

}

],

"avValidityTime": "2",

"avNumberUse": "3"

}

---

<a id="page-347"></a>

## PDF page 347

### A.13.10 Seller Information

The Seller Information object contains optional information about a specific purchase by the Cardholder invoking transactions where Merchants submit transaction details on behalf of another entity, i.e., individual sellers in a marketplace or drivers in a ridesharing platform. The detailed data elements are outlined in Table A.19.

Table A.19:  Seller Information

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Seller Information<br>Field Name: sellerInfo | Contains the details of each seller involved in<br>the transaction.<br>JSON array of objects containing:<br>• Seller Name<br>• Seller ID<br>• Seller Business Name<br>• Seller Account Date<br>• Seller Address Line 1<br>• Seller Address Line 2<br>• Seller Address Line 3<br>• Seller Address City<br>• Seller Address State<br>• Seller Address Postal Code<br>• Seller Address Country<br>• Seller Email Address<br>• Seller Phone Number | Size: Variable, 1–50 elements<br>JSON Data Type: Array of objects<br>Values accepted:<br>• Refer to the following data elements:<br>o Seller Name<br>o Seller ID<br>o Seller Business Name<br>o Seller Account Date<br>o Seller Address Line 1<br>o Seller Address Line 2<br>o Seller Address Line 3<br>o Seller Address City<br>o Seller Address State<br>o Seller Address Postal Code<br>o Seller Address Country<br>o Seller Email Address<br>o Seller Phone Number | Required |
| Seller Name<br>Field Name: sellerName | Name of the Seller. | Length: Variable, maximum 100 characters<br>JSON Data Type: String | Required |

---

<a id="page-348"></a>

## PDF page 348

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Seller ID<br>Field Name: sellerId | Merchant-assigned Seller identifier. | Length: Variable, maximum 50 characters<br>JSON Data Type: String | Required if<br>Seller ID in<br>Multi-<br>Transaction<br>object is<br>present. |
| Seller Business Name<br>Field Name: sellerBusinessName | Business name of the Seller. | Length: Variable, maximum 100 characters<br>JSON Data Type: String | Optional |
| Seller Account Date<br>Field Name: sellerAccDate | Date converted into UTC that the Seller<br>started using the Merchant’s services. | Length: 8 characters<br>JSON Data Type: String<br>Format accepted:<br>• Date format = YYYYMMDD | Optional |
| Seller Address Line 1<br>Field Name: sellerAddrLine1 | First line of the business or contact street<br>address of the Seller. | Length: Variable, maximum 50 characters<br>JSON Data Type: String | Optional |
| Seller Address Line 2<br>Field Name: sellerAddrLine2 | Second line of the business or contact street<br>address of the Seller. | Length: Variable, maximum 50 characters<br>JSON Data Type: String | Optional |
| Seller Address Line 3<br>Field Name: sellerAddrLine3 | Third line of the business or contact street<br>address of the Seller. | Length: Variable, maximum 50 characters<br>JSON Data Type: String | Optional |
| Seller Address City<br>Field Name: sellerAddrCity | Business or contact city of the Seller. | Length: Variable, maximum 50 characters<br>JSON Data Type: String | Optional |

---

<a id="page-349"></a>

## PDF page 349

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Seller Address State<br>Field Name: sellerAddrState | Business or contact state or province of the<br>Seller. | Length: Variable, maximum 3 characters<br>JSON Data Type: String<br>Value accepted:<br>• Country subdivision code defined in ISO<br>3166-2.<br>For example, using the ISO entry US-CA<br>(California, United States), the correct value<br>for this field = CA. Note that the country and<br>hyphen are not included in this value. | Optional |
| Seller Address Postal Code<br>Field Name: sellerAddrPostCode | Business or contact ZIP or other postal code<br>of the Seller. | Length: Variable, maximum 16 characters<br>JSON Data Type: String | Optional |
| Seller Address Country<br>Field Name: sellerAddrCountry | Business or contact country of the Seller. | Length: 3 characters<br>JSON Data Type: String<br>Values accepted:<br>• ISO 3166-1 numeric three-digit country<br>code, other than exceptions listed in<br>Table A.5. | Optional |
| Seller Email Address<br>Field Name: sellerEmail | Business or contact email address of the<br>Seller. | Length: Variable, maximum 254 characters<br>JSON Data Type: String<br>Values accepted:<br>• Shall meet requirements of Section 3.4<br>of IETF RFC 5322. | Optional |

---

<a id="page-350"></a>

## PDF page 350

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Seller Phone Number<br>Field Name: sellerPhone | Business or contact phone number of the<br>Seller. | Length: Variable<br>• cc: 1–3 characters<br>• subscriber: Variable, maximum 15<br>characters<br>Format: JSON object; strings<br>Values accepted:<br>• Country Code and Subscriber sections<br>of the number represented by the<br>following named fields:<br>o cc<br>o subscriber<br>Refer to ITU-E.164 for additional information<br>on format and length.<br>Example:<br>“sellerPhone”: {<br>“cc”: “1”,<br>“subscriber”: “1234567899”<br>} | Optional |

JSON Object Example

{

"sellerInfo": [

{

"sellerName": "Seller 1",

"sellerId": "Seller Id 1",

---

<a id="page-351"></a>

## PDF page 351

"sellerBusinessName": "Seller Business 1",

"sellerAccDate": "20210928",

"sellerAddrLine1": "Seller1 avenue 101",

"sellerAddrCity": "Seller1 city",

"sellerAddrState": "AZ",

"sellerAddrPostCode": "43121",

"sellerAddrCountry": "840",

"sellerEmail": "seller1@seller1.com"

},

{

"sellerName": "Seller 2",

"sellerId": "Seller Id 2",

"sellerBusinessName": "Seller Business 2",

"sellerAccDate": "20201022",

"sellerAddrLine1": "Seller2 road",

"sellerAddrCity": "Seller2 city",

"sellerAddrState": "CA",

"sellerAddrPostCode": "94212",

"sellerAddrCountry": "840",

"sellerPhone": {"cc": "1","subscriber": "1234567899"}

}

]

}

---

<a id="page-352"></a>

## PDF page 352

### A.14 UI Data Elements

Table A.20 specifies the placement and the inclusion of UI data elements on the UI with respect to the zones defined in Section 4.1.

- M = Mandatory inclusion

- O = Optional inclusion—Optional to provide for the ACS; If present, Mandatory to display for the SDK

- C = Conditional inclusion

- N = Not present

Table A.20:  UI Data Elements

| Data Element / Field Name | Zone | Display Order<br>(Top-down) |  | ACS UI Type |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Portrait | Landscape | 01 =<br>Text | 02 =<br>Single Select | 03 =<br>Multi Select | 04 =<br>OOB | 07 =<br>Information |
| Challenge Additional Label<br>Field Name: challengeAddLabel | 3 | 11 | 9 | O | O | O | O | O |
| Challenge Entry Box<br>Field Name: challengeEntryBox | 3 | 5 | 5 | M | N | N | N | N |
| Challenge Entry Box 2<br>Field Name:<br>challengeEntryBoxTwo | 3 | 6 | 5 or 6 | O | N | N | N | N |
| Challenge Information Header<br>Field Name: challengeInfoHeader | 3 | 2 | 2 | M | M | M | M | M |

---

<a id="page-353"></a>

## PDF page 353

| Data Element / Field Name | Zone | Display Order<br>(Top-down) |  | ACS UI Type |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Portrait | Landscape | 01 =<br>Text | 02 =<br>Single Select | 03 =<br>Multi Select | 04 =<br>OOB | 07 =<br>Information |
| Challenge Data Entry Masking Toggle<br>Field Name:<br>challengeDataEntryToggle | 3 | 5 | 5 | O | N | N | N | N |
| Challenge Information Label<br>Field Name: challengeInfoLabel | 3 | 4 | 4 | N | M | M | O | O |
| Challenge Information Text<br>Field Name: challengeInfoText | 3 | 3 | 3 | M | M | M | M | M |
| Challenge Information Text Indicator<br>Field Name:<br>challengeInfoTextIndicator | 3 | 3 | 3 | O | O | O | O | O |
| Challenge Selection Information<br>Field Name: challengeSelectInfo | 3 | 5 | 5 | N | M | M | N | N |
| Device Binding Information Text14<br>Field Name:<br>deviceBindingInfoText | 4 | 8 or 13 | 8 or 12 | O | O | O | O | O |
| Expandable Information Label<br>Field Name: expandInfoLabel | 4 | 16 | 12 | O | O | O | O | O |

14 Device Binding Information Text display order depends on the Toggle Position Indicator.

---

<a id="page-354"></a>

## PDF page 354

| Data Element / Field Name | Zone | Display Order<br>(Top-down) |  | ACS UI Type |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Portrait | Landscape | 01 =<br>Text | 02 =<br>Single Select | 03 =<br>Multi Select | 04 =<br>OOB | 07 =<br>Information |
| Expandable Information Text<br>Field Name: expandInfoText | 4 | 17 | 13 | O | O | O | O | O |
| Information Continuation Label<br>Field Name: infoContinueLabel | 3 | 10 | 9 | N | N | N | N | M |
| Issuer Image15<br>Field Name: issuerImage | 2 | 1 | 1 | C | C | C | C | C |
| OOB App Label16<br>Field Name: oobAppLabel | 3 | 9 | 9 | N | N | N | C | N |
| OOB Continuation Label<br>Field Name: oobContinueLabel | 3 | 10 | 9 | N | N | N | C | N |
| Payment System Image17<br>Field Name: psImage | 2 | 1 | 1 | C | C | C | C | C |

15 Refer to Table A.1 for inclusion conditions.

16 Refer to Table A.1 for inclusion conditions.

17 Refer to Table A.1 for inclusion conditions.

---

<a id="page-355"></a>

## PDF page 355

| Data Element / Field Name | Zone | Display Order<br>(Top-down) |  | ACS UI Type |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Portrait | Landscape | 01 =<br>Text | 02 =<br>Single Select | 03 =<br>Multi Select | 04 =<br>OOB | 07 =<br>Information |
| Resend Information Label<br>Field Name:<br>resendInformationLabel | 3 | 10 | 9 | O | N | N | N | N |
| Submit Authentication Label<br>Field Name:<br>submitAuthenticationLabel | 3 | 9 | 9 | M | M | M | N | N |
| Trust List Information Text18<br>Field Name: trustListInfoText | 3 | 7 or 12 | 7 or 10 | O | O | O | O | O |
| Why Information Label<br>Field Name: whyInfoLabel | 4 | 14 | 10 | O | O | O | O | O |
| Why Information Text<br>Field Name: whyInfoText | 4 | 15 | 11 | O | O | O | O | O |

Note: The data elements listed in Table A.20 are not needed for ACS UI Type = 05 and 06 (HTML and HTML OOB template).

18 Trust List Information Text display order depends on the Toggle Position Indicator.

---

<a id="page-356"></a>

## PDF page 356

### A.14.1 Issuer Image

The Issuer Image (issuerImage) is supplied by the ACS to be displayed during the challenge message exchange. The detailed format of this data element is provided in Table A.21. Depending on the display capabilities and mode set by the Cardholder, the 3DS SDK uses:

- The Default Image if it is the only image provided by the ACS, OR if dark mode is not enabled on the device, OR if the device display is not monochrome-only.

- The Dark Mode Image if the 3DS SDK detects that dark mode is enabled on the device.

- The Monochrome Image if the 3DS SDK is running on a device that only supports monochrome display.

Table A.21:  Issuer Image

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| • Default Image<br>Field Name: default<br>• Dark Mode Image<br>Field Name: dark<br>• Monochrome Image<br>Field Name: monochrome | Include at minimum one and at maximum three Fully Qualified URLs defined as<br>default, dark mode or monochrome images of the Issuer Image.<br>Examples:<br>"issuerImage" :{<br>"default": "https://acs.com/default_image.png",<br>"dark": "https://acs.com/dark_image.png",<br>"monochrome": "https://acs.com/monochrome_image.png"<br>} | Length: Variable, maximum 6144<br>characters<br>JSON Data Type: JSON object<br>Value accepted:<br>• Fully Qualified URL in correct<br>JSON object format<br>If present, the Issuer Image object<br>shall contain, at minimum, the<br>Default Image. |

---

<a id="page-357"></a>

## PDF page 357

### A.14.2 Payment System Image

The Payment System Image (psImage) is supplied by the ACS to be displayed during the challenge message exchange. The detailed format of the data element is provided in Table A.22. Depending on the display capabilities and mode set by the Cardholder, the 3DS SDK uses:

- The Default Image if it is the only image provided by the ACS, OR if dark mode is not enabled on the device, OR if the device display is not monochrome-only.

- The Dark Mode Image if the 3DS SDK detects that dark mode is enabled on the device.

- The Monochrome Image if the 3DS SDK is running on a device that only supports monochrome display.

Table A.22:  Payment System Image

| Data Element/Field Name | Description | Length/Format/Values |
| --- | --- | --- |
| • Default Image<br>Field Name: default<br>• Dark Mode Image<br>Field Name: dark<br>• Monochrome Image<br>Field Name: monochrome | Include at minimum one and at maximum three Fully Qualified URLs defined<br>as default, dark mode or monochrome images of the DS or Payment System<br>Image.<br>Examples:<br>"psImage" :{<br>"default": "https://ds.com/default_image.png",<br>"dark": "https://ds.com/dark_image.png",<br>"monochrome": "https://ds.com/monochrome_image.png"<br>} | Length: Variable, maximum 6144<br>characters<br>JSON Data Type: JSON object<br>Value accepted:<br>• Fully Qualified URL in correct JSON<br>object format<br>If present, the Payment System Image<br>object shall contain, at minimum, the<br>Default Image. |

---

<a id="page-358"></a>

## PDF page 358

### A.15 iframe and Sandbox Attributes

Table A.23 specifies the iframe attributes that the 3DS Requestor uses when it creates the challenge or 3DS Method iframe.

Table A.23:  iframe Attributes

| Attribute19 | Value |
| --- | --- |
| allowfullscreen | false |
| allowpaymentrequest | false |
| height | as per Challenge Window Size |
| sandbox | refer to Table A.24 |
| srcdoc | may be used to initialise redirection content |
| width | as per Challenge Window Size |
| allow="payment *; publickey-credentials-get *"20 | enable access to WebAuthn and SPC (Secure Payment Confirmation) API<br>and Payment Request API |

19  Attributes not listed in Table A.23 should not be present.

20  Use the following syntax <iframe src="https://www.foo.com" allow="payment *; publickey-credentials-get *"></iframe>, if supported by the Browser.

---

<a id="page-359"></a>

## PDF page 359

Table A.24 specifies the sandbox attributes that the 3DS Requestor uses when it creates the challenge or 3DS Method iframe.

Table A.24:  Sandbox Attributes

| Attribute | Description | Inclusion |
| --- | --- | --- |
| allow-forms | Allows the processing of forms. | R |
| allow-scripts | Allows the processing of scripts. Note the allow-scripts permission<br>does not give the iframe the ability to create pop-ups or modal windows,<br>which can help prevent clickjacking attacks from occurring. | R |
| allow-same-origin | Gives the iframe permission to only use the data from the same ACS<br>domain. | R |
| allow-pointer-lock | Gives access to the mouse position and events.<br>Note: this attribute is not needed for the 3DS Method iframe. | R |
| allow-downloads-without-user-activation | Prevents downloads to be initiated for content in the iframe without user<br>action. | Not Allowed |
| allow-downloads | Prevents downloads to be initiated for content in the iframe. | Not Allowed |
| allow-modals | Prevents to open modal window from the iframe. | Not Allowed |
| allow-orientation-lock | Prevents to lock the screen orientation. | Not Allowed |
| allow-popups | Prevents pop-up windows. | Not Allowed |
| allow-popups-to-escape-sandbox | Prevents pop-ups to open new windows without inheriting the sandboxing. | Not Allowed |
| allow-presentation | Prevents to initiate a presentation session. | Not Allowed |
| allow-storage-access-by-user-activation | Prevents access to the parent's storage capabilities. | Not Allowed |

---

<a id="page-360"></a>

## PDF page 360

| Attribute | Description | Inclusion |
| --- | --- | --- |
| allow-top-navigation | Prevents access to the top-level browsing context. | Not Allowed |
| allow-top-navigation-by-user-activation | Prevents access to the top-level browsing context also with user<br>interaction. | Not Allowed |

### A.16 3-D Secure Array Fields

A 3-D Secure array is defined to contain either:

- string

- array

- object

A 3-D Secure array is not defined to contain either:

- number

- boolean

- null

- duplicate elements (i.e., identical string, object or array)

Duplicate elements are not allowed in an array (i.e., identical string, object or array). For example: [{"phone": "Mobile **** **** 321"}, {"phone": "Mobile **** **** 321"}] In the case of duplicate elements in an array, the receiving component returns an Error Message as defined in Section A.9 with the applicable Error Component and Error Code = 204.

---

<a id="page-361"></a>

## PDF page 361

### A.17 EMV Payment Token Information

Table A.25 specifies the EMV Payment Token Information that 3-D Secure components can provide or receive token-related information after a Payment Token has been detokenised.

Table A.25:  Token Information

| Description | Source | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Payment token used to initiate the EMV 3DS<br>transaction. | 3DS<br>Server<br>DS | Length: Variable, 13–19 characters<br>JSON Data Type: String<br>Values accepted:<br>• Format represented ISO 7812 | AReq = O |
| Additional information about the Payment<br>Token from the Token Service Provider. | 3DS<br>Server<br>DS | Length: Variable, maximum 500<br>characters<br>JSON Data Type: Object | AReq = O |
| An updatable value that allows the Token<br>Service Provider to communicate the ID&V<br>performed. It is determined or updated by<br>the ID&V Method(s) and ID&V Actor. | DS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• Refer to EMV Tokenisation<br>Technical Framework. | AReq = O |
| An 11-digit numeric value that identifies<br>each unique combination of Token<br>Requestor and Token Domain(s) for a given<br>Token Service Provider. | DS | Length: 11 characters<br>JSON Data Type: String<br>Values accepted:<br>• Refer to EMV Tokenisation<br>Technical Framework. | AReq = O |

Data Element/Attribute Name

Payment Token

Attribute Name: token

Token Additional Data

Attribute Name: tokenAdditionalData

Token Assurance Method

Attribute Name: tokenAssuranceMethod

Token Requestor ID Attribute Name: tokenRequestorId

---

<a id="page-362"></a>

## PDF page 362

| Description | Source | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| A cryptogram, containing a transaction-<br>unique value, typically generated using the<br>Payment Token, Payment Token related<br>data and transaction data. Cryptogram<br>derivation methods may vary by scenario<br>and may be Payment System-specific. | 3DS<br>Server | Length: Variable, maximum 4000<br>characters<br>JSON Data Type: String<br>Values accepted:<br>• Refer to EMV Tokenisation<br>Technical Framework. | AReq = O |
| Identifies if the Token Cryptogram has been<br>verified and the outcome of that verification. | DS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Verified<br>• 02 = Failed<br>• 03 = Not performed<br>• 04–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use<br>Note: If the element is not provided,<br>the expected action is for the ACS to<br>interpret it as 03. | AReq = O |
| Identifies the current status of the Payment<br>Token. | 3DS<br>Server<br>DS | Length: Variable, maximum 40<br>characters<br>JSON Data Type: String | AReq = O |

Data Element/Attribute Name

Token Cryptogram

Attribute Name: tokenCryptogram

Token Cryptogram Validity Indicator

Attribute Name: tokenCryptogramValidityIndicator

Token Status Indicator

Attribute Name: tokenStatusIndicator

---

<a id="page-363"></a>

## PDF page 363

### A.18 Challenge Text Box Settings

Table A.26 specifies the text box settings that the ACS can use during a challenge for ACS UI Type = 01.

Table A.26:  Text Box Settings

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Challenge Data Entry Keyboard Type<br>Field Name:<br>challengeDataEntryKeyboardType | Indicates if the 3DS SDK shall display a<br>numeric or alphanumeric keyboard. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Numeric keyboard<br>• 02 = Alphanumeric keyboard<br>• 03–99 = Reserved for EMVCo future<br>use (values invalid until defined by<br>EMVCo) | O |
| Challenge Data Entry Autofill<br>Field Name:<br>challengeDataEntryAutofill | Indicates if the 3DS SDK enables the autofill<br>option for the Challenge Data Entry.<br>When enabled, the 3DS SDK/OS<br>automatically copies the received or saved<br>code or password in the Challenge Data<br>Entry.<br>If Challenge Data Entry Autofill is not present,<br>the option is not enabled. | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = Autofill supported for the Challenge<br>Data Entry | O |

---

<a id="page-364"></a>

## PDF page 364

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Challenge Data Entry Autofill Type<br>Field Name:<br>challengeDataEntryAutofillType | Indicates the type of data expected when the<br>Challenge Data Entry Autofill is active.<br>Refer to the following for Android or iOS<br>https://developer.android.com/reference/andro<br>idx/autofill/HintConstants<br>https://developer.apple.com/documentation/se<br>curity/password autofill/enabling password a<br>_ _ _<br>utofill on a text input view?language=objc<br>_ _ _ _ _ | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = SMS OTP<br>• 02 = Password<br>• 03–99 = Reserved for EMVCo future<br>use (values invalid until defined by<br>EMVCo) | C<br>Required if<br>Challenge<br>Data Entry<br>Autofill = Y |
| Challenge Data Entry Length Maximum<br>Field Name:<br>challengeDataEntryLengthMax | Indicates to the 3DS SDK the maximum<br>length of the challenge data entry.<br>Set default to 45 if not present. | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01–45 | O |
| Challenge Data Entry Label<br>Field Name: challengeDataEntryLabel | Label to specify the expected data entry<br>provided by the ACS. | Length: Variable, maximum 45 characters<br>JSON Data Type: String | R |
| Challenge Data Entry Masking<br>Field Name:<br>challengeDataEntryMasking | Indicates that the 3DS SDK shall mask the<br>data entered by the Cardholder. | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = Mask the data entered by the<br>Cardholder<br>• N = Do not mask the data entered by<br>the Cardholder. | O |

---

<a id="page-365"></a>

## PDF page 365

| Data Element/Field Name | Description | Length/Format/Values | Inclusion |
| --- | --- | --- | --- |
| Challenge Data Entry Masking Toggle<br>Field Name: challengeDataEntryToggle | Indicates that the 3DS SDK shall display a<br>toggle icon, and display the data entered, if<br>selected by the Cardholder. | Length: 1 character<br>JSON Data Type: String<br>Values accepted:<br>• Y = Display the toggle icon indicator<br>• N = Do not display the toggle icon<br>indicator | Required if<br>Challenge<br>Data Entry<br>Masking = Y |

---

<a id="page-366"></a>

## PDF page 366

### A.19 Broadcast Information

Table A.27 specifies the Broadcast Information object sent between the 3DS Server, the DS and the ACS.

Table A.27:  Broadcast Information

| Data Element/Field Name | Description | Source | Length/Format/Values | Inclusion |
| --- | --- | --- | --- | --- |
| Category<br>Field Name: category | Indicates the category/type of<br>information. | 3DS Server<br>DS<br>ACS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = General<br>• 02 = Certificate expiry<br>• 03 = Fraud alert<br>• 04 = Operational alert<br>• 05 = Transactional data<br>• 06 = Other<br>• 07–79 = Reserved for EMVCo<br>future use (values invalid until<br>defined by EMVCo)<br>• 80–99 = Reserved for DS use | AReq = R<br>ARes = R |
| Description<br>Field Name: description | Information to be broadcast to<br>recipients. | 3DS Server<br>DS<br>ACS | Length: Variable, maximum 4000<br>characters<br>JSON Data Type: String | AReq = O<br>ARes = O |

---

<a id="page-367"></a>

## PDF page 367

| Data Element/Field Name | Description | Source | Length/Format/Values | Inclusion |
| --- | --- | --- | --- | --- |
| Expiry Date<br>Field Name: expDate | The date after which the relevance of<br>the broadcast information (e.g.,<br>certificate expiration dates) expires. | 3DS Server<br>DS<br>ACS | Length: 8 characters<br>JSON Data Type: String<br>Format accepted:<br>• YYYYMMDD | AReq = O<br>ARes = O |
| Severity<br>Field Name: severity | Indicates the importance/severity level<br>of the broadcast information.<br>• Critical = Immediate action to be<br>taken by recipient<br>• Major = Major impact; Upcoming<br>action to be taken by recipient<br>• Minor = Minor impact; Upcoming<br>action to be taken by recipient<br>• Informational = Informational only<br>with no immediate action by<br>recipient | 3DS Server<br>DS<br>ACS | Length: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = Critical<br>• 02 = Major<br>• 03 = Minor<br>• 04 = Informational | AReq = R<br>ARes = R |
| Recipient(s)<br>Field Name: recipients | Indicates the intended recipient(s) of<br>the broadcast information. | 3DS Server<br>DS<br>ACS | Size: Variable, maximum 3<br>elements<br>JSON Data Type: Array of string<br>String: 2 characters<br>Values accepted:<br>• 01 = 3DS SDK<br>• 02 = 3DS Server<br>• 03 = DS<br>• 04 = ACS | AReq = R<br>ARes = R |

---

<a id="page-368"></a>

## PDF page 368

| Data Element/Field Name | Description | Source | Length/Format/Values | Inclusion |
| --- | --- | --- | --- | --- |
| Source<br>Field Name: source | Indicates the source of the broadcast<br>information. | 3DS Server<br>DS<br>ACS | Size: 2 characters<br>JSON Data Type: String<br>Values accepted:<br>• 01 = 3DS Server<br>• 02 = DS<br>• 03 = ACS | AReq = R<br>ARes = R |

---

<a id="page-369"></a>

## PDF page 369

### A.20 Cardholder Information Text

Figure A.1 and Figure A.2 provide a sample UI format to display the Cardholder Information Text to the Cardholder.

Figure A.1  Sample Cardholder Information UI Example—App—Portrait

![Figure A.1  Sample Cardholder Information UI Example—App—Portrait](../../assets/images/figure-A-1.png)

---

<a id="page-370"></a>

## PDF page 370

Figure A.2  Sample Cardholder Information UI Example—Browser—Landscape

![Figure A.2  Sample Cardholder Information UI Example—Browser—Landscape](../../assets/images/figure-A-2.png)

---

<a id="page-371"></a>

## PDF page 371

### A.21 SPC Transaction Data

The field names of the SPC Transaction Data match the names used in the SPC API (refer to SPC API for additional information).

Table A.28:  SPC Transaction Data

| Data Element/Field Name | Description | Source | Length/Format/Values | Inclusion |
| --- | --- | --- | --- | --- |
| Additional Data<br>Field Name: additionalData | For SPC API enhancement, to be defined in<br>a future 3DS specification release | ACS | Length: Variable, maximum 90000 characters<br>JSON Data Type: Object | ARes = O |
| Challenge<br>Field Name: challenge | Random string generated by the ACS to<br>prevent replay attacks. | ACS | Length: Variable, 43–100 characters<br>JSON Data Type: String<br>Base64url-encoded<br>Example: a random 32-byte value that has<br>been Base64url-encoded gives a 43-character<br>string. | ARes = R |
| Challenge Information Text<br>Field Name:<br>challengeInfoText | Text provided by the ACS to be displayed<br>during the SPC authentication. | ACS | Length: Variable, maximum 350 characters<br>JSON Data Type: String | ARes = C<br>Required if<br>supported by<br>the SPC API |
| Currency<br>Field Name: currency | Transaction amount currency to be<br>displayed during the SPC authentication | ACS | Length: 3 characters, alphabetic<br>JSON Data Type: String<br>Values accepted:<br>• ISO 4217 three-character alphabetic<br>currency code, other than those listed in<br>Table A.5. | ARes = R |

---

<a id="page-372"></a>

## PDF page 372

| Data Element/Field Name | Description | Source | Length/Format/Values | Inclusion |
| --- | --- | --- | --- | --- |
| Display Name<br>Field Name: displayName | Card or product name (Payment Instrument)<br>to be displayed during the SPC<br>authentication. | ACS | Length: Variable, maximum 40 characters<br>JSON Data Type: String | ARes = R |
| Icon<br>Field Name: icon | Card image (Payment Instrument) URL or<br>Data URL to be displayed during the SPC<br>authentication. | ACS | Length: Variable, maximum 4096 characters<br>JSON Data Type: String<br>Values accepted:<br>• Fully Qualified URL or Data URL in<br>correct JSON object format<br>o Fully Qualified URL: Variable length,<br>maximum 2048 characters<br>o Data URL: Variable length, maximum<br>4096 characters. The Data URL<br>embeds the image in Base64-encoded<br>format. | ARes = R |

Issuer Image SPC

Issuer logo or Image URLs or Data URLs to be displayed during the SPC authentication.

ACS Length: Variable, maximum 90000 characters

ARes = C

Field Name: issuerImageSpc

JSON Data Type: JSON object

Required if supported by the SPC API

Includes at minimum the Default Image and at maximum the three Fully Qualified URLs or Data URLs defined as default, dark mode or monochrome images of the Issuer Image SPC.

Values accepted:

- Fully Qualified URL or Data URL in correct JSON object format o Fully Qualified URL: Variable length,

- Default Image

maximum 2048 characters o Data URL: Variable length, maximum

Field Name: default

30000 characters. The Data URL embeds the image in Base64-encoded format. Refer to RFC 2397.

- Dark Mode Image

Field Name: dark

If present, the Issuer Image SPC object should contain, at minimum, the Default Image.

- Monochrome Image

Field Name: monochrome

---

<a id="page-373"></a>

## PDF page 373

| Data Element/Field Name | Description | Source | Length/Format/Values | Inclusion |
| --- | --- | --- | --- | --- |
|  | Example Fully Qualified URL:<br>"issuerImageSpc":{<br>"default":"https://acs.com<br>/defaultspcimage.png"}<br>Example Data URL:<br>"issuerImageSpc":{<br>"default":"data:image/png;<br>base64,iVBORw0KGgoAA..." |  |  |  |
| Payee Name<br>Field Name: payeeName | The display name of the payee that this<br>SPC call is for (e.g. the Merchant).<br>Matches the Merchant Name from the AReq<br>message. | ACS | Length: Variable, maximum 40 characters<br>JSON Data Type: String | ARes = C<br>Required if<br>Payee Origin<br>is NOT<br>present |
| Payee Origin<br>Field Name: payeeOrigin | The origin of the payee that this SPC call is<br>for (e.g. the Merchant).<br>Matches the Payee Origin from the AReq<br>message. | ACS | Length: Variable, maximum 2048 characters<br>JSON Data Type: String<br>Value accepted:<br>• Fully Qualified URL | ARes = C<br>Required if<br>Payee Name<br>is NOT<br>present |

Payment System Image SPC

Payment System logo or Image URLs to be displayed during the SPC authentication.

ACS Length: Variable, maximum 90000 characters

ARes = C

Field Name: psImageSpc

JSON Data Type: JSON object

Required if supported by the SPC API

Includes at minimum the Default Image and at maximum the three Fully Qualified URLs defined as default, dark mode or monochrome images of the Payment System Image SPC.

Values accepted:

- Fully Qualified URL or Data URL in correct JSON object format o Fully Qualified URL: Variable length,

maximum 2048 characters

- Default Image

Field Name: default

---

<a id="page-374"></a>

## PDF page 374

| Data Element/Field Name | Description | Source | Length/Format/Values | Inclusion |
| --- | --- | --- | --- | --- |
|  | • Dark Mode Image<br>Field Name: dark<br>• Monochrome Image<br>Field Name: monochrome<br>Example Fully Qualified URL:<br>"psImageSpc":{<br>"default":"https://ds.com/defaul<br>tspcimage.png"}<br>Example Data URL:<br>"psImageSpc":{<br>"default":"data:image/png;<br>base64,c2RzYWRhc2Q..." |  | o Data URL: Variable length, maximum<br>30000 characters. The Data URL<br>embeds the image in Base64-encoded<br>format. Refer to RFC 2397.<br>If present, the Payment System Image SPC<br>object should contain, at minimum, the Default<br>Image. |  |
| Timeout<br>Field Name: timeout | The number of milliseconds before the<br>request to sign the transaction details times<br>out. | ACS | Length: Variable, 5–6 characters<br>JSON Data Type: String<br>Value accepted:<br>• Integer coded as a string in the range<br>60000–500000 | ARes = R |
| Value<br>Field Name: value | Transaction amount as a decimal value to<br>be displayed during the SPC authentication. | ACS | Length: Variable, maximum 40 characters<br>JSON Data Type: String | ARes = R |

---

<a id="page-375"></a>

## PDF page 375

| Data Element/Field Name | Description | Source | Length/Format/Values | Inclusion |
| --- | --- | --- | --- | --- |
| WebAuthn SPC Extension<br>Indicator<br>Field Name: extInd | For SPC and WebAuthn API enhancement. | ACS | Length: 1 character<br>JSON Data Type: String<br>Value accepted:<br>• Y = Extension requested<br>Only present if value = Y | ARes = O |

---

<a id="page-376"></a>

## PDF page 376

### A.22 HTTP Headers

Table A.29:  HTTP Headers

| Message | X-Request-ID | X-Response-ID |
| --- | --- | --- |
| AReq (3DS Server  DS) | 3DS Server Transaction ID |  |
| AReq (DS  ACS) | DS Transaction ID |  |
| ARes (ACS  DS) | DS Transaction ID | ACS Transaction ID |
| ARes (DS  3DS Server) | 3DS Server Transaction ID | DS Transaction ID |
| RReq (ACS  DS) | ACS Transaction ID |  |
| RReq (DS  3DS Server) | DS Transaction ID |  |
| RRes (3DS Server  DS) | DS Transaction ID | 3DS Server Transaction ID |
| RRes (DS  ACS) | ACS Transaction ID | DS Transaction ID |
| PReq (3DS Server  DS) | 3DS Server Transaction ID |  |
| PRes (DS  3DS Server) | 3DS Server Transaction ID | DS Transaction ID |
| OReq (DS  3DS Server or ACS) | DS Transaction ID |  |
| ORes (3DS Server or ACS  DS) | DS Transaction ID | 3DS Server Transaction ID or ACS Transaction ID |
| CReq (SDK  ACS) | SDK Transaction ID |  |
| CRes (ACS  SDK) | SDK Transaction ID | ACS Transaction ID |

HTTP Header Examples

- Request message:

X-Request-ID: d07c7b7f-a987-4401-a76a-b1ad60d07837

- Response message:

X-Request-ID: d07c7b7f-a987-4401-a76a-b1ad60d07837 X-Response-ID: 9fca3f1c-6178-4668-aed9-d5d3ff0b0d98