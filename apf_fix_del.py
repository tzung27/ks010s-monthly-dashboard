#!/usr/bin/env python3
# encoding: utf-8
"""
Fix 1: FTE table - add btn-del to each row, add btn-add after each phase group
Fix 2: arch/invest add-function JS templates - include btn-del in new items
Fix 3: arch/invest EXISTING items - add btn-del
"""

PATH = "D:/excel_dashboard07 月報/index.html"

with open(PATH, encoding="utf-8") as f:
    c = f.read()

# ══════════════════════════════════════════════════════════════════
# 1. FTE TABLE: add th-action header + td-action+del per row + btn-add per phase
# ══════════════════════════════════════════════════════════════════

# 1a. Add th-action to thead
OLD_TH = '          <th class="fte-name-col"><span class="fte-sub" data-editable="true">Guo</span><span data-editable="true">FTE05</span></th>\n        </tr>\n      </thead>'
NEW_TH = '          <th class="fte-name-col"><span class="fte-sub" data-editable="true">Guo</span><span data-editable="true">FTE05</span></th>\n          <th class="th-action"></th>\n        </tr>\n      </thead>'
if OLD_TH in c:
    c = c.replace(OLD_TH, NEW_TH, 1)
    print("FTE: th-action added")
else:
    print("WARNING: FTE thead anchor not found")

# helper: add td-action del to each phase row
def add_del_to_rows(content, phase_rows_marker, del_html):
    """For each </tr> that belongs to a phase row, append a td-action before </tr>"""
    return content

# 1b. Add td-action to each Phase 1 row (3 rows)
for old_badge, phase_label in [
    # Phase 1 row 1
    ('          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n        </tr>\n        <tr class="row-ph1 row-ph1-b">',
     'ph1-a->b'),
    # Phase 1 row 2
    ('          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n        </tr>\n        <tr class="row-ph1 row-ph1-a">',
     'ph1-b->a'),
]:
    new_badge = old_badge.replace(
        '          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n        </tr>',
        '          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="td-action"><button class="btn-del" onclick="apfT_removeRow(this)">✖</button></td>\n        </tr>'
    )
    if old_badge in c:
        c = c.replace(old_badge, new_badge, 1)
        print(f"FTE: {phase_label} del added")
    else:
        print(f"WARNING: {phase_label} not found")

# Phase 1 last row (GH-300) -> before phase-sep
OLD_PH1_LAST = '          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n        </tr>\n        <!-- Phase separator -->'
NEW_PH1_LAST = '          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph1" data-editable="true">必修</div></td>\n          <td class="td-action"><button class="btn-del" onclick="apfT_removeRow(this)">✖</button></td>\n        </tr>\n        <tr class="add-row"><td colspan="10" style="padding:2px 0;"><button class="btn-add" onclick="apfFte_addRow(this,\'ph1\')">＋ 新增 Phase 1 任務</button></td></tr>\n        <!-- Phase separator -->'
if OLD_PH1_LAST in c:
    c = c.replace(OLD_PH1_LAST, NEW_PH1_LAST, 1)
    print("FTE: Phase 1 last row del + btn-add added")
else:
    print("WARNING: Phase 1 last row not found")

# Phase 2 rows (3 rows) - add td-action del
# row-ph2-a (first)
OLD_PH2_A1 = '          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n        </tr>\n        <tr class="row-ph2 row-ph2-b">'
NEW_PH2_A1 = '          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="td-action"><button class="btn-del" onclick="apfT_removeRow(this)">✖</button></td>\n        </tr>\n        <tr class="row-ph2 row-ph2-b">'
if OLD_PH2_A1 in c:
    c = c.replace(OLD_PH2_A1, NEW_PH2_A1, 1)
    print("FTE: Phase 2 row-a del added")
else:
    print("WARNING: Phase 2 row-a not found")

OLD_PH2_B = '          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n        </tr>\n        <tr class="row-ph2 row-ph2-a">'
NEW_PH2_B = '          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="td-action"><button class="btn-del" onclick="apfT_removeRow(this)">✖</button></td>\n        </tr>\n        <tr class="row-ph2 row-ph2-a">'
if OLD_PH2_B in c:
    c = c.replace(OLD_PH2_B, NEW_PH2_B, 1)
    print("FTE: Phase 2 row-b del added")
else:
    print("WARNING: Phase 2 row-b not found")

