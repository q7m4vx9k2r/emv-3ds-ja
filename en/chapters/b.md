---
layout: default
title: "Message Format"
lang: en
---

# Message Format

[Home](../../index.md)

<a id="page-377"></a>

## PDF page 377

## Annex B

## Message Format

This annex provides the EMV 3-D Secure data elements and field names by Message Type. Refer to Table A.1 for data element specifications.

### B.1

### AReq Message Data Elements

Table A.1 outlines the default validation requirements for the AReq message. A specific DS may specify other DS validations or actions to meet requirements specific for that DS.

Table B.1:  AReq Data Elements

| Data Element | Field Name |
| --- | --- |
| 3DS Method Completion Indicator | threeDSCompInd |
| 3DS Method ID | threeDSMethodId |
| 3DS Requestor Authentication Indicator | threeDSRequestorAuthenticationInd |
| 3DS Requestor Authentication Information | threeDSRequestorAuthenticationInfo |
| 3DS Requestor Challenge Indicator | threeDSRequestorChallengeInd |
| 3DS Requestor Decoupled Max Time | threeDSRequestorDecMaxTime |
| 3DS Requestor Decoupled Request Indicator | threeDSRequestorDecReqInd |
| 3DS Requestor ID | threeDSRequestorID |
| 3DS Requestor Name | threeDSRequestorName |
| 3DS Requestor Prior Transaction<br>Authentication Information | threeDSRequestorPriorAuthenticationInfo |
| 3DS Requestor SPC Support | threeDSRequestorSpcSupport |
| 3DS Requestor URL | threeDSRequestorURL |
| 3DS Server Operator ID | threeDSServerOperatorID |
| 3DS Server Reference Number | threeDSServerRefNumber |
| 3DS Server Transaction ID | threeDSServerTransID |
| 3DS Server URL | threeDSServerURL |
| 3RI Indicator | threeRIInd |
| Accept Language | acceptLanguage |

---

<a id="page-378"></a>

## PDF page 378

| Data Element | Field Name |
| --- | --- |
| Account Type | acctType |
| Acquirer BIN | acquirerBIN |
| Acquirer Country Code | acquirerCountryCode |
| Acquirer Country Code Source | acquirerCountryCodeSource |
| Acquirer Merchant ID | acquirerMerchantID |
| Address Match Indicator | addrMatch |
| App IP Address | appIp |
| Broadcast Information | broadInfo |
| Browser Accept Headers | browserAcceptHeader |
| Browser IP Address | browserIP |
| Browser Java Enabled | browserJavaEnabled |
| Browser JavaScript Enabled | browserJavascriptEnabled |
| Browser Language | browserLanguage |
| Browser Screen Color Depth | browserColorDepth |
| Browser Screen Height | browserScreenHeight |
| Browser Screen Width | browserScreenWidth |
| Browser Time Zone | browserTZ |
| Browser User-Agent | browserUserAgent |
| Browser User Device ID | deviceId |
| Browser User ID | userId |
| Card Security Code | cardSecurityCode |
| Card Security Code Status | cardSecurityCodeStatus |
| Card Security Code Status Source | cardSecurityCodeStatusSource |
| Card/Token Expiry Date | cardExpiryDate |
| Cardholder Account Identifier | acctID |
| Cardholder Account Information | acctInfo |
| Cardholder Account Number | acctNumber |

---

<a id="page-379"></a>

## PDF page 379

| Data Element | Field Name |
| --- | --- |
| Cardholder Billing Address City | billAddrCity |
| Cardholder Billing Address Country | billAddrCountry |
| Cardholder Billing Address Line 1 | billAddrLine1 |
| Cardholder Billing Address Line 2 | billAddrLine2 |
| Cardholder Billing Address Line 3 | billAddrLine3 |
| Cardholder Billing Address Postal Code | billAddrPostCode |
| Cardholder Billing Address State | billAddrState |
| Cardholder Email Address | email |
| Cardholder Home Phone Number | homePhone |
| Cardholder Mobile Phone Number | mobilePhone |
| Cardholder Name | cardholderName |
| Cardholder Shipping Address City | shipAddrCity |
| Cardholder Shipping Address Country | shipAddrCountry |
| Cardholder Shipping Address Line 1 | shipAddrLine1 |
| Cardholder Shipping Address Line 2 | shipAddrLine2 |
| Cardholder Shipping Address Line 3 | shipAddrLine3 |
| Cardholder Shipping Address Postal Code | shipAddrPostCode |
| Cardholder Shipping Address State | shipAddrState |
| Cardholder Work Phone Number | workPhone |
| Default-SDK Type | defaultSdkType |
| Device Binding Status | deviceBindingStatus |
| Device Binding Status Source | deviceBindingStatusSource |
| Device Channel | deviceChannel |
| Device Information | deviceInfo |
| Device Rendering Options Supported | deviceRenderOptions |
| DS Reference Number | dsReferenceNumber |
| DS Transaction ID | dsTransID |

