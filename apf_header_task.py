#!/usr/bin/env python3
# encoding: utf-8
"""
Insert 任務配置與關鍵期程 table into the right side of the 業務計畫 header area.
"""

PATH = "D:/excel_dashboard07 月報/index.html"

with open(PATH, encoding="utf-8") as f:
    c = f.read()

# ── 1. CSS ──────────────────────────────────────────────────────────────────
CSS = """
/* ── 任務配置與關鍵期程 header panel ── */
#tab-apftransform .header-task-panel {
  flex: 0 0 auto;
  margin-left: auto;
  min-width: 340px;
  max-width: 440px;
  align-self: flex-start;
}
#tab-apftransform .htask-hdr {
  background: linear-gradient(90deg, #2D2477 0%, #4B3CA7 100%);
  color: white;
  padding: 7px 12px;
  border-radius: 7px 7px 0 0;
  font-size: 12px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 7px;
  letter-spacing: 0.3px;
}
#tab-apftransform .htask-hdr svg { flex-shrink: 0; }
#tab-apftransform .htask-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 10px;
  border: 1.5px solid #C4BEE8;
  border-top: none;
  border-radius: 0 0 7px 7px;
}
#tab-apftransform .htask-table thead th {
  background: #EAE8F7;
  color: #2D2477;
  padding: 5px 7px;
  text-align: left;
  font-weight: 700;
  border-right: 1px solid #C4BEE8;
  border-bottom: 1.5px solid #C4BEE8;
  white-space: nowrap;
}
#tab-apftransform .htask-table thead th:last-child { border-right: none; }
#tab-apftransform .htask-table tbody tr:nth-child(odd)  { background: #FFFFFF; }
#tab-apftransform .htask-table tbody tr:nth-child(even) { background: #F5F3FC; }
#tab-apftransform .htask-table tbody tr:hover { background: #ECEAF8; }
#tab-apftransform .htask-table tbody td {
  padding: 5px 7px;
  border-bottom: 1px solid #E4E0F5;
  border-right: 1px solid #E4E0F5;
  vertical-align: top;
  line-height: 1.4;
  color: #2A2A3A;
}
#tab-apftransform .htask-table tbody td:last-child { border-right: none; }
#tab-apftransform .htask-table tbody tr:last-child td { border-bottom: none; }
#tab-apftransform .htask-date-cell { display:flex; align-items:flex-start; gap:5px; }
#tab-apftransform .htask-icon-ring {
  width: 24px; height: 24px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0; margin-top: 1px;
}
#tab-apftransform .htask-icon-ring.cal { background: #E3EEFF; }
#tab-apftransform .htask-icon-ring.msg { background: #E6F5EA; }
#tab-apftransform .htask-icon-ring.doc { background: #FFF3E0; }
#tab-apftransform .htask-icon-ring.pen { background: #FDEAED; }
#tab-apftransform .htask-date-info { }
#tab-apftransform .htask-date-main { font-weight: 700; font-size: 11px; color: #0A2540; line-height: 1.2; }
#tab-apftransform .htask-date-sub  { font-size: 9px; color: #6B6B8A; line-height: 1.2; margin-top: 1px; }
#tab-apftransform .htask-table .htask-task { font-weight: 500; color: #1A1A2E; }
#tab-apftransform .htask-table .htask-note { color: #555570; font-size: 9.5px; }
#tab-apftransform .htask-add-row {
  display: none;
  padding: 3px 7px;
  border: 1px dashed #9B93D9;
  border-top: none;
  border-radius: 0 0 7px 7px;
  text-align: center;
}
#tab-apftransform.apf-editing .htask-add-row { display: block; }
#tab-apftransform .htask-table .td-action {
  width: 20px; padding: 2px; text-align: center; vertical-align: middle;
  border-right: none;
}
"""

STYLE_END = '</style>'
style_end_pos = c.find(STYLE_END, c.find('<style id="apf-transform-styles">'))
if style_end_pos > 0 and 'htask-hdr' not in c:
    c = c[:style_end_pos] + CSS + c[style_end_pos:]
    print("CSS injected")
else:
    print("CSS already present or style end not found")

# ── 2. HTML ──────────────────────────────────────────────────────────────────
# SVG icons (14x14, stroke-based)
CAL_ICON = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#3B5BBD" stroke-width="2.2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>'
MSG_ICON = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#2E7D32" stroke-width="2.2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>'
DOC_ICON = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#E65100" stroke-width="2.2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>'
PEN_ICON = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#C62828" stroke-width="2.2"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>'
CAL_HDR  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>'

def date_cell(icon_html, icon_cls, date_main, date_sub=""):
    sub = f'<span class="htask-date-sub" data-editable="true">{date_sub}</span>' if date_sub else ''
    return (f'<td><div class="htask-date-cell">'
            f'<div class="htask-icon-ring {icon_cls}">{icon_html}</div>'
            f'<div class="htask-date-info">'
            f'<span class="htask-date-main" data-editable="true">{date_main}</span>{sub}'
            f'</div></div></td>')

