---
layout: default
title: "附属書A：3-D Secureデータ要素（翻訳途中）"
lang: ja
---

# 附属書A：3-D Secureデータ要素

> 非公式の日本語参考訳。185–216ページを翻訳済み。217–376ページは未翻訳です。

[目次](../../index.md) · [英語原文](../../en/chapters/a.md)

<a id="page-185"></a>

## 原本 185ページ

## 附属書A
## 3-D Secureデータ要素

本附属書は、すべてのEMV 3-D Secureデータ要素をアルファベット順に列挙する。データ要素の情報と、その情報を示す表記規則は次のとおり。

- **データ要素名**：データ要素を識別する名称。
- **フィールド名**：データ要素のフィールド名。
- **説明**：データ要素の目的と、該当する場合は追加の詳細。
- **提供元**：メッセージ内のデータ要素を提供する責任を持つ3-D Secureコンポーネント。
- **長さ／形式／値**：値の長さ、JSONデータ形式、および該当する場合はデータ要素に対応する値。長さの検証基準でいう「文字」はUTF-8の1文字を指す。JSONオブジェクトの長さは、オブジェクトを表す文字列全体の文字数である。
- **デバイスチャネル**：個々の取引で使用するデバイスチャネルに応じて、メッセージにデータ要素を含めることを示す。チャネル種別の表記は次のとおり。
  - `01-APP`：アプリベース認証。
  - `02-BRW`：ブラウザベース認証。
  - `03-3RI`：デバイスを使用しない決済認証／アカウント検証。
- **メッセージカテゴリ**：取引の種類に応じて、メッセージにデータ要素を含めることを示す。認証種別の表記は次のとおり。
  - `01-PA`：決済認証。
  - `02-NPA`：非決済認証。
- **メッセージへの包含**：データ要素を含めるメッセージ種別と、両メッセージカテゴリについて、その包含が必須・任意・条件付きのいずれであるかを示す。表A.1で明示的に別の定めがない限り、ある取引のデバイスチャネルおよびメッセージカテゴリでフィールドが必須である場合、値が存在し、空またはnullであってはならない。

---

<a id="page-186"></a>

## 原本 186ページ

包含区分は次の表記で示す。

- **R = Required（必須）**：送信側は、指定されたメッセージ種別・デバイスチャネル・メッセージカテゴリにデータ要素を含めなければならない。受信側はデータ要素の存在を確認し、その内容を検証しなければならない。
- **C = Conditional（条件付き）**：送信側は、条件付き包含の要件を満たす場合、指定されたメッセージ種別にデータ要素を含めなければならない。受信側は存在を確認し、内容を検証しなければならない。任意のデータ要素に送信するデータがない場合、その要素は含めないことが望ましい。これには、メッセージ内容に基づいて必須にならない条件付きデータ要素も含む。
- **O = Optional（任意）**：送信側は、指定されたメッセージ種別にデータ要素を含めてもよい。受信側は、存在する場合、その内容を検証しなければならない。任意のデータ要素に送信するデータがない場合、その要素は含めないことが望ましい。これには、メッセージ内容に基づいて必須にならない条件付きデータ要素も含む。

**条件付き包含**：該当するメッセージ種別にデータ要素を含める条件を示す。提供元コンポーネントがその条件を満たす責任を持つ。

例：

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Requestor URL<br>`threeDSRequestorURL` | 3DS RequestorのWebサイトまたはカスタマーケアサイトの完全修飾URL。問題が発生した場合に、受信側3-D Secureシステムへ追加情報を提供する。連絡先情報を提供することが望ましい。 | 3DS Server | 可変長、最大2048文字。JSON：String。値：完全修飾URL。例：`https://server.domainname.com` | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R | — |

上記の例では、3DS Requestor URLは3DS Serverが提供し、アプリベース認証とブラウザベース認証の両方で、Authentication Request（AReq）メッセージに使用される。

---

<a id="page-187"></a>

## 原本 187ページ

### A.1 必須フィールドの欠落

次のいずれかの場合、データフィールドは欠落している。

- 名前／値のペアが存在しない。
- フィールド名は存在するが、値が空またはnullである。

明示的な別の定めがない限り、必須フィールドが欠落している場合、受信側コンポーネントはA.9節で定義するError Messageを、該当するError Componentおよび`Error Code = 201`で返す。これは、常に必須のフィールドにも、条件付きで必須となるフィールドにも適用される。

### A.2 フィールドの検証基準

指定された検証のみを実施する。本附属書の表に記載されていない検証に基づいて、メッセージを拒否してはならない。フィールドが存在しても、その値が表A.1の検証基準に適合しない場合、受信側コンポーネントはA.9節で定義するError Messageを、該当するError Componentおよび`Error Code = 203`で返す。

### A.3 AReqデータの暗号化

