#!/usr/bin/env python3
# encoding: utf-8
"""
Fix JS:
 1. Update arch/invest add-function templates to include btn-del
 2. Add apfT_injectDelButtons() - auto-adds del buttons to existing items on edit-mode entry
 3. Call apfT_injectDelButtons() inside apfT_toggleEditMode when entering edit mode
 4. Add apfFte_addRow() function
"""

PATH = "D:/excel_dashboard07 月報/index.html"

with open(PATH, encoding="utf-8") as f:
    c = f.read()

# ── 1. Fix apfArch_addTechCard: include btn-del ────────────────────────────
OLD_TECH = ("card.innerHTML = '<div class=\"tech-card-hdr' + (colorClass ? ' ' + colorClass : '') + '\" data-editable=\"true\" "
            "contenteditable=\"true\">新元件</div><div class=\"tech-card-body\"><div data-editable=\"true\" contenteditable=\"true\">功能說明</div></div>';")
NEW_TECH = ("card.innerHTML = '<div class=\"tech-card-hdr' + (colorClass ? ' ' + colorClass : '') + '\" data-editable=\"true\" "
            "contenteditable=\"true\">新元件</div><div class=\"tech-card-body\"><div data-editable=\"true\" contenteditable=\"true\">功能說明</div></div>"
            "<button class=\"btn-del\" onclick=\"apfT_removeEl(this,\\'.tech-card\\')\">✖ 刪除</button>';")
if OLD_TECH in c:
    c = c.replace(OLD_TECH, NEW_TECH, 1)
    print("apfArch_addTechCard: btn-del added")
else:
    print("WARNING: apfArch_addTechCard template not found")

# ── 2. Fix apfArch_addScCard: include btn-del ──────────────────────────────
OLD_SC = ("card.innerHTML = '<div class=\"sc-card-hdr' + (colorClass ? ' ' + colorClass : '') + '\" data-editable=\"true\" "
          "contenteditable=\"true\">新情境</div><div class=\"sc-card-body\"><div data-editable=\"true\" contenteditable=\"true\">說明內容</div>"
          "<div class=\"sc-goal' + (colorClass ? ' ' + colorClass : '') + '\" data-editable=\"true\" contenteditable=\"true\">目標：</div></div>';")
NEW_SC = ("card.innerHTML = '<div class=\"sc-card-hdr' + (colorClass ? ' ' + colorClass : '') + '\" data-editable=\"true\" "
          "contenteditable=\"true\">新情境</div><div class=\"sc-card-body\"><div data-editable=\"true\" contenteditable=\"true\">說明內容</div>"
          "<div class=\"sc-goal' + (colorClass ? ' ' + colorClass : '') + '\" data-editable=\"true\" contenteditable=\"true\">目標：</div>"
          "<button class=\"btn-del\" onclick=\"apfT_removeEl(this,\\'.sc-card\\')\">✖ 刪除</button></div>';")
if OLD_SC in c:
    c = c.replace(OLD_SC, NEW_SC, 1)
    print("apfArch_addScCard: btn-del added")
else:
    print("WARNING: apfArch_addScCard template not found")

# ── 3. Fix apfArch_addGanttRow: include btn-del ────────────────────────────
OLD_GANTT = ("row.innerHTML = '<div class=\"gantt-label\" data-editable=\"true\" contenteditable=\"true\">新任務</div>"
             "<div class=\"gantt-bars\"><div class=\"gantt-vline-q3\"></div><div class=\"gantt-bar ' + (colorClass || 'dark') + '\" "
             "style=\"left:0%;width:27%;\" data-editable=\"true\" contenteditable=\"true\">說明  ·  $0  ·  1M</div></div>';")
