// ─────────────────────────────────────────────────────────────
// 內部使用權 (IUR) 資料
// ─────────────────────────────────────────────────────────────

const IUR_AZURE_DEFAULT = [
  {id:'az1', label:'AzureAI ASP',         usd:21720, desc:'針對 AI 相關應用專案所分配的 Azure 贊助點數。',     icon:'🧠', color:'#DBEAFE'},
  {id:'az2', label:'InfraDB Migrate ASP', usd:24320, desc:'用於基礎架構與資料庫遷移專案的資源預算。',           icon:'🗄️', color:'#CCFBF1'},
  {id:'az3', label:'Competency',          usd:29000, desc:'核心技術能力發展與專長認證相關的點數分配，為目前金額最高的項目。', icon:'🏅', color:'#D1FAE5'},
];

// price = NTD 單價/月（List Price，0 = 未填）
// 資料來源：Microsoft 台灣官網 https://www.microsoft.com/zh-tw/ 2026-05-19 查詢
const IUR_PRODUCTS_DEFAULT = [
  // Teams / 核心協作工具
  {id:'p001', name:'Teams Enterprise',                          qty:697, cat:'teams',        subcat:'Teams',          price:275},
  {id:'p002', name:'Teams Premium',                             qty:10,  cat:'teams',        subcat:'Teams',          price:320},
  {id:'p003', name:'Teams Rooms Pro',                           qty:5,   cat:'teams',        subcat:'Teams',          price:1285},
  // M365
  {id:'p004', name:'Microsoft 365 E5 (no Teams)',               qty:300, cat:'m365',         subcat:'M365',           price:1560},
  {id:'p005', name:'Microsoft 365 E3 (no Teams)',               qty:260, cat:'m365',         subcat:'M365',           price:955},
  {id:'p006', name:'Microsoft 365 Business Premium (no Teams)', qty:37,  cat:'m365',         subcat:'M365',           price:705},
  {id:'p007', name:'Microsoft 365 EDU A5',                      qty:37,  cat:'m365',         subcat:'M365',           price:0},
  // Dynamics 365
  {id:'p008', name:'Dynamics 365 Customer Service Enterprise',  qty:100, cat:'dynamics',     subcat:'Dynamics 365',   price:3375},
  {id:'p009', name:'Dynamics 365 Finance Premium',              qty:100, cat:'dynamics',     subcat:'Dynamics 365',   price:9645},
  {id:'p010', name:'Dynamics 365 Sales Enterprise',             qty:100, cat:'dynamics',     subcat:'Dynamics 365',   price:3375},
  {id:'p011', name:'Dynamics 365 Human Resources',              qty:100, cat:'dynamics',     subcat:'Dynamics 365',   price:4340},
  {id:'p012', name:'Dynamics 365 Contact Center',               qty:100, cat:'dynamics',     subcat:'Dynamics 365',   price:3535},
  {id:'p013', name:'Dynamics 365 Business Central Premium',     qty:100, cat:'dynamics',     subcat:'Dynamics 365',   price:3535},
  {id:'p014', name:'Dynamics 365 Team Members',                 qty:100, cat:'dynamics',     subcat:'Dynamics 365',   price:320},
  {id:'p015', name:'Dynamics 365 Project Operations',           qty:100, cat:'dynamics',     subcat:'Dynamics 365',   price:4340},
  {id:'p016', name:'Dynamics 365 Customer Insights',            qty:1,   cat:'dynamics',     subcat:'Dynamics 365',   price:54660},
  {id:'p017', name:'Dynamics 365 Marketing (Base Pack)',        qty:1,   cat:'dynamics',     subcat:'Dynamics 365',   price:54660},
  // Security
  {id:'p018', name:'Defender for Endpoint P2',                  qty:260, cat:'security',     subcat:'Security',       price:166},
  {id:'p019', name:'Entra ID P2',                               qty:260, cat:'security',     subcat:'Security',       price:290},
  // Power Platform
  {id:'p020', name:'Power BI Premium',                          qty:200, cat:'powerplatform',subcat:'Power Platform',  price:770},
  {id:'p021', name:'Power Apps Premium',                        qty:175, cat:'powerplatform',subcat:'Power Platform',  price:645},
  {id:'p022', name:'Power Automate Premium',                    qty:125, cat:'powerplatform',subcat:'Power Platform',  price:480},
  {id:'p023', name:'Power Automate Process',                    qty:25,  cat:'powerplatform',subcat:'Power Platform',  price:4825},
  // Copilot
  {id:'p024', name:'Microsoft 365 Copilot',                     qty:5,   cat:'copilot',      subcat:'Copilot',        price:965},
  {id:'p025', name:'Microsoft 365 Copilot for Sales',           qty:5,   cat:'copilot',      subcat:'Copilot',        price:965},
  {id:'p026', name:'Microsoft 365 Copilot for Service',         qty:5,   cat:'copilot',      subcat:'Copilot',        price:965},
  {id:'p027', name:'Microsoft 365 Copilot for Finance',         qty:5,   cat:'copilot',      subcat:'Copilot',        price:965},
  // Other
  {id:'p028', name:'Microsoft Project Online Project Plan 5',   qty:100, cat:'other',        subcat:'其他',           price:1760},
  {id:'p029', name:'Microsoft Visio Plan 2',                    qty:25,  cat:'other',        subcat:'其他',           price:480},
  {id:'p030', name:'Windows 365 Enterprise',                    qty:12,  cat:'other',        subcat:'其他',           price:1080},
  {id:'p031', name:'Viva Suite',                                qty:50,  cat:'other',        subcat:'其他',           price:385},
  // Sandbox
  {id:'p032', name:'Dynamics 365 Contact Center Partner Sandbox',                          qty:25,  cat:'sandbox',subcat:'Partner Sandbox',price:0},
  {id:'p033', name:'Dynamics 365 Partner Sandbox – Operations Application',                qty:100, cat:'sandbox',subcat:'Partner Sandbox',price:0},
  {id:'p034', name:'Dynamics 365 Partner Sandbox – Sales, Field Service and Customer Service',qty:100,cat:'sandbox',subcat:'Partner Sandbox',price:0},
  {id:'p035', name:'Dynamics 365 Partner Sandbox – Human Resources',                       qty:5,   cat:'sandbox',subcat:'Partner Sandbox',price:0},
  {id:'p036', name:'Dynamics 365 Partner Sandbox – Sales Insights',                        qty:5,   cat:'sandbox',subcat:'Partner Sandbox',price:0},
  {id:'p037', name:'Dynamics 365 Partner Sandbox – Guides',                                qty:1,   cat:'sandbox',subcat:'Partner Sandbox',price:0},
  {id:'p038', name:'Dynamics 365 Partner Sandbox – Marketing',                             qty:1,   cat:'sandbox',subcat:'Partner Sandbox',price:0},
  {id:'p039', name:'Dynamics 365 Partner Sandbox – eCommerce and Cloud Scale Unit',        qty:1,   cat:'sandbox',subcat:'Partner Sandbox',price:0},
  {id:'p040', name:'Dynamics 365 Partner Sandbox – Customer Service Digital Messaging',    qty:5,   cat:'sandbox',subcat:'Partner Sandbox',price:0},
  {id:'p041', name:'Dynamics 365 Partner Sandbox – Intelligent Order Management',          qty:1,   cat:'sandbox',subcat:'Partner Sandbox',price:0},
  {id:'p042', name:'Dynamics 365 Partner Sandbox – Business Central',                      qty:5,   cat:'sandbox',subcat:'Partner Sandbox',price:0},
  {id:'p043', name:'Dynamics 365 Partner Sandbox – Operations Application Tier 2 Add on', qty:1,   cat:'sandbox',subcat:'Partner Sandbox',price:0},
];