AReqメッセージには、暗号化せずに含めるフィールドがある。これらは6.1節で定義するセキュアなリンクにより、転送中に保護される。これに加えて、Device Informationデータ要素は3DS SDKが暗号化し、DSへのメッセージに含める前に3DS Serverへ渡す。

暗号化対象のすべてのデータは、3DS SDK Encrypted Dataフィールド内のJWEオブジェクトとして、1つの暗号化データブロックで送信する。JWEオブジェクトを構成フィールドに分解する前に処理するのは、3DS SDKとDSのみである。復号結果は、ACSへ送るAReqメッセージのDevice Informationデータ要素に、暗号化せずに格納する。

---

<a id="page-188"></a>

## 原本 188ページ

### A.4 EMV 3-D Secureデータ要素

**表A.1：EMV 3-D Secureデータ要素**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Method完了指標<br>`threeDSCompInd` | 3DS Methodが正常に完了したかどうかを示す。 | 3DS Server | 1文字。JSON：String。`Y` = 正常に完了。`N` = 実行されなかった、または正常に完了しなかった。`U` = 利用不可。Cardholder Account Numberに対応するカード範囲のPResメッセージデータに、3DS Method URLが存在しなかった。 | 02-BRW | 01-PA<br>02-NPA | AReq = R | — |
| 3DS Method ID<br>`threeDSMethodId` | 前回の3DS Method実行時に使用した3DS Server Transaction IDを含む。 | 3DS Server | 36文字。JSON：String。IETF RFC 4122で定義する正規形式。出力が指定要件を満たす場合、同RFCで指定するどのバージョンを使用してもよい。 | 02-BRW | 01-PA<br>02-NPA | AReq = C | 3DS Requestorが前回の3DS Methodの実行を再利用する場合に必須。 |

---

<a id="page-189"></a>

## 原本 189ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Requestor App URL<br>`threeDSRequestorAppURL` | OOB認証後にAuthentication Appから3DS Requestor Appを呼び出せるよう、3DS Requestor AppがCReqメッセージ内で自身のURLを宣言する。注：このURLを提供する場合、3DS RequestorはOSにURLを適切に登録する必要がある。 | 3DS SDK | 可変長、最大2048文字。JSON：String。値：Universal App Link。例：`https://appname.com`。Universal App Linkの定義は表1.3を参照。 | 01-APP | 01-PA<br>02-NPA | CReq = C | 3DS SDKが3DS Requestor App URLを提供する場合、すべてのCReqメッセージで必須。 |
| 3DS Requestor App URL指標<br>`threeDSRequestorAppURLInd` | チャレンジ中にACSが使用するOOB Authentication Appが、3DS Requestor App URLに対応しているかを示す。 | ACS | 1文字。JSON：String。`Y` = OOB Authentication Appが3DS Requestor App URLに対応。`N` = 対応していない。 | 01-APP | 01-PA<br>02-NPA | ARes = R | — |
| 3DS Requestor認証指標（次ページへ続く） | 認証要求の種類を示す。 | 3DS Server | 2文字。JSON：String。`01` = 決済取引。`02` = 継続取引。 | 01-APP<br>02-BRW | 01-PA<br>02-NPA | AReq = R | — |

---

<a id="page-190"></a>

## 原本 190ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Requestor認証指標（前ページの続き）<br>`threeDSRequestorAuthenticationInd` | ACSが認証要求の処理に最適な方法を判断するための追加情報を提供する。 | 前ページ参照 | `03` = 分割払い取引。`04` = カード追加。`05` = カードの管理。`06` = EMVトークンのID&Vの一環としてのカード会員検証。`07` = 請求契約（Billing Agreement）。`08` = 分割配送。`09` = 遅延配送。`10` = 分割決済。`11–79` = EMVCoの将来用途のため予約済み（EMVCoが定義するまで無効）。`80–99` = DS用途のため予約済み。 | 前ページ参照 | 前ページ参照 | 前ページ参照 | — |
| 3DS Requestor認証情報<br>`threeDSRequestorAuthenticationInfo` | 取引の前または取引中に、3DS Requestorがカード会員をどのように認証したかに関する情報。 | 3DS Server<br>DS | 要素数：1–3。JSON：Array of objects。含めるデータ要素は表A.12を参照。注：メッセージの当フィールドに格納する前に、JSONオブジェクトの配列に整形する。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O | 任意。含めることを推奨。 |
| 3DS Requestorチャレンジ指標（次ページへ続く） | この取引でチャレンジを要求するかを示す。 | 3DS Server<br>DS | 要素数：1–2。JSON：Array of string。各文字列は2文字。原文の「Example:」に続く例は記載されていない。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O | — |

---

<a id="page-191"></a>

## 原本 191ページ

**表A.1（続き）：3DS Requestorチャレンジ指標**

フィールド名：`threeDSRequestorChallengeInd`。提供元、形式、チャネル、カテゴリ、包含区分は前ページ参照。

