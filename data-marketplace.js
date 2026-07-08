// ─────────────────────────────────────────────────────────────
// MS Marketplace 供應項目資料
// ─────────────────────────────────────────────────────────────
const MARKETPLACE_DEFAULT = [
  {id:'mp1', name:'Microsoft Fabric導入服務', code:'fabric', type:'專業服務', updated:'2026-04-07', status:'即時', url:'https://marketplace.microsoft.com/en-us/marketplace/consulting-services/weblinkinternationalinc1604460323575.fabric-preview?tab=Overview&flightCodes=8734fe0a2dfc44f4bb92ddaea51d0f3b'},
  {id:'mp2', name:'如何用 Microsoft 365 Copilot 加值辦公室生產力', code:'m365_copilot', type:'專業服務', updated:'2026-01-09', status:'即時', url:'https://marketplace.microsoft.com/en-us/marketplace/consulting-services/weblinkinternationalinc1604460323575.m365_copilot-preview?tab=Overview&flightCodes=09494a20f56549f6b8a7bf1e7a7c0e97'},
  {id:'mp3', name:'Business Premium 是企業安全的標配', code:'m365_bp', type:'專業服務', updated:'2026-01-09', status:'即時', url:'https://marketplace.microsoft.com/en-us/marketplace/consulting-services/weblinkinternationalinc1604460323575.m365_bp-preview?tab=Overview&flightCodes=47ce8406ed9f466f9bb4dd471eb7a51a'},
  {id:'mp4', name:'智訊雲 - 企業專屬智慧情報與知識管理平台', code:'copilot-agent', type:'專業服務', updated:'2026-01-08', status:'即時', url:'https://marketplace.microsoft.com/en-us/marketplace/consulting-services/weblinkinternationalinc1604460323575.copilot-agent-preview?tab=Overview&flightCodes=088c8e9eda0446cfb47bf41b52f97300'},
  {id:'mp5', name:'打造第一個位數位同事：Copilot Agent 企業流程自動化快速落地方案', code:'solutionoffering', type:'專業服務', updated:'2025-09-15', status:'即時', url:'https://marketplace.microsoft.com/en-us/marketplace/consulting-services/weblinkinternationalinc1604460323575.solutionoffering-preview?tab=Overview&flightCodes=b42ab79c969a4ff2a85e3a0896d536ab'},
  {id:'mp6', name:'保證上雲！Azure 遷移 SOP 完整實戰 Workshop', code:'azure-migration-sop-hands-on-workshop', type:'專業服務', updated:'2025-09-12', status:'即時', url:'https://marketplace.microsoft.com/en-us/marketplace/consulting-services/weblinkinternationalinc1604460323575.azure-migration-sop-hands-on-workshop-preview?tab=Overview&flightCodes=188de80e057449ad855b6197db3a1812'},
  {id:'mp7', name:'企業對話解決方案', code:'copilot-ai-agent', type:'專業服務', updated:'2025-09-11', status:'即時', url:'https://marketplace.microsoft.com/en-us/marketplace/consulting-services/weblinkinternationalinc1604460323575.copilot-ai-agent-preview?tab=Overview&flightCodes=015ed19870d24bd1b7b835274323b9d9'},
  {id:'mp8', name:'全方位雲移轉', code:'azure-migration', type:'專業服務', updated:'2025-08-28', status:'即時', url:'https://marketplace.microsoft.com/en-us/marketplace/consulting-services/weblinkinternationalinc1604460323575.azure-migration-preview?tab=Overview&flightCodes=212ebb47d18145c692b4d16a1be59ade'}
];

function loadMarketplace(){
  const s=localStorage.getItem('ks_marketplace');
  return s?JSON.parse(s):JSON.parse(JSON.stringify(loadMarketplaceDefault()));
}
function saveMarketplace(d){localStorage.setItem('ks_marketplace',JSON.stringify(d));}

// 存為預設：將目前資料存為重置時的基準
function saveMarketplaceAsDefault(d){
  localStorage.setItem('ks_marketplace_default',JSON.stringify(d));
}
// 讀取預設（優先用使用者存的，否則用原始 hardcode）
function loadMarketplaceDefault(){
  const s=localStorage.getItem('ks_marketplace_default');
  return s?JSON.parse(s):JSON.parse(JSON.stringify(MARKETPLACE_DEFAULT));
}
// 重置：回到上次存的預設（或 hardcode）
function resetMarketplace(){
  localStorage.removeItem('ks_marketplace');
}