# Phase 2 last row -> before phase-sep-3
OLD_PH2_LAST = '          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n        </tr>\n        <!-- Phase 3 separator -->'
NEW_PH2_LAST = '          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph2" data-editable="true">必修</div></td>\n          <td class="td-action"><button class="btn-del" onclick="apfT_removeRow(this)">✖</button></td>\n        </tr>\n        <tr class="add-row"><td colspan="10" style="padding:2px 0;"><button class="btn-add" onclick="apfFte_addRow(this,\'ph2\')">＋ 新增 Phase 2 任務</button></td></tr>\n        <!-- Phase 3 separator -->'
if OLD_PH2_LAST in c:
    c = c.replace(OLD_PH2_LAST, NEW_PH2_LAST, 1)
    print("FTE: Phase 2 last row del + btn-add added")
else:
    print("WARNING: Phase 2 last row not found")

# Phase 3 row 1 (Frontier COE)
OLD_PH3_A = '          <td class="badge-cell"><div class="fte-badge ph3" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph3" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph3" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph3" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph3" data-editable="true">必修</div></td>\n        </tr>\n        <tr class="row-badge">'
NEW_PH3_A = '          <td class="badge-cell"><div class="fte-badge ph3" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph3" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph3" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph3" data-editable="true">必修</div></td>\n          <td class="badge-cell"><div class="fte-badge ph3" data-editable="true">必修</div></td>\n          <td class="td-action"><button class="btn-del" onclick="apfT_removeRow(this)">✖</button></td>\n        </tr>\n        <tr class="row-badge">'
if OLD_PH3_A in c:
    c = c.replace(OLD_PH3_A, NEW_PH3_A, 1)
    print("FTE: Phase 3 row-a del added")
else:
    print("WARNING: Phase 3 row-a not found")

# Phase 3 last row (FTE Badge goal) -> after it add btn-add
OLD_PH3_LAST = '          <td class="badge-cell"><div class="fte-badge goal" data-editable="true">目標</div></td>\n          <td class="badge-cell"><div class="fte-badge goal" data-editable="true">目標</div></td>\n          <td class="badge-cell"><div class="fte-badge goal" data-editable="true">目標</div></td>\n          <td class="badge-cell"><div class="fte-badge goal" data-editable="true">目標</div></td>\n          <td class="badge-cell"><div class="fte-badge goal" data-editable="true">目標</div></td>\n        </tr>\n      </tbody>'
NEW_PH3_LAST = '          <td class="badge-cell"><div class="fte-badge goal" data-editable="true">目標</div></td>\n          <td class="badge-cell"><div class="fte-badge goal" data-editable="true">目標</div></td>\n          <td class="badge-cell"><div class="fte-badge goal" data-editable="true">目標</div></td>\n          <td class="badge-cell"><div class="fte-badge goal" data-editable="true">目標</div></td>\n          <td class="badge-cell"><div class="fte-badge goal" data-editable="true">目標</div></td>\n          <td class="td-action"><button class="btn-del" onclick="apfT_removeRow(this)">✖</button></td>\n        </tr>\n        <tr class="add-row"><td colspan="10" style="padding:2px 0;"><button class="btn-add" onclick="apfFte_addRow(this,\'ph3\')">＋ 新增 Phase 3 任務</button></td></tr>\n      </tbody>'
if OLD_PH3_LAST in c:
    c = c.replace(OLD_PH3_LAST, NEW_PH3_LAST, 1)
    print("FTE: Phase 3 last row del + btn-add added")
else:
    print("WARNING: Phase 3 last row not found")