`01-PA`では、3DS Requestorが取引に懸念を持ち、チャレンジを要求する場合がある。`02-NPA`では、ウォレットに新しいカードを追加する際にチャレンジが必要となる場合がある。

注：2つの希望を提供する場合、3DS Requestorは希望順に並べ、相互に矛盾しないことを保証する。原文の例は`02`（チャレンジを要求しない）と`04`（チャレンジを要求する：必須）である。

| 値 | 意味 |
| --- | --- |
| 01 | 希望なし |
| 02 | チャレンジを要求しない |
| 03 | チャレンジを要求する（3DS Requestorの希望） |
| 04 | チャレンジを要求する（必須） |
| 05 | チャレンジを要求しない（取引リスク分析を実施済み） |
| 06 | チャレンジを要求しない（データ共有のみ） |
| 07 | チャレンジを要求しない（強固な顧客認証を実施済み） |
| 08 | チャレンジを要求しない（チャレンジ不要の場合、Trust List免除を使用） |
| 09 | チャレンジを要求する（チャレンジが必要な場合、Trust Listのプロンプトを要求） |
| 10 | チャレンジを要求しない（少額決済免除を使用） |
| 11 | チャレンジを要求しない（安全な法人決済の免除） |

---

<a id="page-192"></a>

## 原本 192ページ

**表A.1（続き）**

3DS Requestorチャレンジ指標の許容値（続き）：

| 値 | 意味 |
| --- | --- |
| 12 | チャレンジを要求する（チャレンジが必要な場合、Device Bindingのプロンプトを要求） |
| 13 | チャレンジを要求する（イシュアの要求） |
| 14 | チャレンジを要求する（加盟店起点の取引） |
| 15–79 | EMVCoの将来用途のため予約済み（EMVCoが定義するまで無効） |
| 80–99 | DS用途のため予約済み |

注：この要素が提供されない場合、ACSは`01`（希望なし）として解釈することが想定される。

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Requestor分離認証の最大待機時間<br>`threeDSRequestorDecMaxTime` | 分離認証（Decoupled Authentication）取引の結果をACSが提供するまで、3DS Requestorが待機する最大時間を分単位で示す。 | 3DS Server | 5文字。JSON：String。`00001`から`10080`までの数値。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | 3DS Requestor Decoupled Request Indicatorが`Y`、`F`または`B`の場合に必須。 |

---

<a id="page-193"></a>

## 原本 193ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Requestor分離認証要求指標<br>`threeDSRequestorDecReqInd` | 3DS RequestorがACSに分離認証の使用を要求するか、およびACSがその使用を確認した場合に分離認証の使用に同意するかを示す。注：この要素が提供されない場合、ACSは`N`（分離認証を使用しない）と解釈することが想定される。 | 3DS Server | 1文字。JSON：String。許容値は下表。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O | — |

| 値 | 意味 |
| --- | --- |
| Y | 分離認証に対応しており、チャレンジが必要な場合は主たるチャレンジ方式として優先する（AResのTransaction Status = D）。 |
| N | 分離認証を使用しない。 |
| F | 分離認証に対応しており、チャレンジが必要な場合はフォールバックのチャレンジ方式としてのみ使用する（RReqのTransaction Status = D）。 |
| B | 分離認証に対応しており、チャレンジが必要な場合は主たる方式またはフォールバック方式として使用できる（AResまたはRReqのTransaction Status = D）。 |

---

<a id="page-194"></a>

## 原本 194ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Requestor ID<br>`threeDSRequestorID` | DSが定義する3DS Requestorの識別子。 | 3DS Server | 可変長、最大35文字。JSON：String。個々のDSは、このフィールドの内容に対して、特定の形式・文字・その他の要件を課してもよい。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R | — |
| 3DS Requestor名<br>`threeDSRequestorName` | DSが定義する3DS Requestorの名称。 | 3DS Server | 可変長、最大40文字。JSON：String。個々のDSは、このフィールドの内容に対して、特定の形式・文字・その他の要件を課してもよい。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R | — |
| 3DS Requestor過去取引の認証情報<br>`threeDSRequestorPriorAuthenticationInfo` | 過去の3DS取引の一環として、3DS Requestorがカード会員をどのように認証したかに関する情報。 | 3DS Server | 要素数：可変、1–3。JSON：Array of objects。含めるデータ要素は表A.13を参照。注：メッセージの当フィールドに格納する前にJSONオブジェクトに整形する（原文表記）。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | 分離認証フォールバックの場合の3RI、またはSPCの場合に必須。 |

> 訳注：最後の行ではJSON型を「Array of objects」とする一方、原文の注には「JSON object」と記載されています。原文の両方の表記を保持しました。

---

<a id="page-195"></a>

