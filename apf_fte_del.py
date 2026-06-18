#!/usr/bin/env python3
# encoding: utf-8
"""
Fix FTE table:
 1. Add th-action to thead
 2. Add td-action (btn-del) to each data row
 3. Update phase-sep colspan 9→10
 4. Insert btn-add rows after each phase group
"""

PATH = "D:/excel_dashboard07 月報/index.html"

with open(PATH, encoding="utf-8") as f:
    lines = f.readlines()

TD_DEL = '          <td class="td-action"><button class="btn-del" onclick="apfT_removeRow(this)">✖</button></td>\n'

# For each data row, the pattern is: the last badge-cell is followed by </tr>
# We identify each row by its unique task-title span content.
# We'll find the closing </tr> of each row and insert td-action before it.

# Also we need:
# - th-action in thead (after the last fte-name-col <th>)
# - phase-sep colspan 9 → 10
# - btn-add rows

def find_line_containing(text, start=0):
    for i in range(start, len(lines)):
        if text in lines[i]:
            return i
    return -1

# ── 1. Thead: add th-action ──────────────────────────────────────
thead_guo = find_line_containing('<th class="fte-name-col"><span class="fte-sub" data-editable="true">Guo</span>')
if thead_guo >= 0:
    lines[thead_guo] = lines[thead_guo].rstrip('\n') + '\n'  # no change needed
    # Insert after thead_guo
    lines.insert(thead_guo + 1, '          <th class="th-action"></th>\n')
    print(f"th-action inserted after line {thead_guo+1}")
else:
    print("WARNING: Guo th not found")

# ── 2. Phase separators: colspan 9→10 ────────────────────────────
for i, line in enumerate(lines):
    if 'class="phase-sep"' in line and 'colspan="9"' in line:
        lines[i] = line.replace('colspan="9"', 'colspan="10"')
        print(f"phase-sep colspan→10 at line {i+1}")
    elif 'class="phase-sep-3"' in line and 'colspan="9"' in line:
        lines[i] = line.replace('colspan="9"', 'colspan="10"')
        print(f"phase-sep-3 colspan→10 at line {i+1}")

# ── 3. Add td-action before </tr> for each data row ──────────────
# Find each row by its unique task title, then find its closing </tr>
row_markers = [
    'AI-103：Developing AI Apps',
    'AB-100：Agentic AI Business Solutions Architect',
    'GH-300：GitHub Copilot Certification',
    'Project Ready Workshop + Labs',
    'Copilot Studio + Azure AI Foundry',
    'Microsoft Fabric IQ',
    'Frontier COE 訓練 + Hypervelocity Engineering',
    'FTE Badge 申請',
]

for marker in row_markers:
    title_line = find_line_containing(marker)
    if title_line < 0:
        print(f"WARNING: '{marker[:30]}' not found")
        continue
    # Find the next </tr> after this title_line
    for j in range(title_line + 1, title_line + 20):
        if j < len(lines) and '        </tr>' in lines[j] and '<td' not in lines[j]:
            lines.insert(j, TD_DEL)
            print(f"td-action inserted before line {j+1} (row: {marker[:30]})")
            break
    else:
        print(f"WARNING: could not find </tr> for '{marker[:30]}'")

# ── 4. Insert btn-add rows after each phase group ─────────────────
# After Phase 1 last row (GH-300), before <!-- Phase separator -->
def add_btn_add_after(marker_text, phase_name, phase_class, insert_after_lines=2):
    """Insert btn-add row after a specific marker row's </tr>"""
    m = find_line_containing(marker_text)
    if m < 0:
        print(f"WARNING: marker '{marker_text[:30]}' not found for btn-add")
        return
    # Find the </tr> for this row
    for j in range(m + 1, m + 20):
        if j < len(lines) and '        </tr>' in lines[j]:
            # Insert the btn-add row after this </tr>
            insert_at = j + 1
            btn_row = f'        <tr class="add-row"><td colspan="10" style="padding:2px 0;"><button class="btn-add" onclick="apfFte_addRow(this,\'{phase_class}\')" style="margin:0 auto;">＋ 新增 {phase_name} 任務</button></td></tr>\n'
            lines.insert(insert_at, btn_row)
            print(f"btn-add ({phase_name}) inserted at line {insert_at+1}")
            break
    else:
        print(f"WARNING: could not find </tr> for btn-add marker '{marker_text[:30]}'")

add_btn_add_after('GH-300：GitHub Copilot Certification', 'Phase 1', 'ph1')
add_btn_add_after('Microsoft Fabric IQ', 'Phase 2', 'ph2')
add_btn_add_after('FTE Badge 申請', 'Phase 3', 'ph3')

with open(PATH, "w", encoding="utf-8") as f:
    f.writelines(lines)

total = sum(1 for l in lines if l.strip())
print(f"\nDone. Total non-empty lines: {total}")