---

<a id="page-380"></a>

## PDF page 380

| Data Element | Field Name |
| --- | --- |
| DS URL | dsURL |
| EMV Payment Token Indicator | payTokenInd |
| EMV Payment Token Information | payTokenInfo |
| EMV Payment Token Source | payTokenSource |
| Instalment Payment Data | purchaseInstalData |
| Merchant Category Code | mcc |
| Merchant Country Code | merchantCountryCode |
| Merchant Name | merchantName |
| Merchant Risk Indicator | merchantRiskIndicator |
| Message Category | messageCategory |
| Message Extension | messageExtension |
| Message Type | messageType |
| Message Version Number | messageVersion |
| Multi-Transaction | multiTransaction |
| Notification URL | notificationURL |
| Payee Origin | payeeOrigin |
| Purchase Amount | purchaseAmount |
| Purchase Currency | purchaseCurrency |
| Purchase Currency Exponent | purchaseExponent |
| Purchase Date & Time | purchaseDate |
| Recurring Amount | recurringAmount |
| Recurring Currency | recurringCurrency |
| Recurring Currency Exponent | recurringExponent |
| Recurring Date | recurringDate |
| Recurring Expiry | recurringExpiry |
| Recurring Frequency | recurringFrequency |
| Recurring Indicator | recurringInd |

---

<a id="page-381"></a>

## PDF page 381

| Data Element | Field Name |
| --- | --- |
| SDK App ID | sdkAppID |
| SDK Encrypted Data | sdkEncData |
| SDK Ephemeral Public Key (Qc) | sdkEphemPubKey |
| SDK Maximum Timeout | sdkMaxTimeout |
| SDK Reference Number | sdkReferenceNumber |
| SDK Server Signed Content | sdkServerSignedContent |
| SDK Transaction ID | sdkTransID |
| SDK Type | sdkType |
| Seller Information | sellerInfo |
| SPC Incompletion Indicator | spcIncompInd |
| Split-SDK Type | splitSdkType |
| Tax ID | taxId |
| Transaction Type | transType |
| Trust List Status | trustListStatus |
| Trust List Status Source | trustListStatusSource |

---

<a id="page-382"></a>

## PDF page 382

### B.2

### ARes Message Data Elements

Table A.1 outlines the default validation requirements for the ARes message. A specific DS may specify other DS validations or actions to meet requirements specific for that DS.

Table B.2:  ARes Data Elements

| Data Element | Field Name |
| --- | --- |
| 3DS Requestor App URL Indicator | threeDSRequestorAppURLInd |
| 3DS Server Transaction ID | threeDSServerTransID |
| ACS Challenge Mandated Indicator | acsChallengeMandated |
| ACS Decoupled Confirmation Indicator | acsDecConInd |
| ACS Operator ID | acsOperatorID |
| ACS Reference Number | acsReferenceNumber |
| ACS Rendering Type | acsRenderingType |
| ACS Signed Content | acsSignedContent |
| ACS Transaction ID | acsTransID |
| ACS URL | acsURL |
| Authentication Method | authenticationMethod |
| Authentication Value | authenticationValue |
| Broadcast Information | broadInfo |
| Cardholder Information Text | cardholderInfo |
| Card Security Code Status Source | cardSecurityCodeStatusSource |
| Card Security Code Status | cardSecurityCodeStatus |
| Device Binding Status | deviceBindingStatus |
| Device Binding Status Source | deviceBindingStatusSource |
| Device Information Recognised Version | deviceInfoRecognisedVersion |
| DS Reference Number | dsReferenceNumber |
| DS Transaction ID | dsTransID |
| Electronic Commerce Indicator | eci |

---

<a id="page-383"></a>

## PDF page 383

| Data Element | Field Name |
| --- | --- |
| Message Extension | messageExtension |
| Message Type | messageType |
| Message Version Number | messageVersion |
| SDK Transaction ID | sdkTransID |
| SPC Transaction Data | spcTransData |
| Transaction Challenge Exemption | transChallengeExemption |
| Transaction Status | transStatus |
| Transaction Status Reason | transStatusReason |
| Transaction Status Reason Information | transStatusReasonInfo |
| Trust List Status | trustListStatus |
| Trust List Status Source | trustListStatusSource |
| WebAuthn Credential List | webAuthnCredList |

---

<a id="page-384"></a>

## PDF page 384