## 原本 195ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS RequestorのSPC対応<br>`threeDSRequestorSpcSupport` | 3DS RequestorがSPC認証に対応しているかを示す。注：存在する場合、このフィールドには値`Y`が入る。 | 3DS Server | JSON：String。許容値：`Y` = 対応。 | 02-BRW | 01-PA<br>02-NPA | AReq = C | 3DS Requestorが対応している場合に必須。 |
| 3DS Requestor URL<br>`threeDSRequestorURL` | 3DS RequestorのWebサイトまたはカスタマーケアサイトの完全修飾URL。問題発生時に受信側3-D Secureシステムへ追加情報を提供する。連絡先情報を提供することが望ましい。 | 3DS Server | 可変長、最大2048文字。JSON：String。値：完全修飾URL。例：`https://server.domainname.com` | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R | — |
| 3DS Server Operator ID<br>`threeDSServerOperatorID` | DSが割り当てる3DS Serverの識別子。各DSは、個々の3DS Serverに対して独自のIDを個別に提供できる。 | 3DS Server | 可変長、最大32文字。JSON：String。個々のDSは、このフィールドの内容に特定の形式・文字の要件を課してもよい。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C<br>PReq = C | フィールドの存在に関する要件はDSごとに定める。 |

---

<a id="page-196"></a>

## 原本 196ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Server Reference Number<br>`threeDSServerRefNumber` | 試験および承認時にEMVCo事務局が割り当てる一意の識別子。 | 3DS Server | 可変長、最大32文字。JSON：String。値はEMVCo事務局が設定する。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R<br>PReq = R<br>ORes = C | OReqメッセージを受信する3DS ServerのOResメッセージで必須。 |
| 3DS Server Transaction ID<br>`threeDSServerTransID` | 単一の取引を識別するために3DS Serverが割り当てる、全世界で一意の取引識別子。 | 3DS Server | 36文字。JSON：String。IETF RFC 4122で定義する正規形式。出力が指定要件を満たす場合、同RFCで指定するどのバージョンを使用してもよい。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R<br>ARes = R<br>CReq = R<br>CRes = R<br>ORes = C<br>PReq = R<br>PRes = R<br>RReq = R<br>RRes = R<br>Erro = C | 利用可能な場合（例：メッセージから取得できる場合、または生成中の場合）、Error Messageで必須。OReqメッセージを受信する3DS ServerのOResメッセージで必須。 |

---

<a id="page-197"></a>

## 原本 197ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3DS Server URL<br>`threeDSServerURL` | チャレンジ完了後、DSがRReqメッセージを送る3DS Serverの完全修飾URL。形式が正しくない場合、RReqメッセージによる取引結果の配信に失敗する。 | 3DS Server | 可変長、最大2048文字。JSON：String。値：完全修飾URL。例：`https://server.adomainname.net` | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R | — |
| 3RI指標<br>`threeRIInd` | 3RI要求の種類を示す。ACSが3RI要求の処理に最適な方法を判断するための追加情報を提供する。 | 3DS Server | 2文字。JSON：String。許容値は下表および次ページ。 | 03-3RI | 01-PA<br>02-NPA | AReq = R | — |

| 値 | 意味 |
| --- | --- |
| 01 | 継続取引 |
| 02 | 分割払い取引 |
| 03 | カード追加 |
| 04 | カード情報の管理 |
| 05 | アカウント検証 |
| 06 | 分割配送 |
| 07 | チャージ（Top-up） |
| 08 | 郵便注文 |
| 09 | 電話注文 |
| 10 | Trust Listの状態確認 |
| 11 | その他の決済 |
| 12 | 請求契約（Billing Agreement） |
| 13 | Device Bindingの状態確認 |

---

<a id="page-198"></a>

## 原本 198ページ

**表A.1（続き）**

3RI指標の許容値（続き）：

| 値 | 意味 |
| --- | --- |
| 14 | Card Security Codeの状態確認 |
| 15 | 遅延配送 |
| 16 | 分割決済 |
| 17 | FIDO認証情報の削除 |
| 18 | FIDO認証情報の登録 |
| 19 | 分離認証フォールバック |
| 20–79 | EMVCoの将来用途のため予約済み（EMVCoが定義するまで無効） |
| 80–99 | DS用途のため予約済み |

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Accept Language<br>`acceptLanguage` | IETF BCP 47で定義される、HTTPヘッダーに含まれるブラウザの言語設定を表す値。 | 3DS Server | 要素数：可変、1–99。JSON：Array of string。各文字列は可変長、最大100文字。 | 02-BRW | 01-PA<br>02-NPA | AReq = R | — |

---

<a id="page-199"></a>