NEW_GANTT = ("row.innerHTML = '<div class=\"gantt-label\" data-editable=\"true\" contenteditable=\"true\">新任務</div>"
             "<div class=\"gantt-bars\"><div class=\"gantt-vline-q3\"></div><div class=\"gantt-bar ' + (colorClass || 'dark') + '\" "
             "style=\"left:0%;width:27%;\" data-editable=\"true\" contenteditable=\"true\">說明  ·  $0  ·  1M</div></div>"
             "<button class=\"btn-del\" onclick=\"apfT_removeEl(this,\\'.gantt-row\\')\">✖</button>';")
if OLD_GANTT in c:
    c = c.replace(OLD_GANTT, NEW_GANTT, 1)
    print("apfArch_addGanttRow: btn-del added")
else:
    print("WARNING: apfArch_addGanttRow template not found")

# ── 4. Fix apfInvest_addCard: include btn-del ──────────────────────────────
OLD_INVEST = ("card.innerHTML = '<div class=\"invest-card-title ' + colorClass + '\" data-editable=\"true\" contenteditable=\"true\">新項目</div>"
              "<div class=\"invest-card-desc ' + colorClass + '\" data-editable=\"true\" contenteditable=\"true\">說明</div>';")
NEW_INVEST = ("card.innerHTML = '<div class=\"invest-card-title ' + colorClass + '\" data-editable=\"true\" contenteditable=\"true\">新項目</div>"
              "<div class=\"invest-card-desc ' + colorClass + '\" data-editable=\"true\" contenteditable=\"true\">說明</div>"
              "<button class=\"btn-del\" onclick=\"apfT_removeEl(this,\\'.invest-card\\')\">✖ 刪除</button>';")
if OLD_INVEST in c:
    c = c.replace(OLD_INVEST, NEW_INVEST, 1)
    print("apfInvest_addCard: btn-del added")
else:
    print("WARNING: apfInvest_addCard template not found")

# ── 5. Fix apfInvest_addKpi: switch to innerHTML with btn-del ─────────────
OLD_KPI = "        item.textContent = '新 KPI 指標';"
NEW_KPI = "        item.innerHTML = '新 KPI 指標 <button class=\"btn-del\" onclick=\"apfT_removeEl(this,\\'.kpi-item\\')\">✖</button>';"
if OLD_KPI in c:
    c = c.replace(OLD_KPI, NEW_KPI, 1)
    print("apfInvest_addKpi: btn-del added")
else:
    print("WARNING: apfInvest_addKpi textContent not found")

