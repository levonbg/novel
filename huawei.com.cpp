getProductDetails

rcjc

if (params.GetString("applicationID").empty()) {
	break;
}
if (params.GetString("requestId").empty()) {
	break;
}
if (params.GetString("merchantId").empty()) {
	break;
}
if (params.GetString("productNos").empty()) {
	break;
}


aaa.appId = params.GetString("applicationID");
aaa.requestId = params.GetString("requestId");
aaa.merchantId = params.GetString("merchantId");
aaa.productNos = params.GetString("productNos");


return
succ
JsonArray array;
JsonObject obj;
obj.Put("productNo", input.GetString("productNo"));
obj.Put("microsPrice", input.GetLong("microsPrice"));
obj.Put("price", input.GetString("price"));
obj.Put("currency", input.GetString("currency"));
obj.Put("country", input.GetString("country"));
obj.Put("productName", input.GetString("productName"));
obj.Put("productDesc", input.GetString("productDesc"));
array.PushBack(obj);

fail
JsonArray array;
obj.Put("productNo", input.GetString("productNo"));
obj.Put("code", input.GetInt("code"));
obj.Put("msg", input.GetString("msg"));
array.PushBack(obj);





getPurchaseInfo
rcjc

if (params.GetString("appId").empty()) {
	break;
}
if (params.GetString("priceType").empty()) {
	break;
}
if (params.GetString("merchantId").empty()) {
	break;
}
if (params.GetLong("ts") == 0) {
	break;
}
if (params.GetString("publicKey").empty()) {
	break;
}
if (params.GetLong("pageNo") == 0) {
	break;
}
if (params.GetString("sign").empty()) {
	break;
}
aaa.appId = params.GetString("appId");
aaa.priceType = params.GetString("priceType");
aaa.merchantId = params.GetString("merchantId");
aaa.ts = params.GetLong("ts");
aaa.publicKey = params.GetString("publicKey");
aaa.pageNo = params.GetLong("pageNo");
aaa.sign = params.GetString("sign");
aaa.productId = params.GetString("productId");

return
JsonArray array;
obj.Put("requestId", input.GetString("requestId"));
obj.Put("merchantId", input.GetString("merchantId"));
obj.Put("appId", input.GetString("appId"));
obj.Put("productId", input.GetString("productId"));
obj.Put("tradeTime", input.GetString("tradeTime"));
array.PushBack(obj);


getOrderDetail
if (params.GetString("requestId").empty()) {
	break;
}
if (params.GetString("keyType").empty()) {
	break;
}
if (params.GetString("merchantId").empty()) {
	break;
}
if (params.GetString("time").empty()) {
	break;
}
if (params.GetString("publicKey").empty()) {
	break;
}
if (params.GetString("sign").empty()) {
	break;
}
aaa.requestId = params.GetString("requestId");
aaa.keyType = params.GetString("keyType");
aaa.merchantId = params.GetString("merchantId");
aaa.time = params.GetString("time");
aaa.publicKey = params.GetString("publicKey");
aaa.sign = params.GetLong("sign");



pay.getPurchaseInfo(OBJECT)
查询当前用户已订购的非消耗商品订单信息。

1. 入参校验

2. callback拼接

pay.getOrderDetail(OBJECT)
查询订单详情，所有调用pay接口的订单均可查询，用于在丢单的情况下复核订单。

1. 入参校验

2. callback拼接



class AAA
{
    public:
    bool Parse(std::string input);

std::string GetReturnDesc();
std::string GetRequestId();
std::string GetOrderID();
std::string GetOrderTime();
std::string GetTradeTime();
std::string GetStatus();
std::string GetSign();
    private:
std::string returnDesc;
std::string requestId;
std::string orderID;
std::string orderTime;
std::string tradeTime;
std::string status;
std::string sign;
}

bool AAA::Parse(std::string input)
{
    auto result = xxx(input);
    if (！result.IsObject()) {
        return false;
    }

    if (!result.HasMember("returnDesc") || !result.IsString("returnDesc")){
        return false;
    } 
    returnDesc = result.GetString("returnDesc");
    if (!result.HasMember("requestId") || !result.IsString("requestId")){
        return false;
    } 
    requestId = result.GetString("requestId");
    if (!result.HasMember("orderID") || !result.IsString("orderID")){
        return false;
    } 
    orderID = result.GetString("orderID");
    if (!result.HasMember("orderTime") || !result.IsString("orderTime")){
        return false;
    } 
    orderTime = result.GetString("orderTime");
    if (!result.HasMember("tradeTime") || !result.IsString("tradeTime")){
        return false;
    } 
    tradeTime = result.GetString("tradeTime");
    if (!result.HasMember("status") || !result.IsString("status")){
        return false;
    } 
    status = result.GetString("status");
    if (!result.HasMember("sign") || !result.IsString("sign")){
        return false;
    } 
    sign = result.GetString("sign");
    return true;
}

std::string AAA::GetReturnDesc()
{
    return returnDesc;
}
std::string AAA::GetRequestId()
{
    return requestId;
}
std::string AAA::GetOrderID()
{
    return orderID;
}
std::string AAA::GetOrderTime()
{
    return orderTime;
}
std::string AAA::GetTradeTime()
{
    return tradeTime;
}
std::string AAA::GetStatus()
{
    return status;
}
std::string AAA::GetSign()
{
    return sign;
}




class BBB
{
    public:
    bool Parse(std::string input);

std::string GetRtnCode();
std::string GetPageCount();
std::string GetPurchaseInfoList();
std::string GetSign();
    private:
std::string rtnCode;
std::string pageCount;
std::string purchaseInfoList;
std::string sign;
}

bool BBB::Parse(std::string input)
{
    auto result = xxx(input);
    if (！result.IsObject()) {
        return false;
    }

    if (!result.HasMember("rtnCode") || !result.IsString("rtnCode")){
        return false;
    } 
    rtnCode = result.GetString("rtnCode");
    if (!result.HasMember("pageCount") || !result.IsString("pageCount")){
        return false;
    } 
    pageCount = result.GetString("pageCount");
    if (!result.HasMember("purchaseInfoList") || !result.IsString("purchaseInfoList")){
        return false;
    } 
    purchaseInfoList = result.GetString("purchaseInfoList");
    if (!result.HasMember("orderTime") || !result.IsString("orderTime")){
        return false;
    } 
    if (!result.HasMember("sign") || !result.IsString("sign")){
        return false;
    } 
    sign = result.GetString("sign");
    return true;
}

std::string BBB::GetRtnCode()
{
    return rtnCode;
}
std::string BBB::GetPageCount()
{
    return pageCount;
}
std::string BBB::GetPurchaseInfoList()
{
    return purchaseInfoList;
}
std::string BBB::GetSign()
{
    return sign;
}