# ══════════════════════════════════════════════════════════════════
# 2. JS: add apfFte_addRow function
# ══════════════════════════════════════════════════════════════════
NEW_FTE_FN = """
    function apfFte_addRow(btn, phaseClass) {
        if (!apfT_isEditMode) return;
        var phaseColors = { ph1:'row-ph1 row-ph1-a', ph2:'row-ph2 row-ph2-a', ph3:'row-ph3 row-ph3-a' };
        var badgeClasses = { ph1:'ph1', ph2:'ph2', ph3:'ph3' };
        var cls = phaseColors[phaseClass] || 'row-ph1 row-ph1-a';
        var badge = badgeClasses[phaseClass] || 'ph1';
        var tr = document.createElement('tr');
        tr.className = cls;
        tr.innerHTML = '<td class="phase-cell" data-editable="true" contenteditable="true">Phase ' + (phaseClass==='ph1'?'1':phaseClass==='ph2'?'2':'3') + '</td>'
            + '<td class="task-cell"><span class="task-title" data-editable="true" contenteditable="true">新任務名稱</span><span class="task-desc" data-editable="true" contenteditable="true">說明</span></td>'
            + '<td class="fte-host" data-editable="true" contenteditable="true">平台</td>'
            + '<td class="url-cell" data-editable="true" contenteditable="true">連結</td>'
            + '<td class="badge-cell"><div class="fte-badge ' + badge + '" data-editable="true" contenteditable="true">必修</div></td>'
            + '<td class="badge-cell"><div class="fte-badge ' + badge + '" data-editable="true" contenteditable="true">必修</div></td>'
            + '<td class="badge-cell"><div class="fte-badge ' + badge + '" data-editable="true" contenteditable="true">必修</div></td>'
            + '<td class="badge-cell"><div class="fte-badge ' + badge + '" data-editable="true" contenteditable="true">必修</div></td>'
            + '<td class="badge-cell"><div class="fte-badge ' + badge + '" data-editable="true" contenteditable="true">必修</div></td>'
            + '<td class="td-action"><button class="btn-del" onclick="apfT_removeRow(this)">✖</button></td>';
        // Insert before the btn-add row (btn.closest('tr'))
        var addRow = btn.closest('tr');
        addRow.parentNode.insertBefore(tr, addRow);
    }
"""
JS_ANCHOR = 'function apfFte_addRow'
if JS_ANCHOR not in c:
    # insert after apfInvest_addKpi
    KPI_END = c.find('\n    function apfInvest_addKpi')
    end_fn = c.find('\n    }', KPI_END + 10) + len('\n    }')
    c = c[:end_fn] + '\n' + NEW_FTE_FN + c[end_fn:]
    print("JS: apfFte_addRow added")
else:
    print("JS: apfFte_addRow already exists")

# ══════════════════════════════════════════════════════════════════
# 3. Fix JS add functions to include btn-del in created elements
# ══════════════════════════════════════════════════════════════════

# apfArch_addTechCard - add btn-del to card
OLD_TECH_TPL = "card.innerHTML = '<div class=\"tech-card-hdr' + (colorClass ? ' ' + colorClass : '') + '\" data-editable=\"true\" contenteditable=\"true\">新元件</div><div class=\"tech-card-body\"><div data-editable=\"true\" contenteditable=\"true\">功能說明</div></div>';"
NEW_TECH_TPL = "card.innerHTML = '<div class=\"tech-card-hdr' + (colorClass ? ' ' + colorClass : '') + '\" data-editable=\"true\" contenteditable=\"true\">新元件</div><div class=\"tech-card-body\"><div data-editable=\"true\" contenteditable=\"true\">功能說明</div></div><button class=\"btn-del\" onclick=\"apfT_removeEl(this,\\'.tech-card\\')\" style=\"display:block;margin:4px auto 2px;width:90%;\">✖ 刪除</button>';"
if OLD_TECH_TPL in c:
    c = c.replace(OLD_TECH_TPL, NEW_TECH_TPL, 1)
    print("JS: apfArch_addTechCard btn-del added")
else:
    print("WARNING: apfArch_addTechCard template not found")

# apfArch_addScCard - add btn-del to card
OLD_SC_TPL = "card.innerHTML = '<div class=\"sc-card-hdr' + (colorClass ? ' ' + colorClass : '') + '\" data-editable=\"true\" contenteditable=\"true\">新情境</div><div class=\"sc-card-body\"><div data-editable=\"true\" contenteditable=\"true\">說明內容</div><div class=\"sc-goal' + (colorClass ? ' ' + colorClass : '') + '\" data-editable=\"true\" contenteditable=\"true\">目標：</div></div>';"
NEW_SC_TPL = "card.innerHTML = '<div class=\"sc-card-hdr' + (colorClass ? ' ' + colorClass : '') + '\" data-editable=\"true\" contenteditable=\"true\">新情境</div><div class=\"sc-card-body\"><div data-editable=\"true\" contenteditable=\"true\">說明內容</div><div class=\"sc-goal' + (colorClass ? ' ' + colorClass : '') + '\" data-editable=\"true\" contenteditable=\"true\">目標：</div><button class=\"btn-del\" onclick=\"apfT_removeEl(this,\\'.sc-card\\')\" style=\"margin-top:4px;width:100%;\">✖ 刪除</button></div>';"
if OLD_SC_TPL in c:
    c = c.replace(OLD_SC_TPL, NEW_SC_TPL, 1)
    print("JS: apfArch_addScCard btn-del added")
