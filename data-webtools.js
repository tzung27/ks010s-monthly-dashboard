// ─────────────────────────────────────────────────────────────
// AI & 網站開發工具資料
// ─────────────────────────────────────────────────────────────
const WEBTOOLS_DEFAULT = [
  {id:'wt1', name:'CSP Renewal Dashboard', url:'https://tzung27.github.io/WIIM365RenewMSFULL/csp_renewal_dashboard.html', cat:'分析工具', desc:'CSP 客戶續約狀態總覽儀表板，提供合約到期預警與授權使用情況分析。', note:'Allen - 仿原廠'},
  {id:'wt2', name:'Weblink M365 續約概況與精準行銷推廣平台', url:'https://wiim365renewms-4ay4fvrj2w6qh4zh89l3bh.streamlit.app/', cat:'行銷平台', desc:'基於 Streamlit 建置的 M365 續約概況平台，整合精準行銷推廣功能。', note:'Allen'},
  {id:'wt3', name:'KS010S 部門月報系統', url:'https://ks010s-monthly-dashboard.pages.dev/', cat:'月報系統', desc:'KS010S 部門每月績效與業務指標總覽，部署於 Cloudflare Pages。', note:'Allen'},
  {id:'wt1780642051982', name:'展碁 Weekly 產品週報、技術週報', url:'', cat:'產品 & 技術週報', desc:'週一：產品週報、Azure 技術週報\n週二：M365 技術週報、週三：Copilot 技術週報、週四：Security 技術週報\n週五：週技術精選彙整', note:'Allen - 使用 M365 Copilot Cowork'},
  {id:'wt1780907044365', name:'Weblink 展碁國際線上教學 Youtube', url:'https://www.youtube.com/@weblink2199', cat:'線上教學', desc:'以 Adobe Creative Cloud 授權管理與專業應用為核心，並結合 Microsoft 系統整合技術 與 Jamf MDM 行動裝置管理 ，提供企業與教育單位完整的數位化線上教學支援。', note:'Adobe Jimmy - 嘔心瀝血之作'},
  {id:'wt1780907108927', name:'Microsoft Azure 完整指南', url:'https://i-services.info/mscloud/azure-guide.html', cat:'Azure 大使', desc:'', note:'Lucas'},
  {id:'wt1780907160125', name:'AvePoint', url:'', cat:'代理產品支援', desc:'', note:'Aaron'},
  {id:'wt1780907199270', name:'BlueChip ManageEngine', url:'', cat:'代理產品支援', desc:'', note:''},
  {id:'wt1780907305829', name:'AMM ASP 稽核 - 2026', url:'', cat:'ASP 稽核', desc:'', note:'Lucas'},
  {id:'wt1783327001124', name:'Microsoft Frontier Transform 黑客松', url:'https://microsoft.sharepoint.com/:f:/r/teams/OCP-China-PTA/Shared%20Documents/Forms/AllItems.aspx?id=%2fteams%2fOCP-China-PTA%2fShared+Documents%2fGeneral%2f1+-+FY26+WorkingDocs%2f1+-+GCR+AI+Agentic+Hackathon%2fPartner+Agent%2fLow+Code+Track%2f70-Weblink+International+Inc.-Product+InfoPilot+%E2%80%94+Product+Intelligence+%26+Technical+Weekly+Agent&p=true&share=cgqnjbdJ7lipTZIHD72sggO3EgUCqjK4zWWt9GfPvHZIenC-7Q', cat:'Copilot Studio', desc:'', note:'6/23'},
  {id:'wt1783327055318', name:'Adobe 續約總表管理系統', url:'http://allenchung168.pythonanywhere.com', cat:'', desc:'', note:''},
  {id:'wt1783327550872', name:'Weblink M365 續約精準行銷 old', url:'https://weblink-m365-dashboar-eq23r59ryjiydohbnkgg54.streamlit.app/', cat:'', desc:'', note:''},
  {id:'wt1784259944299', name:'動態權重與分紅 KPI 管理系統', url:'file:///D:/excel_dashboard13%20%E5%88%86%E7%B4%85%E7%B8%BE%E6%95%88/KPI_Dashboard_Summary.html', cat:'管理系統', desc:'', note:'Allen'},
  {id:'wt1784859807355', name:'Apple Business 申請流程說明', url:'https://www.youtube.com/watch?v=WjgNnqOrkAg', cat:'線上教學', desc:'帳號：training.weblink@gmail.com\n密碼：Training.Weblink\n我們的都沒公開 得知道連結或是透過 KS010S KB才能看', note:'Denny & William'}
];

function loadWebtools(){
  const s=localStorage.getItem('ks_webtools');
  return s?JSON.parse(s):JSON.parse(JSON.stringify(loadWebtoolsDefault()));
}
function saveWebtools(d){localStorage.setItem('ks_webtools',JSON.stringify(d));}

function saveWebtoolsAsDefault(d){
  localStorage.setItem('ks_webtools_default',JSON.stringify(d));
}
function loadWebtoolsDefault(){
  const s=localStorage.getItem('ks_webtools_default');
  return s?JSON.parse(s):JSON.parse(JSON.stringify(WEBTOOLS_DEFAULT));
}
function resetWebtools(){
  localStorage.removeItem('ks_webtools');
}