## 原本 199ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| アカウント種別<br>`acctType` | アカウントの種類を示す。例：複数のアカウントを持つカード商品。 | 3DS Server | 2文字。JSON：String。`01` = 該当なし。`02` = クレジット。`03` = デビット。`04–79` = EMVCoの将来用途のため予約済み（EMVCoが定義するまで無効）。`80–99` = DSまたは決済システム固有。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = C | 購入前に3DS Requestorがカード会員へ使用するアカウント種別を尋ねる場合に必須。一部市場（例：ブラジルの加盟店）で必須。それ以外は任意。 |
| アクワイアラBIN<br>`acquirerBIN` | AReqメッセージを受信するDSが割り当てる、アクワイアリング機関の識別コード。 | 3DS Server | 可変長、最大11文字。JSON：String。各決済システムが定義するAcquirer BINに対応する値。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | 01-PA：AReq = R<br>02-NPA：AReq = O | — |

---

<a id="page-200"></a>

## 原本 200ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| アクワイアラ国コード<br>`acquirerCountryCode` | アクワイアリング機関が所在する国のコード（ISO 3166-1に準拠）。DSは3DS Serverが提供した値を変更してもよい。 | 3DS Server<br>DS | 3文字。JSON：String。表A.5に列挙する例外を除く、ISO 3166-1の数字3桁の国コード。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R | — |
| アクワイアラ国コードの設定元<br>`acquirerCountryCodeSource` | Acquirer Country Codeを設定するシステムがこのデータ要素を設定する。DSは3DS Serverが提供した値を変更してもよい。 | 3DS Server<br>DS | 2文字。JSON：String。`01` = 3DS Server。`02` = DS。`03–79` = EMVCoの将来用途のため予約済み（EMVCoが定義するまで無効）。`80–99` = DS用途のため予約済み。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = R | — |
| アクワイアラ加盟店ID<br>`acquirerMerchantID` | アクワイアラが割り当てる加盟店識別子。3DS Requestorの代理で送信するオーソリゼーション要求で使用する値と同じ場合があり、ISO 8583-1の形式要件で表現される。 | 3DS Server | 可変長、最大35文字。JSON：String。個々のDSは、このフィールドの内容に特定の形式・文字の要件を課してもよい。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | 01-PA：AReq = R<br>02-NPA：AReq = O | — |

---

<a id="page-201"></a>

## 原本 201ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACSチャレンジ必須指標<br>`acsChallengeMandated` | 国・地域の義務付けやその他の要因により、取引を承認するためにチャレンジが必要かを示す。 | ACS | 1文字。JSON：String。`Y` = チャレンジが義務付けられる。`N` = 義務付けられない。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = C | Transaction Statusが`C`または`D`の場合に必須。 |
| ACSからSDKへのカウンタ<br>`acsCounterAtoS` | ACSから3DS SDKへのセキュアチャネルで、セキュリティ対策として使用するカウンタ。注：バイトに相当する10進数値を数値文字列として符号化したもの。 | ACS | 3文字。JSON：String。許容値：`000–255`。 | 01-APP | 01-PA<br>02-NPA | CRes = R | — |
| ACS分離認証確認指標<br>`acsDecConInd` | ACSが分離認証（Decoupled Authentication）の使用を確認し、カード会員の認証にその方式を使用することに同意するかを示す。 | ACS | 1文字。JSON：String。`Y` = 分離認証を使用することを確認。`N` = 分離認証を使用しない。注：3DS Requestor Decoupled Request Indicatorが`N`の場合、このフィールドに`Y`を返すことはできない。Transaction Statusが`D`の場合、値`N`は無効。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = C | Transaction Status = Dの場合に必須。 |

---

<a id="page-202"></a>

## 原本 202ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS一時公開鍵（QT）<br>`acsEphemPubKey` | ACSが生成する一時鍵ペアの公開鍵成分。3DS SDKとACSの間のセッション鍵を確立するために使用する。詳細は6.2.3.2節参照。 | ACS | 可変長、最大256文字。JSON：Object。 | 01-APP | 01-PA<br>02-NPA | ACS Signed Content参照 | ACS Signed Content参照。 |
| ACS HTML<br>`acsHTML` | ACSがCResメッセージ内で提供するHTML。カード会員へのチャレンジ中にACS UI TypeでHTMLが指定された場合に使用する。 | ACS | 可変長、最大300000文字。JSON：String。値：Base64url符号化されたHTML。CResメッセージに格納する前に、この値をBase64url符号化する。 | 01-APP | 01-PA<br>02-NPA | CRes = C | ACS UI Typeが`05`または`06`の場合に必須。 |
| ACS Operator ID<br>`acsOperatorID` | DSが割り当てるACS識別子。各DSは、個々のACSに対して独自のIDを個別に提供できる。 | ACS | 可変長、最大32文字。JSON：String。個々のDSは、このフィールドの内容に特定の形式・文字の要件を課してもよい。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = C | フィールドの存在に関する要件はDSごとに定める。 |

---

<a id="page-203"></a>

