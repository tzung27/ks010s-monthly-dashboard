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
      {id:'sec-az500', code:'AZ-500', name:'Microsoft Azure Security Engineer',    required:6, members:{Allen:0,Nick:0,Lucas:1,Aaron:1,Guo:0,Eric:0}},
      {id:'sec-sc200', code:'SC-200', name:'Microsoft Security Operations Analyst',required:5, members:{Allen:0,Nick:1,Lucas:1,Aaron:1,Guo:0}},
    ]
  },
  infra: {
    label:'Infra and Database Migration to Microsoft Azure ASP', subtitle:'Microsoft Azure 基礎架構與資料庫遷移專長方案',
    icon:'☁️', theme:'asp-infra', deadline:'2026/10/26',
    refsTitle:'Audit',
    dlNote:'評估期間 2026/07/28～2026/10/26，Module B 由 Lucas 與 Allen 共同負責，尚缺一人考取左列任一認證 (洽詢高雄趨勢工程師 AZ-104)。',
    refs:[
      {name:'Module A', who:'',              date:'',           done:false},
      {name:'Module B', who:'Lucas / Allen', date:'2026/10/26', done:false},
    ],
    certs:[
      {id:'infra-az104', code:'AZ-104', name:'Microsoft Azure Administrator Associate', required:1, members:{Allen:1,Somebody01:0,Lucas:1,Aaron:1}},
      {id:'infra-az500', code:'AZ-500', name:'Azure Security Engineer Associate',        required:1, members:{Allen:0,Somebody01:0,Lucas:1,Aaron:1}},
      {id:'infra-dp300', code:'DP-300', name:'Azure 資料庫管理師助理',                   required:1, members:{Allen:0,Somebody01:0,Lucas:0,Aaron:0}},
      {id:'infra-az400', code:'AZ-400', name:'DevOps Engineer Expert',                   required:1, members:{Allen:1,Somebody01:0,Lucas:0,Aaron:0}},
    ]
  },
  copilotnew: {
    label:'Copilot ASP (New)', subtitle:'Microsoft Copilot 下一代專長方案',
    icon:'🤖', theme:'asp-copilotnew', deadline:'2026/09/30',
    refsTitle:'Audit',
    dlNote:'SC-401 與 AB-100 全員已完成；Audit / Module A / Module B 稽核進行中，Module B 由 Aaron 負責，截止日 2026/09/30。',
    refs:[
      {name:'Module A', who:'',    date:'',           done:false},
      {name:'Module B', who:'Aaron', date:'2026/09/30', done:false},
    ],
    certs:[
      {id:'cnew-sc401', code:'SC-401', name:'Information Security Administrator Associate', required:5, members:{Allen:1,Somebody:1,Lucas:1,Aaron:1,Guo:1}},
      {id:'cnew-ab100', code:'AB-100', name:'Agentic AI Business Solutions Architect',       required:5, members:{Allen:1,Somebody:1,Lucas:1,Aaron:1,Guo:1}},
    ]
  },
  datasecurity: {
    label:'Data Security ASP', subtitle:'Microsoft 資料安全性專長方案',
    icon:'🗄️', theme:'asp-datasecurity', deadline:'2026/08/31',
    dlNote:'客戶推薦資料三件均由 Aaron 負責，截止日 2026/08/31，目前尚未完成，請盡速準備並上傳至合作夥伴入口網站。',
    refs:[
      {name:'客戶推薦資料 01', who:'Aaron', date:'2026/08/31', done:false},
      {name:'客戶推薦資料 02', who:'Aaron', date:'2026/08/31', done:false},
      {name:'客戶推薦資料 03', who:'Aaron', date:'2026/08/31', done:false},
    ],
    certs:[
      {id:'ds-sc401',  code:'SC-401',        name:'Information Security Administrator Associate',                       required:6, members:{Allen:1,Somebody01:0,Lucas:1,Aaron:1,Guo:1,Eric:0}},
      {id:'ds-as-pur', code:'Applied Skills', name:'使用 Microsoft Purview 實作資訊保護和資料外洩防護', required:4, members:{Allen:1,Lucas:1,Aaron:1,Guo:1}},
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
  let d;
  try{
    const s=localStorage.getItem('ks_partner_data');
    d=s?JSON.parse(s):JSON.parse(JSON.stringify(PARTNER_DATA_DEFAULT));
  }catch(e){d=JSON.parse(JSON.stringify(PARTNER_DATA_DEFAULT));}
  // 自動修正舊名稱
  if(d.subtitle) d.subtitle=d.subtitle.replace(/展基數位/g,'展碁國際');
  if(d.title)    d.title=d.title.replace(/展基數位/g,'展碁國際');
  // 確保必要陣列欄位存在（防止舊 localStorage 殘存資料破壞 .map()）
  if(!Array.isArray(d.specializations))      d.specializations=PARTNER_DATA_DEFAULT.specializations.map(x=>({...x}));
  if(!d.solutionDesignations||!Array.isArray(d.solutionDesignations.items))
    d.solutionDesignations=JSON.parse(JSON.stringify(PARTNER_DATA_DEFAULT.solutionDesignations));
  if(!Array.isArray(d.partnerCards))         d.partnerCards=PARTNER_DATA_DEFAULT.partnerCards.map(x=>({...x}));
  delete d.aspImages; // 清除舊版殘存欄位
  return d;
}
function savePartnerData(d){localStorage.setItem('ks_partner_data',JSON.stringify(d));}
function resetPartnerData(){localStorage.removeItem('ks_partner_data');}

function loadAspData(){
  // DEFAULT 是結構來源（refsTitle、refs 清單、certs 清單）；localStorage 保留用戶可編輯狀態
  const d = JSON.parse(JSON.stringify(ASP_DATA_DEFAULT));
  let cached = null;
  try{ const s=localStorage.getItem('ks_asp_data'); cached=s?JSON.parse(s):null; }catch(e){}
  if(cached){
    Object.entries(d).forEach(([k,asp])=>{
      const c=cached[k]; if(!c) return;
      // 保留文字欄位
      if(c.dlNote   !== undefined) asp.dlNote   = c.dlNote;
      if(c.deadline !== undefined) asp.deadline = c.deadline;
      // 保留 refs done 狀態（以名稱對應）
      if(Array.isArray(c.refs)){
        const cmap={}; c.refs.forEach(r=>{ cmap[r.name]=r; });
        asp.refs.forEach(r=>{ if(cmap[r.name]) r.done=!!cmap[r.name].done; });
      }
      // 保留 cert member 切換狀態（以 cert.id 對應，只覆蓋 DEFAULT 已知的成員）
      if(Array.isArray(c.certs)){
        const certMap={}; c.certs.forEach(cert=>{ certMap[cert.id]=cert; });
        asp.certs.forEach(cert=>{
          const cc=certMap[cert.id]; if(!cc||!cc.members) return;
          Object.keys(cert.members).forEach(m=>{
            if(cc.members[m]!==undefined) cert.members[m]=cc.members[m];
          });
        });
      }
    });
  }
  return d;
}
function saveAspData(d){localStorage.setItem('ks_asp_data',JSON.stringify(d));}
function resetAspData(){localStorage.removeItem('ks_asp_data');}