else:
    print("WARNING: apfArch_addScCard template not found")

# apfArch_addGanttRow - add btn-del to row
OLD_GANTT_TPL = "row.innerHTML = '<div class=\"gantt-label\" data-editable=\"true\" contenteditable=\"true\">新任務</div><div class=\"gantt-bars\"><div class=\"gantt-vline-q3\"></div><div class=\"gantt-bar ' + (colorClass || 'dark') + '\" style=\"left:0%;width:27%;\" data-editable=\"true\" contenteditable=\"true\">說明  ·  $0  ·  1M</div></div>';"
NEW_GANTT_TPL = "row.innerHTML = '<div class=\"gantt-label\" data-editable=\"true\" contenteditable=\"true\">新任務</div><div class=\"gantt-bars\"><div class=\"gantt-vline-q3\"></div><div class=\"gantt-bar ' + (colorClass || 'dark') + '\" style=\"left:0%;width:27%;\" data-editable=\"true\" contenteditable=\"true\">說明  ·  $0  ·  1M</div></div><button class=\"btn-del\" onclick=\"apfT_removeEl(this,\\'.gantt-row\\')\" style=\"flex-shrink:0;height:22px;margin-left:4px;\">✖</button>';"
if OLD_GANTT_TPL in c:
    c = c.replace(OLD_GANTT_TPL, NEW_GANTT_TPL, 1)
    print("JS: apfArch_addGanttRow btn-del added")
else:
    print("WARNING: apfArch_addGanttRow template not found")

# apfInvest_addCard - add btn-del
OLD_INVEST_TPL = "card.innerHTML = '<div class=\"invest-card-title ' + colorClass + '\" data-editable=\"true\" contenteditable=\"true\">新項目</div><div class=\"invest-card-desc ' + colorClass + '\" data-editable=\"true\" contenteditable=\"true\">說明</div>';"
NEW_INVEST_TPL = "card.innerHTML = '<div class=\"invest-card-title ' + colorClass + '\" data-editable=\"true\" contenteditable=\"true\">新項目</div><div class=\"invest-card-desc ' + colorClass + '\" data-editable=\"true\" contenteditable=\"true\">說明</div><button class=\"btn-del\" onclick=\"apfT_removeEl(this,\\'.invest-card\\')\" style=\"margin-top:4px;width:100%;\">✖ 刪除</button>';"
if OLD_INVEST_TPL in c:
    c = c.replace(OLD_INVEST_TPL, NEW_INVEST_TPL, 1)
    print("JS: apfInvest_addCard btn-del added")
else:
    print("WARNING: apfInvest_addCard template not found")

# apfInvest_addKpi - add btn-del inline
OLD_KPI_TPL = "    item.textContent = '新 KPI 指標';\n        btn.parentNode.insertBefore(item, btn);"
NEW_KPI_TPL = "    item.innerHTML = '新 KPI 指標 <button class=\"btn-del\" onclick=\"apfT_removeEl(this,\\'.kpi-item\\')\">✖</button>';\n        btn.parentNode.insertBefore(item, btn);"
if OLD_KPI_TPL in c:
    c = c.replace(OLD_KPI_TPL, NEW_KPI_TPL, 1)
    print("JS: apfInvest_addKpi btn-del added")
else:
    print("WARNING: apfInvest_addKpi template not found")

# ══════════════════════════════════════════════════════════════════
# 4. gantt-row CSS: add flex display so btn-del aligns correctly
# ══════════════════════════════════════════════════════════════════
OLD_GR_CSS = '#tab-apftransform .gantt-row { display:flex; align-items:center; min-height:32px; border-bottom:1px solid #F0F0F0; }'
NEW_GR_CSS = '#tab-apftransform .gantt-row { display:flex; align-items:center; min-height:32px; border-bottom:1px solid #F0F0F0; }\n#tab-apftransform .gantt-row .btn-del { flex-shrink:0; height:22px; margin-left:4px; }'
if OLD_GR_CSS in c:
    c = c.replace(OLD_GR_CSS, NEW_GR_CSS, 1)
    print("CSS: gantt-row btn-del flex added")
else:
    print("CSS: gantt-row already has btn-del or not found")

with open(PATH, "w", encoding="utf-8") as f:
    f.write(c)
print(f"\nDone. Lines: {c.count(chr(10))}")