## 原本 203ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS Reference Number<br>`acsReferenceNumber` | 試験および承認時にEMVCo事務局が割り当てる一意の識別子。 | ACS | 可変長、最大32文字。JSON：String。値はEMVCo事務局が設定する。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = R<br>ORes = C | OReqメッセージを受信するACSのOResメッセージで必須。 |
| ACS表示方式<br>`acsRenderingType` | ACSが最初に利用者へ提示するACS InterfaceとACS UI Templateを識別する。 | ACS | JSON：Object。含めるデータ要素は表A.14を参照。注：メッセージの`acsRenderingType`フィールドに格納する前に、データをJSONオブジェクトに整形する。 | 01-APP | 01-PA<br>02-NPA | ARes = C<br>RReq = C | AResではTransaction Status = Cの場合に必須。RReqでは、ACS Decoupled Confirmation Indicator = Yの場合を除き必須。 |

---

<a id="page-204"></a>

## 原本 204ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS署名済みコンテンツ<br>`acsSignedContent` | ACSがAResメッセージ用に作成するJWSオブジェクトを、文字列として含む。詳細は6.2.3.2節参照。 | ACS | 可変長、最大16000文字。JSON：String。文字列として表現するJWSオブジェクトの本体には、表A.1で定義する次のデータ要素を含む：ACS URL、ACS Ephemeral Public Key（QT）、SDK Ephemeral Public Key（QC）。 | 01-APP | 01-PA<br>02-NPA | ARes = C | Transaction Status = Cの場合に必須。 |

---

<a id="page-205"></a>

## 原本 205ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS Transaction ID<br>`acsTransID` | 単一の取引を識別するためにACSが割り当てる、全世界で一意の取引識別子。 | ACS | 36文字。JSON：String。IETF RFC 4122で定義する正規形式。出力が指定要件を満たす場合、同RFCで指定するどのバージョンを使用してもよい。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = R<br>CReq = R<br>CRes = R<br>ORes = C<br>RReq = R<br>RRes = R<br>Erro = C | 利用可能な場合（例：メッセージから取得できる場合、または生成中の場合）、Error Messageで必須。OReqメッセージを受信するACSのOResメッセージで必須。 |

---

<a id="page-206"></a>

## 原本 206ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS UI Type<br>`acsUiType` | 3DS SDKが描画するユーザーインターフェースの種類。個々のデータマッピングと要件を含む。 | ACS | 2文字。JSON：String。許容値は下表。 | 01-APP | 01-PA<br>02-NPA | CRes = C | 最終CResメッセージを除いて必須。 |

| 値 | 意味 |
| --- | --- |
| 01 | テキスト |
| 02 | 単一選択 |
| 03 | 複数選択 |
| 04 | OOB |
| 05 | HTML |
| 06 | HTML OOB |
| 07 | 情報表示 |
| 08–79 | EMVCoの将来用途のため予約済み（EMVCoが定義するまで無効） |
| 80–99 | DS用途のため予約済み |

---

<a id="page-207"></a>

## 原本 207ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACS URL<br>`acsURL` | チャレンジに使用するACSの完全修飾URL。`01-APP`：3DS SDKがこのURLへChallenge Requestを送る。`02-BRW`：3DS Requestorがチャレンジiframeを通じてこのURLへCReqをPOSTする。アプリ方式ではACS Signed ContentのJWSオブジェクト内に含む。ブラウザ方式では、このデータ要素は独立したオブジェクトとして存在する。 | ACS | 可変長、最大2048文字。JSON：String。値：完全修飾URL。例：`https://server.acsdomainname.com` | 01-APP<br>02-BRW | 01-PA<br>02-NPA | 01-APP：ACS Signed Content参照<br>02-BRW：ARes = C | 01-APP：ACS Signed Content参照。02-BRW：Transaction Status = Cの場合に必須。 |
| 住所一致指標<br>`addrMatch` | カード会員の配送先住所と請求先住所が同じかを示す。 | 3DS Server | 1文字。JSON：String。`Y` = 配送先住所と請求先住所が一致。`N` = 一致しない。 | 01-APP<br>02-BRW | 01-PA<br>02-NPA | AReq = O | — |

---

<a id="page-208"></a>

## 原本 208ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| アプリIPアドレス<br>`appIp` | 3DS Requestor Appが3DS Requestor環境へ接続する際に使用する外部IPアドレス（デバイスのパブリックIPアドレス）。 | 3DS Server | 可変長、最大45文字。JSON：String。値：IPv4アドレス（RFC 791参照）、またはIPv6アドレス（RFC 4291参照）。 | 01-APP | 01-PA<br>02-NPA | AReq = C | 市場または地域の規則により、この情報の送信が制限される場合を除き必須。 |
| 認証方式（次ページへ続く）<br>`authenticationMethod` | AResでは、イシュアがカード会員へのチャレンジに使用する認証種別の一覧を示す。RReqでは、ACSが使用した認証種別の一覧を示す。 | ACS | 要素数：可変、1–99。JSON：Array of string。各文字列は2文字。許容値は下表と次ページ。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = C<br>RReq = C | AResではTransaction Statusが`C`または`D`の場合に必須。RReqではTransaction Statusが`Y`または`N`の場合に必須。注：03-3RIでは、分離認証の場合にのみ存在する。 |