function loadIurAzure(){
  const s=localStorage.getItem('ks_iur_azure');
  return s?JSON.parse(s):JSON.parse(JSON.stringify(IUR_AZURE_DEFAULT));
}
function saveIurAzure(d){localStorage.setItem('ks_iur_azure',JSON.stringify(d));}

function loadIurProducts(){
  const s=localStorage.getItem('ks_iur_products');
  if(!s) return JSON.parse(JSON.stringify(IUR_PRODUCTS_DEFAULT));
  const d=JSON.parse(s);
  // 補齊舊資料缺少的 price 欄位，並自動從預設值填入尚未設定的單價
  d.forEach(p=>{
    if(p.price===undefined||p.price===0){
      const def=IUR_PRODUCTS_DEFAULT.find(x=>x.id===p.id);
      if(def&&def.price>0) p.price=def.price;
    }
  });
  return d;
}
function saveIurProducts(d){localStorage.setItem('ks_iur_products',JSON.stringify(d));}

function loadIurSettings(){
  const s=localStorage.getItem('ks_iur_settings');
  return s?JSON.parse(s):{exchangeRate:32};
}
function saveIurSettings(d){localStorage.setItem('ks_iur_settings',JSON.stringify(d));}

function resetIurData(){
  localStorage.removeItem('ks_iur_azure');
  localStorage.removeItem('ks_iur_products');
  localStorage.removeItem('ks_iur_settings');
}