def task_row(date_td, task, owner, note, row_id):
    return (f'<tr id="htask-row-{row_id}">'
            f'{date_td}'
            f'<td class="htask-task" data-editable="true">{task}</td>'
            f'<td data-editable="true">{owner}</td>'
            f'<td class="htask-note" data-editable="true">{note}</td>'
            f'<td class="td-action"><button class="btn-del" onclick="apfT_removeRow(this)">✖</button></td>'
            f'</tr>')

TASK_HTML = f'''
            <div class="header-task-panel">
              <div class="htask-hdr">
                {CAL_HDR}
                <span data-editable="true">任務配置與關鍵期程</span>
              </div>
              <table class="htask-table" id="htask-table">
                <thead>
                  <tr>
                    <th data-editable="true">截止日期</th>
                    <th data-editable="true">任務事項</th>
                    <th data-editable="true">負責人</th>
                    <th data-editable="true">備註</th>
                    <th class="th-action"></th>
                  </tr>
                </thead>
                <tbody>
                  {task_row(date_cell(CAL_ICON,'cal','6/23','(週二)'), '與 Allen Chung 完成三大方向初步想法討論，提交初稿', 'Partner 內部 + Cindy Wu', 'Cindy 下週一召集討論', 1)}
                  {task_row(date_cell(CAL_ICON,'cal','6/30',''), 'SPF 草約送法務開始審查', 'Partner 法務', '條款不可修改', 2)}
                  {task_row(date_cell(MSG_ICON,'msg','7/1','週開始'), 'Microsoft QC / Feedback Sessions 啟動', 'Microsoft PDM + Partner', '鼓勵提前提交以取得回饋', 3)}
                  {task_row(date_cell(DOC_ICON,'doc','7/31',''), 'Transform Business Plan 最終版提交', 'Partner', 'Transform 合約同期簽署', 4)}
                  {task_row(date_cell(PEN_ICON,'pen','9/30',''), 'Perform 合約簽署截止 (追溯至 7/1)', 'Partner', '逾期喪失 Q1 追溯款項資格', 5)}
                </tbody>
              </table>
              <div class="htask-add-row">
                <button class="btn-add" onclick="apfHtask_addRow()">＋ 新增任務</button>
              </div>
            </div>'''

# Insert after </div><!-- end header-meta-boxes --> i.e. after the closing of header-meta-boxes
# The header-meta-boxes ends just before </div> which closes header-top.
# We identify the anchor: end of the confidential-tag line inside header-meta-boxes.
OLD_HDR_END = '            </div>\n        </div>\n\n        <div style="display:flex; justify-content:space-between;'
NEW_HDR_END = '            </div>\n' + TASK_HTML + '\n        </div>\n\n        <div style="display:flex; justify-content:space-between;'

if OLD_HDR_END in c:
    c = c.replace(OLD_HDR_END, NEW_HDR_END, 1)
    print("Task panel HTML inserted")
else:
    # Alternative anchor
    ALT = '                </div>\n            </div>\n        </div>\n\n        <div style="display:flex; justify-content:space-between;'
    if ALT in c:
        c = c.replace(ALT, '                </div>\n            </div>\n' + TASK_HTML + '\n        </div>\n\n        <div style="display:flex; justify-content:space-between;', 1)
        print("Task panel HTML inserted (alt anchor)")
    else:
        print("WARNING: anchor not found - checking structure...")
        # Debug: find confidential tag
        idx = c.find('Microsoft Confidential')
        if idx > 0:
            print(f"Confidential tag found at char {idx}")
            print(repr(c[idx:idx+200]))

# ── 3. Add apfHtask_addRow JS function ───────────────────────────────────────
NEW_HTASK_FN = """
    function apfHtask_addRow() {
        if (!apfT_isEditMode) return;
        var tbody = document.querySelector('#htask-table tbody');
        var tr = document.createElement('tr');
        tr.innerHTML = '<td><div class="htask-date-cell">'
            + '<div class="htask-icon-ring cal"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#3B5BBD" stroke-width="2.2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg></div>'
            + '<div class="htask-date-info"><span class="htask-date-main" data-editable="true" contenteditable="true">M/DD</span><span class="htask-date-sub" data-editable="true" contenteditable="true"></span></div>'
            + '</div></td>'
            + '<td class="htask-task" data-editable="true" contenteditable="true">任務說明</td>'
            + '<td data-editable="true" contenteditable="true">負責人</td>'
            + '<td class="htask-note" data-editable="true" contenteditable="true">備註</td>'
            + '<td class="td-action"><button class="btn-del" onclick="apfT_removeRow(this)">✖</button></td>';
        tbody.appendChild(tr);
    }
"""

# Insert after apfFte_addRow function
FTE_FN_ANCHOR = "    function apfFte_addRow(btn, phaseClass) {"
fn_start = c.find(FTE_FN_ANCHOR)
if fn_start > 0:
    fn_end = c.find('\n    }', fn_start) + len('\n    }')
    if 'apfHtask_addRow' not in c:
        c = c[:fn_end] + '\n' + NEW_HTASK_FN + c[fn_end:]
        print("apfHtask_addRow JS added")
    else:
        print("apfHtask_addRow already present")
else:
    print("WARNING: apfFte_addRow not found")

with open(PATH, "w", encoding="utf-8") as f:
    f.write(c)
print(f"\nDone. Lines: {c.count(chr(10))}")