| 値 | 意味 |
| --- | --- |
| 01 | 固定パスコード |
| 02 | SMS OTP |
| 03 | キーフォブまたはEMVカードリーダーのOTP |
| 04 | アプリOTP |
| 05 | その他のOTP |
| 06 | KBA（知識に基づく認証） |
| 07 | OOB生体認証 |
| 08 | OOBログイン |
| 09 | その他のOOB |
| 10 | その他 |
| 11 | プッシュ確認 |
| 12 | 分離認証 |

---

<a id="page-209"></a>

## 原本 209ページ

**表A.1（続き）：認証方式**

前ページの`authenticationMethod`の許容値の続き。

| 値 | 意味 |
| --- | --- |
| 13 | WebAuthn |
| 14 | SPC |
| 15 | 行動的生体認証 |
| 16 | 電子ID |
| 17–79 | EMVCoの将来用途のため予約済み（EMVCoが定義するまで無効） |
| 80–99 | DS用途のため予約済み |

SDK Type = 02、かつSplit-SDK Type/Limited Indicator = Yの場合、値`01`または`06`は無効。

---

<a id="page-210"></a>

## 原本 210ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 認証値<br>`authenticationValue` | 決済システムが定義するアルゴリズムを使用してACSまたはDSが提供する、決済システム固有の値。認証の証拠を提供するために使用してもよい。 | ACS<br>DS | 可変長、最大4000文字。実際の長さは決済システムの規則で定義する。JSON：String。例：20-byteの値をBase64符号化して、28-byteの結果を得る。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | ARes = C<br>RReq = C | 01-PA：Transaction Statusが`Y`または`A`の場合に必須。Transaction Status = Iの場合、DS規則に基づく条件付き。中断通知として送るRReqメッセージでは省略する。02-NPA：DS規則に基づく条件付き。 |
| ブロードキャスト情報<br>`broadInfo` | 3DS Server、DS、ACSの間で送信する構造化情報。 | 3DS Server<br>DS<br>ACS | 可変長、最大4096文字。JSON：Object。含めるデータ要素は表A.27を参照。 | 01-APP<br>02-BRW<br>03-3RI | 01-PA<br>02-NPA | AReq = O<br>ARes = O | — |

---

<a id="page-211"></a>

## 原本 211ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ブラウザAcceptヘッダー<br>`browserAcceptHeader` | カード会員のブラウザから3DS Requestorに送られたHTTP acceptヘッダーの正確な内容。 | 3DS Server | 可変長、最大2048文字。JSON：String。ブラウザが送信したacceptヘッダー全体の長さが2048文字を超える場合、3DS Serverは超過部分を切り捨てる。詳細はA.6節参照。 | 02-BRW | 01-PA<br>02-NPA | AReq = R | — |
| ブラウザIPアドレス<br>`browserIP` | HTTPヘッダーによって3DS Requestorに返されるブラウザのIPアドレス。 | 3DS Server | 可変長、最大45文字。JSON：String。値：IPv4アドレス（RFC 791参照）、またはIPv6アドレス（RFC 4291参照）。 | 02-BRW | 01-PA<br>02-NPA | AReq = C | 市場または地域の規則により、この情報の送信が制限される場合を除き必須。 |

---

<a id="page-212"></a>

## 原本 212ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ブラウザのJava有効化<br>`browserJavaEnabled` | カード会員のブラウザがJavaを実行できるかを表す真偽値。値は`navigator.javaEnabled`プロパティから返される。詳細はA.6節参照。 | 3DS Server | JSON：Boolean。許容値：`true`、`false`。 | 02-BRW | 01-PA<br>02-NPA | AReq = C | Browser JavaScript Enabled = trueの場合に必須。それ以外は任意。 |
| ブラウザのJavaScript有効化<br>`browserJavascriptEnabled` | カード会員のブラウザがJavaScriptを実行できるかを表す真偽値。詳細はA.6節参照。 | 3DS Server | JSON：Boolean。許容値：`true`、`false`。 | 02-BRW | 01-PA<br>02-NPA | AReq = R | — |
| ブラウザ言語<br>`browserLanguage` | IETF BCP47で定義するブラウザ言語を表す値。`navigator.language`プロパティから返される。詳細はA.6節参照。 | 3DS Server | 可変長、最大35文字。JSON：String。 | 02-BRW | 01-PA<br>02-NPA | AReq = C | Browser JavaScript Enabled = trueの場合に必須。それ以外は任意。 |

---

<a id="page-213"></a>

