// ─────────────────────────────────────────────────────────────
// Microsoft 認證追蹤資料（依 2026-05-19 匯出 CSV 校正）
// Allen=11, Nick=11, Lucas=13, Aaron=12, Bruno=1 → 合計48
// ─────────────────────────────────────────────────────────────
const CERT_MEMBERS_LIST = ['Allen', 'Nick', 'Lucas', 'Aaron', 'Bruno'];

const CERT_DATA_DEFAULT = [
  // id          name                                                           code      expiry        csa                          cat1                   cat2                                                   note           Allen Nick Lucas Aaron Bruno
  { id:'CR001', name:'Azure AI Engineer Associate',                           code:'AI-102', expiry:'2026-06-30', csa:'Cloud & AI Platforms',  cat1:'Data & AI',          cat2:'Data & AI',                                       note:'',             Allen:0, Nick:1, Lucas:0, Aaron:1, Bruno:1 },
  { id:'CR002', name:'(新認證 取代 AI-102)',                                   code:'AI-103', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Data & AI',          cat2:'Data & AI',                                       note:'取代 AI-102',  Allen:0, Nick:0, Lucas:0, Aaron:0, Bruno:0 },
  { id:'CR003', name:'Administrator Expert',                                  code:'MS-102', expiry:'',           csa:'AI Business Solutions', cat1:'Modern Work',        cat2:'Modern Work',                                     note:'',             Allen:1, Nick:1, Lucas:1, Aaron:1, Bruno:0 },
  { id:'CR004', name:'Security Administrator Associate',                      code:'MS-500', expiry:'expired',    csa:'AI Business Solutions', cat1:'Security',           cat2:'Security',                                        note:'已汰換',       Allen:0, Nick:0, Lucas:0, Aaron:1, Bruno:0 },
  { id:'CR005', name:'Microsoft 365 Fundamentals',                            code:'MS-900', expiry:'',           csa:'AI Business Solutions', cat1:'Modern Work',        cat2:'Modern Work',                                     note:'',             Allen:1, Nick:0, Lucas:0, Aaron:1, Bruno:0 },
  { id:'CR006', name:'Microsoft Azure Administrator Certification Transition', code:'AZ-102', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Infra',              cat2:'',                                                note:'',             Allen:0, Nick:0, Lucas:1, Aaron:0, Bruno:0 },
  { id:'CR007', name:'Azure Administrator Associate',                         code:'AZ-104', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Infra',              cat2:'Data & AI/Digital & App Innovation/Infrastructure',note:'',             Allen:1, Nick:1, Lucas:1, Aaron:1, Bruno:0 },
  { id:'CR008', name:'Azure Virtual Desktop Specialty',                       code:'AZ-140', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Infra',              cat2:'Infra',                                           note:'',             Allen:1, Nick:0, Lucas:1, Aaron:0, Bruno:0 },
  { id:'CR009', name:'Developing Solutions for Microsoft Azure',              code:'AZ-204', expiry:'2026-07-31', csa:'Cloud & AI Platforms',  cat1:'Digital & Apps',     cat2:'Digital & App Innovation',                        note:'',             Allen:1, Nick:0, Lucas:0, Aaron:0, Bruno:0 },
  { id:'CR010', name:'(AI-200 取代 AZ-204)',                                  code:'AI-200', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Digital & Apps',     cat2:'Digital & App Innovation',                        note:'取代 AZ-204',  Allen:0, Nick:0, Lucas:0, Aaron:0, Bruno:0 },
  { id:'CR011', name:'Azure IoT Developer Specialty',                         code:'AZ-220', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Digital & Apps',     cat2:'Digital & Apps',                                  note:'',             Allen:0, Nick:0, Lucas:1, Aaron:0, Bruno:0 },
  { id:'CR012', name:'Azure Solutions Architect Expert',                      code:'AZ-305', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Infra',              cat2:'Data & AI',                                       note:'',             Allen:1, Nick:1, Lucas:1, Aaron:1, Bruno:0 },
  { id:'CR013', name:'Designing and Implementing Microsoft DevOps Solutions', code:'AZ-400', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Digital & Apps',     cat2:'Digital & Apps',                                  note:'',             Allen:1, Nick:0, Lucas:0, Aaron:0, Bruno:0 },
  { id:'CR014', name:'Azure Security Engineer Associate',                     code:'AZ-500', expiry:'2026-08-31', csa:'Security',              cat1:'Security',           cat2:'Security',                                        note:'',             Allen:1, Nick:0, Lucas:1, Aaron:1, Bruno:0 },
  { id:'CR015', name:'邊緣與人工智慧安全工程師助理',                           code:'SC-500', expiry:'',           csa:'Security',              cat1:'Security',           cat2:'Security',                                        note:'取代 AZ-504',  Allen:0, Nick:0, Lucas:0, Aaron:0, Bruno:0 },
  { id:'CR016', name:'Azure Network Engineer Associate',                      code:'AZ-700', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Infra',              cat2:'Infrastructure',                                  note:'',             Allen:1, Nick:0, Lucas:1, Aaron:0, Bruno:0 },
  { id:'CR017', name:'Azure Fundamentals',                                    code:'AZ-900', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Infra',              cat2:'Infrastructure',                                  note:'',             Allen:1, Nick:0, Lucas:1, Aaron:1, Bruno:0 },
  { id:'CR018', name:'Power Platform Functional Consultant Associate',        code:'PL-200', expiry:'',           csa:'AI Business Solutions', cat1:'Power Platform',     cat2:'Business Applications',                           note:'',             Allen:0, Nick:1, Lucas:0, Aaron:0, Bruno:0 },
  { id:'CR019', name:'Power Platform Developer Associate',                    code:'PL-400', expiry:'',           csa:'AI Business Solutions', cat1:'Power Platform',     cat2:'Business Applications/Digital & App Innovation',  note:'',             Allen:0, Nick:1, Lucas:0, Aaron:0, Bruno:0 },
  { id:'CR020', name:'Power Platform Solution Architect Expert',              code:'PL-600', expiry:'',           csa:'AI Business Solutions', cat1:'Power Platform',     cat2:'Business Applications',                           note:'',             Allen:0, Nick:1, Lucas:0, Aaron:0, Bruno:0 },
  { id:'CR021', name:'Azure Data Scientist Associate',                        code:'DP-100', expiry:'2026-08-01', csa:'Cloud & AI Platforms',  cat1:'Data & AI',          cat2:'Data & AI',                                       note:'',             Allen:0, Nick:1, Lucas:0, Aaron:0, Bruno:0 },
  { id:'CR022', name:'機器學習實踐組 MLOps 工程師助理',                        code:'AI-300', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Data & AI',          cat2:'Data & AI',                                       note:'取代 DP-100',  Allen:0, Nick:0, Lucas:0, Aaron:0, Bruno:0 },
  { id:'CR023', name:'Azure Data Engineer Associate',                         code:'DP-203', expiry:'expired',    csa:'Cloud & AI Platforms',  cat1:'Data & AI',          cat2:'Data & AI',                                       note:'已過期',       Allen:0, Nick:0, Lucas:0, Aaron:1, Bruno:0 },
  { id:'CR024', name:'(DP-300 取代 DP-208)',                                  code:'DP-300', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Data & AI',          cat2:'Data & AI',                                       note:'取代 DP-208',  Allen:0, Nick:0, Lucas:0, Aaron:0, Bruno:0 },
  { id:'CR025', name:'Azure Cosmos DB Developer Specialty',                   code:'DP-420', expiry:'',           csa:'Cloud & AI Platforms',  cat1:'Data & AI',          cat2:'Data & AI',                                       note:'',             Allen:0, Nick:0, Lucas:1, Aaron:0, Bruno:0 },
  { id:'CR026', name:'Dynamics 365 Customer Insights (Data) Specialty',      code:'MB-260', expiry:'',           csa:'AI Business Solutions', cat1:'Dynamics 365/Data & AI',cat2:'Business Applications/Data & AI',             note:'',             Allen:0, Nick:0, Lucas:0, Aaron:1, Bruno:0 },
  { id:'CR027', name:'Security Operations Analyst Associate',                 code:'SC-200', expiry:'',           csa:'Security',              cat1:'Security',           cat2:'Security',                                        note:'',             Allen:0, Nick:1, Lucas:1, Aaron:1, Bruno:0 },
  { id:'CR028', name:'Identity and Access Administrator Associate',           code:'SC-300', expiry:'',           csa:'Security',              cat1:'Security',           cat2:'Modern Work',                                     note:'',             Allen:0, Nick:1, Lucas:0, Aaron:0, Bruno:0 },
  { id:'CR029', name:'Administering Information Security in Microsoft 365',   code:'SC-401', expiry:'',           csa:'Security',              cat1:'Security',           cat2:'Security',                                        note:'',             Allen:1, Nick:0, Lucas:1, Aaron:0, Bruno:0 },
  { id:'CR030', name:'Security, Compliance, and Identity Fundamentals',       code:'SC-900', expiry:'',           csa:'Security',              cat1:'Security',           cat2:'Security',                                        note:'',             Allen:0, Nick:1, Lucas:1, Aaron:1, Bruno:0 },
];
// 驗證合計: Allen=11, Nick=11, Lucas=13, Aaron=12, Bruno=1 → 48

function loadCertData(){
  const s=localStorage.getItem('ks_cert_data');
  return s?JSON.parse(s):loadCertDefault();
}
function loadCertDefault(){
  const s=localStorage.getItem('ks_cert_data_default');
  return s?JSON.parse(s):CERT_DATA_DEFAULT.map(r=>({...r}));
}
function saveCertData(d){ localStorage.setItem('ks_cert_data',JSON.stringify(d)); }
function saveCertDataAsDefault(d){ localStorage.setItem('ks_cert_data_default',JSON.stringify(d)); }
function resetCertData(){ localStorage.removeItem('ks_cert_data'); }

function getCertStatus(row){
  if(row.expiry==='expired') return 'expired';
  if(row.expiry && row.expiry!=='expired'){
    const d=new Date(row.expiry);
    const diff=(d-new Date())/(1000*60*60*24);
    if(diff<0) return 'expired';
    if(diff<=180) return 'expiring';
  }
  if(row.name.startsWith('(') || (row.note && row.note.includes('取代'))) return 'new';
  return 'active';
}
