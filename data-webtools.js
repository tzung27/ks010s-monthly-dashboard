// ─────────────────────────────────────────────────────────────
// AI & 網站開發工具資料
// ─────────────────────────────────────────────────────────────
const WEBTOOLS_DEFAULT = [
  {id:'wt1', name:'CSP Renewal Dashboard',                  url:'https://tzung27.github.io/WIIM365RenewMSFULL/csp_renewal_dashboard.html', cat:'分析工具',   desc:'CSP 客戶續約狀態總覽儀表板，提供合約到期預警與授權使用情況分析。', note:''},
  {id:'wt2', name:'Weblink M365 續約概況與精準行銷推廣平台', url:'https://wiim365renewms-4ay4fvrj2w6qh4zh89l3bh.streamlit.app/',              cat:'行銷平台',   desc:'基於 Streamlit 建置的 M365 續約概況平台，整合精準行銷推廣功能。',   note:''},
  {id:'wt3', name:'KS010S 部門月報系統',                    url:'https://ks010s-monthly-dashboard.pages.dev/',                             cat:'月報系統',   desc:'KS010S 部門每月績效與業務指標總覽，部署於 Cloudflare Pages。',      note:''},
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
