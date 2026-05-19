// ─────────────────────────────────────────────────────────────
// ASP 專長方案追蹤資料
// ─────────────────────────────────────────────────────────────
const ASP_DATA_DEFAULT = {
  copilot: {
    label:'Copilot ASP', subtitle:'Microsoft 365 Copilot 專長方案',
    icon:'🤖', theme:'asp-copilot', deadline:'2026/03/31',
    dlNote:'MS-102 (Guo) 須於此日期前完成以符合專長資格。',
    refs:[
      {name:'角色型 Copilot 導入專案', who:'Nick', date:'2026/02/28', done:true},
      {name:'Copilot 延伸模組實作',     who:'Nick', date:'2026/02/28', done:true},
      {name:'自訂 Copilot 實作',         who:'Nick', date:'2026/02/28', done:true},
    ],
    certs:[
      {id:'cop-sc401', code:'SC-401',        name:'Administering Information Security in M365',       required:5, members:{Allen:1,Nick:1,Lucas:1,Aaron:1,Guo:1}},
      {id:'cop-ms102', code:'MS-102',        name:'Microsoft 365 Administrator Expert',               required:5, members:{Allen:1,Nick:1,Lucas:1,Aaron:1,Guo:0}},
      {id:'cop-as1',   code:'Applied Skills',name:'準備安全性和合規性以支援 M365 Copilot',            required:5, members:{Allen:1,Nick:1,Lucas:1,Aaron:1,Guo:1}},
      {id:'cop-as2',   code:'Applied Skills',name:'在 Microsoft Copilot Studio 中建立代理程式',       required:5, members:{Allen:1,Nick:1,Lucas:1,Aaron:1,Guo:1}},
    ]
  },
  security: {
    label:'Cloud Security ASP', subtitle:'Microsoft 雲端資安專長方案',
    icon:'🔒', theme:'asp-security', deadline:'2026/06/30',
    dlNote:'相較於 Copilot ASP，此專長擁有更充裕的緩衝時間，請把握時機加速備考。',
    refs:[
      {name:'客戶推薦資料 01', who:'Aaron', date:'2026/03/31', done:true},
      {name:'客戶推薦資料 02', who:'Aaron', date:'2026/03/31', done:true},
      {name:'客戶推薦資料 03', who:'Lucas', date:'2026/03/31', done:true},
    ],
    certs:[
      {id:'sec-az500', code:'AZ-500', name:'Microsoft Azure Security Engineer',    required:6, members:{Allen:1,Nick:0,Lucas:1,Aaron:1,Guo:0,Eric:0}},
      {id:'sec-sc200', code:'SC-200', name:'Microsoft Security Operations Analyst',required:5, members:{Allen:0,Nick:1,Lucas:1,Aaron:1,Guo:0}},
    ]
  }
};

// ─────────────────────────────────────────────────────────────
// 合作夥伴認證資料
// ─────────────────────────────────────────────────────────────
const PARTNER_DATA_DEFAULT = {
  title:    '我們的技術實力與合作夥伴認證',
  subtitle: '展碁國際致力於提供業界領先的 AI 解決方案，這得益於我們深厚的技術實力與策略性合作夥伴認證。',
  specializations: [
    {id:'sp1', text:'【Without GAP】AI Platform on Microsoft Azure'},
    {id:'sp2', text:'【Without GAP】Infra and Database Migration to Microsoft Azure'},
  ],
  solutionDesignations: {
    total: 6,
    items: [
      {id:'sd1', text:'Data & AI',              done:true},
      {id:'sd2', text:'Infrastructure',          done:true},
      {id:'sd3', text:'Modern Work',             done:true},
      {id:'sd4', text:'Security',                done:true},
      {id:'sd5', text:'Digital & App Innovation',done:true},
      {id:'sd6', text:'Business Applications',   done:false},
    ]
  },
  partnerCards: [
    {id:'pc1', area:'Data & AI',     sub:'Azure', specialist:'AI Platform on Microsoft Azure'},
    {id:'pc2', area:'Infrastructure',sub:'Azure', specialist:'Infra and Database Migration'},
  ]
};

function loadPartnerData(){
  const s=localStorage.getItem('ks_partner_data');
  const d=s?JSON.parse(s):JSON.parse(JSON.stringify(PARTNER_DATA_DEFAULT));
  // 自動修正舊名稱
  if(d.subtitle) d.subtitle=d.subtitle.replace(/展基數位/g,'展碁國際');
  if(d.title)    d.title=d.title.replace(/展基數位/g,'展碁國際');
  return d;
}
function savePartnerData(d){localStorage.setItem('ks_partner_data',JSON.stringify(d));}
function resetPartnerData(){localStorage.removeItem('ks_partner_data');}

function loadAspData(){
  const s=localStorage.getItem('ks_asp_data');
  return s?JSON.parse(s):JSON.parse(JSON.stringify(ASP_DATA_DEFAULT));
}
function saveAspData(d){localStorage.setItem('ks_asp_data',JSON.stringify(d));}
function resetAspData(){localStorage.removeItem('ks_asp_data');}