## 原本 213ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ブラウザ画面の色深度<br>`browserColorDepth` | 画像を表示するカラーパレットのビット深度を、1ピクセルあたりのビット数で表す値。カード会員のブラウザの`screen.colorDepth`プロパティから取得する。詳細はA.6節参照。 | 3DS Server | 1–2文字、数値。JSON：String。許容値：`1–99`。注：ACSが提供された値に対応していない場合、最も近い対応値を使用できる。例えば、提供値が`30`でACSが未対応の場合、`24`を使用できる。 | 02-BRW | 01-PA<br>02-NPA | AReq = C | Browser JavaScript Enabled = trueの場合に必須。それ以外は任意。 |
| ブラウザ画面の高さ<br>`browserScreenHeight` | カード会員の画面全体の高さをピクセル単位で表す。値は`screen.height`プロパティから返される。詳細はA.6節参照。 | 3DS Server | 可変長、1–6文字、数値。JSON：String。 | 02-BRW | 01-PA<br>02-NPA | AReq = C | Browser JavaScript Enabled = trueの場合に必須。それ以外は任意。 |
| ブラウザ画面の幅<br>`browserScreenWidth` | カード会員の画面全体の幅をピクセル単位で表す。値は`screen.width`プロパティから返される。詳細はA.6節参照。 | 3DS Server | 可変長、1–6文字、数値。JSON：String。 | 02-BRW | 01-PA<br>02-NPA | AReq = C | Browser JavaScript Enabled = trueの場合に必須。それ以外は任意。 |

---

<a id="page-214"></a>

## 原本 214ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ブラウザタイムゾーン<br>`browserTZ` | UTCとカード会員のブラウザの現地時間との差を分単位で表す。現地タイムゾーンがUTCより遅れている場合は正、進んでいる場合は負。 | 3DS Server | 可変長、1–5文字。JSON：String。値は`getTimezoneOffset()`メソッドから返される。例：UTC -5時間の場合は`300`または`+300`。UTC +5時間の場合は`-300`。詳細はA.6節参照。 | 02-BRW | 01-PA<br>02-NPA | AReq = C | Browser JavaScript Enabled = trueの場合に必須。それ以外は任意。 |
| ブラウザUser-Agent<br>`browserUserAgent` | HTTP user-agentヘッダーの正確な内容。 | 3DS Server | 可変長、最大2048文字。JSON：String。注：ブラウザが送信するUser-Agent全体の長さが2048文字を超える場合、3DS Serverは超過部分を切り捨てる。詳細はA.6節参照。 | 02-BRW | 01-PA<br>02-NPA | AReq = R | — |

---

<a id="page-215"></a>

## 原本 215ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ブラウザ利用者のデバイスID<br>`deviceId` | デバイスに紐付く一意かつ不変の識別子。同じ利用者デバイスについて、3DS取引間で一貫する。例：ハードウェアのデバイスID、プラットフォームが算出したデバイスフィンガープリント。SDK Device InformationのD021を参照。 | 3DS Server | 可変長、最大64文字。JSON：String。 | 02-BRW | 01-PA<br>02-NPA | AReq = C | 利用可能な場合に必須。 |
| ブラウザ利用者ID<br>`userId` | 取引を行う利用者のBrowser Account IDの識別子。そのブラウザにおける利用者のアカウント識別子の、一意かつ不変のハッシュを文字列として提供する。注：カード会員は同じブラウザで複数のアカウントを持つ場合がある。SDK Device InformationのD026を参照。 | 3DS Server | 可変長、最大64文字。JSON：String。 | 02-BRW | 01-PA<br>02-NPA | AReq = C | 利用可能な場合に必須。 |

---

<a id="page-216"></a>

## 原本 216ページ

**表A.1（続き）**

| データ要素／フィールド名 | 説明 | 提供元 | 長さ／形式／値 | デバイスチャネル | メッセージカテゴリ | メッセージへの包含 | 条件付き包含 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| カード範囲データ<br>`cardRangeData` | DSが提供するカード範囲データ。ACSが対応する最新のプロトコルバージョン、および任意でその範囲をホストするDSの対応バージョンを示す。設定されていれば3DS Method用のACS URLも示す。さらに、Trust Listや分離認証など、ACSが対応する3DS機能を識別する。DSに保存されたカード範囲の数と同じだけのJSONオブジェクトが存在してもよい。 | DS | 要素数：可変、1–200000。JSON：Array of objects。Card Range Dataのデータ要素は表A.6を参照。 | N/A | N/A | PRes = C | 前回のPResメッセージのSerial Numberから変更されている場合、またはPReqメッセージにSerial Numberがない場合に必須。かつ、Card Range Data File URLが存在する場合は含めない。 |
| カード範囲データのダウンロード指標<br>`cardRangeDataDownloadInd` | 3DS ServerがファイルからのCard Range Data取得に対応するかを示す。注：存在する場合、このフィールドには値`Y`が入る。 | 3DS Server | 1文字。JSON：String。許容値：`Y` = ダウンロード対応。 | N/A | N/A | PReq = C | 3DS ServerがCard Range Data Fileのダウンロードに対応する場合にのみ存在する。 |

---