# ── 6. Add apfT_injectDelButtons and apfFte_addRow functions ──────────────
NEW_FUNCS = """
    function apfT_injectDelButtons() {
        // Auto-inject btn-del to existing arch/invest items that don't have one
        var tab = document.getElementById('tab-apftransform');
        tab.querySelectorAll('.tech-card').forEach(function(el) {
            if (el.querySelector('.btn-del')) return;
            var b = document.createElement('button');
            b.className = 'btn-del';
            b.textContent = '✖ 刪除';
            b.style.cssText = 'display:block;width:calc(100% - 16px);margin:4px 8px 2px;';
            b.setAttribute('onclick', "apfT_removeEl(this,'.tech-card')");
            el.appendChild(b);
        });
        tab.querySelectorAll('.sc-card').forEach(function(el) {
            if (el.querySelector('.btn-del')) return;
            var b = document.createElement('button');
            b.className = 'btn-del';
            b.textContent = '✖ 刪除';
            b.style.cssText = 'display:block;width:calc(100% - 16px);margin:4px 8px 2px;';
            b.setAttribute('onclick', "apfT_removeEl(this,'.sc-card')");
            el.appendChild(b);
        });
        tab.querySelectorAll('.gantt-row').forEach(function(el) {
            if (el.querySelector('.btn-del')) return;
            var b = document.createElement('button');
            b.className = 'btn-del';
            b.textContent = '✖';
            b.style.cssText = 'flex-shrink:0;height:22px;margin-left:4px;';
            b.setAttribute('onclick', "apfT_removeEl(this,'.gantt-row')");
            el.appendChild(b);
        });
        tab.querySelectorAll('.invest-card').forEach(function(el) {
            if (el.querySelector('.btn-del')) return;
            var b = document.createElement('button');
            b.className = 'btn-del';
            b.textContent = '✖ 刪除';
            b.style.cssText = 'display:block;width:calc(100% - 16px);margin:4px 8px 2px;';
            b.setAttribute('onclick', "apfT_removeEl(this,'.invest-card')");
            el.appendChild(b);
        });
        tab.querySelectorAll('.kpi-item').forEach(function(el) {
            if (el.querySelector('.btn-del')) return;
            var b = document.createElement('button');
            b.className = 'btn-del';
            b.textContent = '✖';
            b.style.cssText = 'margin-left:4px;vertical-align:middle;';
            b.setAttribute('onclick', "apfT_removeEl(this,'.kpi-item')");
            el.appendChild(b);
        });
    }

    function apfFte_addRow(btn, phaseClass) {
        if (!apfT_isEditMode) return;
        var phaseNum = phaseClass === 'ph1' ? '1' : phaseClass === 'ph2' ? '2' : '3';
        var tr = document.createElement('tr');
        tr.className = 'row-' + phaseClass + ' row-' + phaseClass + '-a';
        tr.innerHTML = '<td class="phase-cell" data-editable="true" contenteditable="true">Phase ' + phaseNum + '</td>'
            + '<td class="task-cell"><span class="task-title" data-editable="true" contenteditable="true">新任務名稱</span>'
            + '<span class="task-desc" data-editable="true" contenteditable="true">說明</span></td>'
            + '<td class="fte-host" data-editable="true" contenteditable="true">平台</td>'
            + '<td class="url-cell" data-editable="true" contenteditable="true">連結</td>'
            + '<td class="badge-cell"><div class="fte-badge ' + phaseClass + '" data-editable="true" contenteditable="true">必修</div></td>'
            + '<td class="badge-cell"><div class="fte-badge ' + phaseClass + '" data-editable="true" contenteditable="true">必修</div></td>'
            + '<td class="badge-cell"><div class="fte-badge ' + phaseClass + '" data-editable="true" contenteditable="true">必修</div></td>'
            + '<td class="badge-cell"><div class="fte-badge ' + phaseClass + '" data-editable="true" contenteditable="true">必修</div></td>'
            + '<td class="badge-cell"><div class="fte-badge ' + phaseClass + '" data-editable="true" contenteditable="true">必修</div></td>'
            + '<td class="td-action"><button class="btn-del" onclick="apfT_removeRow(this)">✖</button></td>';
        btn.closest('tr').parentNode.insertBefore(tr, btn.closest('tr'));
    }
"""

# Insert after apfT_removeRow function
INSERT_ANCHOR = "    function apfT_removeRow(btn) {\n        if(!apfT_isEditMode) return;\n        btn.closest('tr').remove();\n        apfT_recalculateAll();\n    }"
if INSERT_ANCHOR in c:
    c = c.replace(INSERT_ANCHOR, INSERT_ANCHOR + '\n' + NEW_FUNCS, 1)
    print("apfT_injectDelButtons + apfFte_addRow added")
else:
    print("WARNING: insert anchor not found")

# ── 7. Call apfT_injectDelButtons when entering edit mode ────────────────
OLD_ENTER_EDIT = "        const editables = document.querySelectorAll('[data-editable]');\n        editables.forEach(el => {\n            if(apfT_isEditMode) {"
NEW_ENTER_EDIT = "        if(apfT_isEditMode) { apfT_injectDelButtons(); }\n        const editables = document.querySelectorAll('[data-editable]');\n        editables.forEach(el => {\n            if(apfT_isEditMode) {"
if OLD_ENTER_EDIT in c:
    c = c.replace(OLD_ENTER_EDIT, NEW_ENTER_EDIT, 1)
    print("apfT_toggleEditMode: injectDelButtons hook added")
else:
    print("WARNING: toggleEditMode editables anchor not found")

with open(PATH, "w", encoding="utf-8") as f:
    f.write(c)
print(f"\nDone. Lines: {c.count(chr(10))}")