### B.3

### CReq Message Data Elements

Table A.1 outlines the default validation requirements for the CReq message.

Table B.3:  CReq Data Elements

| Data Element | Field Name |
| --- | --- |
| 3DS Requestor App URL | threeDSRequestorAppURL |
| 3DS Server Transaction ID | threeDSServerTransID |
| ACS Transaction ID | acsTransID |
| Challenge Additional Code | challengeAddCode |
| Challenge Cancelation Indicator | challengeCancel |
| Challenge Data Entry | challengeDataEntry |
| Challenge Data Entry 2 | challengeDataEntryTwo |
| Challenge HTML Data Entry | challengeHTMLDataEntry |
| Challenge No Entry | challengeNoEntry |
| Challenge Window Size | challengeWindowSize |
| Device Binding Data Entry | deviceBindingDataEntry |
| Information Continuation Indicator | infoContinueIndicator |
| Message Extension | messageExtension |
| Message Type | messageType |
| Message Version Number | messageVersion |
| OOB App Status | oobAppStatus |
| OOB App URL Indicator | oobAppURLInd |
| OOB Continuation Indicator | oobContinue |
| Resend Challenge Information Code | resendChallenge |
| SDK Counter SDK to ACS | sdkCounterStoA |
| SDK Transaction ID | sdkTransID |
| Trust List Data Entry | trustListDataEntry |

---

<a id="page-385"></a>

## PDF page 385

### B.4

### CRes Message Data Elements

Table A.1 outlines the default validation requirements for the CRes message.

Table B.4:  CRes Data Elements

| Data Element | Field Name |
| --- | --- |
| 3DS Server Transaction ID | threeDSServerTransID |
| ACS Counter ACS to SDK | acsCounterAtoS |
| ACS Transaction ID | acsTransID |
| ACS HTML | acsHTML |
| ACS UI Type | acsUiType |
| Challenge Additional Label | challengeAddLabel |
| Challenge Completion Indicator | challengeCompletionInd |
| Challenge Entry Box | challengeEntryBox |
| Challenge Entry Box 2 | challengeEntryBoxTwo |
| Challenge Information Header | challengeInfoHeader |
| Challenge Information Label | challengeInfoLabel |
| Challenge Information Text | challengeInfoText |
| Challenge Information Text Indicator | challengeInfoTextIndicator |
| Challenge Selection Information | challengeSelectInfo |
| Device Binding Information Text | deviceBindingInfoText |
| Expandable Information Label | expandInfoLabel |
| Expandable Information Text | expandInfoText |
| Information Continuation Label | infoContinueLabel |
| Issuer Image | issuerImage |
| Message Extension | messageExtension |
| Message Type | messageType |
| Message Version Number | messageVersion |
| OOB App Label | oobAppLabel |

---

<a id="page-386"></a>

## PDF page 386

| Data Element | Field Name |
| --- | --- |
| OOB App URL | oobAppURL |
| OOB Continuation Label | oobContinueLabel |
| Payment System Image | psImage |
| Resend Information Label | resendInformationLabel |
| SDK Transaction ID | sdkTransID |
| Submit Authentication Label | submitAuthenticationLabel |
| Toggle Position Indicator | togglePositionInd |
| Trust List Information Text | trustListInfoText |
| Why Information Label | whyInfoLabel |
| Why Information Text | whyInfoText |

### B.5

### Final CRes Message Data Elements

Table B.5 provides the data elements for the Final CRes message sent upon completion of the challenge from the ACS. Table A.1 outlines the default validation requirements for the CRes message.

Table B.5:  Final CRes Data Elements

| Data Element | Field Description |
| --- | --- |
| 3DS Server Transaction ID | threeDSServerTransID |
| ACS Counter ACS to SDK | acsCounterAtoS |
| ACS Transaction ID | acsTransID |
| Challenge Completion Indicator | challengeCompletionInd |
| Message Extension | messageExtension |
| Message Type | messageType |
| Message Version Number | messageVersion |
| SDK Transaction ID | sdkTransID |
| Transaction Status | transStatus |

---

<a id="page-387"></a>

## PDF page 387

### B.6

### PReq Message Data Elements

Table A.1 outlines the default validation requirements for the PReq message.

Table B.6:  PReq Data Elements

| Data Element | Field Name |
| --- | --- |
| 3DS Server Operator ID | threeDSServerOperatorID |
| 3DS Server Reference Number | threeDSServerRefNumber |
| 3DS Server Transaction ID | threeDSServerTransID |
| Card Range Data Download Indicator | cardRangeDataDownloadInd |
| Message Extension | messageExtension |
| Message Type | messageType |
| Message Version Number | messageVersion |
| Serial Number | serialNum |

