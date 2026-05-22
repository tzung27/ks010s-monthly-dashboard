// ─────────────────────────────────────────────────────────────
// MS Marketplace 供應項目資料
// ─────────────────────────────────────────────────────────────
const MARKETPLACE_DEFAULT = [
  {id:'mp1', name:'Microsoft Fabric導入服務',                                      code:'fabric',                                 type:'專業服務', updated:'2026-04-07', status:'即時', url:''},
  {id:'mp2', name:'如何用 Microsoft 365 Copilot 加值辦公室生產力',                code:'m365_copilot',                           type:'專業服務', updated:'2026-01-09', status:'即時', url:''},
  {id:'mp3', name:'Business Premium 是企業安全的標配',                             code:'m365_bp',                                type:'專業服務', updated:'2026-01-09', status:'即時', url:''},
  {id:'mp4', name:'智訊雲 - 企業專屬智慧情報與知識管理平台',                        code:'copilot-agent',                          type:'專業服務', updated:'2026-01-08', status:'即時', url:''},
  {id:'mp5', name:'打造第一個位數位同事：Copilot Agent 企業流程自動化快速落地方案', code:'solutionoffering',                       type:'專業服務', updated:'2025-09-15', status:'即時', url:''},
  {id:'mp6', name:'保證上雲！Azure 遷移 SOP 完整實戰 Workshop',                   code:'azure-migration-sop-hands-on-workshop',  type:'專業服務', updated:'2025-09-12', status:'即時', url:''},
  {id:'mp7', name:'企業對話解決方案',                                               code:'copilot-ai-agent',                       type:'專業服務', updated:'2025-09-11', status:'即時', url:''},
  {id:'mp8', name:'全方位雲移轉',                                                   code:'azure-migration',                        type:'專業服務', updated:'2025-08-28', status:'即時', url:''},
];

function loadMarketplace(){
  const s=localStorage.getItem('ks_marketplace');
  return s?JSON.parse(s):JSON.parse(JSON.stringify(MARKETPLACE_DEFAULT));
}
function saveMarketplace(d){localStorage.setItem('ks_marketplace',JSON.stringify(d));}
function resetMarketplace(){localStorage.removeItem('ks_marketplace');}