---

<a id="page-388"></a>

## PDF page 388

### B.7

### PRes Message Data Elements

Table A.1 outlines the default validation requirements for the PRes message.

Table B.7:  PRes Data Elements

| Data Element | Field Name |
| --- | --- |
| 3DS Server Transaction ID | threeDSServerTransID |
| Card Range Data | cardRangeData |
| Card Range Data File URL | cardRangeDataFileURL |
| DS Protocol Versions | dsProtocolVersions |
| DS Transaction ID | dsTransID |
| DS URL List | dsUrlList |
| Message Extension | messageExtension |
| Message Type | messageType |
| Message Version Number | messageVersion |
| Read Order | readOrder |
| Serial Number | serialNum |

---

<a id="page-389"></a>

## PDF page 389

### B.8

### RReq Message Data Elements

Table A.1 outlines the default validation requirements for the RReq message.

Table B.8:  RReq Data Elements

| Data Element | Field Name |
| --- | --- |
| 3DS Server Transaction ID | threeDSServerTransID |
| ACS Rendering Type | acsRenderingType |
| ACS Transaction ID | acsTransID |
| Authentication Method | authenticationMethod |
| Authentication Value | authenticationValue |
| Cardholder Information Text | cardholderInfo |
| Challenge Cancelation Indicator | challengeCancel |
| Challenge Error Reporting | challengeErrorReporting |
| Device Binding Status | deviceBindingStatus |
| Device Binding Status Source | deviceBindingStatusSource |
| DS Transaction ID | dsTransID |
| Electronic Commerce Indicator | eci |
| Interaction Counter | interactionCounter |
| Message Category | messageCategory |
| Message Extension | messageExtension |
| Message Type | messageType |
| Message Version Number | messageVersion |
| SDK Transaction ID | sdkTransID |
| Transaction Status | transStatus |
| Transaction Status Reason | transStatusReason |
| Transaction Status Reason Information | transStatusReasonInfo |
| Trust List Status | trustListStatus |
| Trust List Status Source | trustListStatusSource |

---

<a id="page-390"></a>

## PDF page 390

### B.9

### RRes Message Data Elements

Table A.1 outlines the default validation requirements for the RRes message.

Table B.9:  RRes Data Elements

| Data Element | Field Name |
| --- | --- |
| 3DS Server Transaction ID | threeDSServerTransID |
| ACS Transaction ID | acsTransID |
| DS Transaction ID | dsTransID |
| Message Extension | messageExtension |
| Message Type | messageType |
| Message Version Number | messageVersion |
| Results Message Status | resultsStatus |
| SDK Transaction ID | sdkTransID |

---

<a id="page-391"></a>

## PDF page 391

### B.10 OReq Message Data Elements

Table A.1 outlines the default validation requirements for the OReq message.

Table B.10:  OReq Data Elements

| Data Element | Field Name |
| --- | --- |
| DS Reference Number | dsReferenceNumber |
| DS Transaction ID | dsTransID |
| Message Extension | messageExtension |
| Message Type | messageType |
| Message Version Number | messageVersion |
| Operation Category | opCategory |
| Operation Description | opDescription |
| Operation Expiration Date | opExpDate |
| Operation Prior Transaction Reference | opPriorTransRef |
| Operation Sequence | opSeq |
| Operation Severity | opSeverity |

---

<a id="page-392"></a>

## PDF page 392

### B.11 ORes Message Data Elements

Table A.1 outlines the default validation requirements for the ORes message.

Table B.11:  ORes Data Elements

| Data Element | Field Name |
| --- | --- |
| 3DS Server Reference Number | threeDSServerRefNumber |
| 3DS Server Transaction ID | threeDSServerTransID |
| ACS Reference Number | acsReferenceNumber |
| ACS Transaction ID | acsTransID |
| DS Transaction ID | dsTransID |
| Message Extension | messageExtension |
| Message Type | messageType |
| Message Version Number | messageVersion |
| Operation Message Status | opStatus |

---

<a id="page-393"></a>

## PDF page 393

### B.12 Error Message Data Elements

Table A.4 provides detailed information including Error Code values.

Table B.12:  Error Message Data Elements

| Data Element | Field Name |
| --- | --- |
| 3DS Server Transaction ID | threeDSServerTransID |
| ACS Transaction ID | acsTransID |
| DS Transaction ID | dsTransID |
| Error Code | errorCode |
| Error Component | errorComponent |
| Error Description | errorDescription |
| Error Detail | errorDetail |
| Error Message Type | errorMessageType |
| Message Type | messageType |
| Message Version Number | messageVersion |
| SDK Transaction ID | sdkTransID |