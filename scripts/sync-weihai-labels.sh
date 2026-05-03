#!/bin/bash
# 威海标签贴膜文件同步到飞书知识库
# 目标知识库节点: LhlUwJt5ViLPhZkrknLcHzV4nwc (标签贴膜设计)
# 临时文件夹: fldcnRPjh6QcMmwt4l61XoCDfqd

SPACE_ID="7632924686837418976"
PARENT_NODE="LhlUwJt5ViLPhZkrknLcHzV4nwc"
TEMP_FOLDER="fldcnRPjh6QcMmwt4l61XoCDfqd"
LOG_FILE="scripts/sync-weihai-labels.log"
RESULT_FILE="scripts/sync-weihai-labels-result.tsv"

# 初始化结果文件
echo -e "原始token\t文件名\t副本token\twiki_node_token\t状态" > "$RESULT_FILE"
echo "=== 威海标签贴膜同步开始 $(date) ===" > "$LOG_FILE"

# 文件列表: token<TAB>文件名
# 注意：第一个文件 模型.skp 已经手动测试成功，跳过
FILES=(
"boxcnjRj2VKAnuJeyXxcLGdKNdc	贴膜-转曲.pdf"
"boxcnl4rts8j0vxg8KwYvWWEMcH	1.png"
"boxcnR40sl2sXGcRV1xGd86kFGe	1-2.psd"
"boxcnWIoya5ih9tEnGSONadv8Ae	贴膜-转曲.ai"
"boxcno7C5qxNp1HYEgqGZ3n8dLe	2.png"
"boxcntJsgOlPAAQC2JKWvJdZ7jS	b8389b504fc2d56209c309e6e91190ef77c66cf6.png"
"boxcn22lrhP0tusMxtJUekJ6kuc	1-2.png"
"boxcnIcEgy1JavUBJ1p3PSxAPpb	贴膜v4-转曲.ai"
"boxcnWlLrZjzxvfbw7eOO3vxZEb	1.psd"
"boxcnoII2s5OxgmNuMptfcaS8Af	贴膜v5-转曲-灰底.ai"
"boxcnbkXhTpbmEHb1U9MsUq6B7A	1-1.png"
"boxcnUOG5EQCN7kKdBsVJ4GybAb	贴膜v5-转曲-02.png"
"boxcnK3WTFtXY9x1MSp880Ws3gb	2021_logo1.png"
"boxcn5H9t8F0LgzlcyRANzlt9Fe	WechatIMG3513.jpeg"
"boxcnQyuuLppyzEjL5T4NF2rLy6	贴膜v3-转曲.pdf"
"boxcn7kUrFm3NTVPMCAiraXsnCe	渲染图带logo.png"
"boxcnc2iCQtix6oXMUn1KTjKilf	2-2.png"
"boxcnEkkR27uCcIZA3H3jEuGKid	贴膜v5-转曲.ai"
"boxcn8UPXBq3ofM8sFEJRhsoKWc	渲染图带logo的副本.png"
"boxcnt43k1K6joiQsZOCod1cDXd	模型~.skp"
"boxcniEKQ0fXT960SnlSH1J9oke	贴膜v5-转曲_画板 1.png"
"boxcnxOTpTeHilwWucORKnDneM4	贴膜v6-按钮无边框_画板 1.png"
"boxcngxiI4QMQuz2DrDFYVtsaSd	贴膜2.dxf"
"boxcnPh0kRXeoUdxFpuSO8YN0Db	asm0004.stl"
"boxcncNmYFQdSBgSp33WZpnosPd	贴膜上-基础.ai"
"boxcnYvirh7LXQOr6IaNKAlxXQb	下载.png"
"boxcngrPUCoeaf7pAwDi6i1GxNc	贴膜-cmyk.ai"
"boxcn9MxO1qwYrMlGDIbpFhJ9Wc	贴膜2.eps"
"boxcnYT3gAhHOvODcaemdABoNEg	核电图片.ai"
"boxcnPo2xxHaLF3SVKWBZvy030U	贴膜v6-按钮带边框.ai"
"boxcnWReHtYGnuY0z3h5veLYoYe	WechatIMG3514 1.jpeg"
"boxcnsuHvaYqKGIBnVq2upH3Vcb	贴膜-转曲v2.pdf"
"boxcn8Dy1VQrkPQXhFyU135baOc	上盖贴膜修改.eps"
"boxcnm2jrO3lvOPEZ6cWrzGqYHc	上盖贴膜1031.dxf"
"boxcncSbxB4XU9AuiMmztWuvECe	贴膜v6-按钮无边框.ai"
"boxcnGoISyhGXB9pFCMmUgdsppe	spic2021_Screen.png"
"boxcnI5DmG1Z7viebe1imf5rRlb	贴膜v3.ai"
"boxcnB1RCw7qTcQZo1zQHy6spjd	上盖贴膜1031.eps"
"boxcnp3ByLFth5aCGWMyeobi6Wf	36021666942396_.pic_hd_副本.png"
"boxcnPK8p7M4Sgbix60KFWTLZ3e	贴膜上.ai"
"boxcni5i4ULQtpct4bf4eTKRcYm	贴膜-转曲v2.ai"
)

# 记录已完成的第一个文件
echo -e "boxcniIloR4LNtC8K1T5Kp1uQIb\t模型.skp\tEqFLbreBrolbLExJbedczv08nQg\tHaDHwzKtNioZ74kr94lceFpFnxb\t成功" >> "$RESULT_FILE"

TOTAL=${#FILES[@]}
SUCCESS=1  # 已有1个成功
FAIL=0

for i in "${!FILES[@]}"; do
  IFS=$'\t' read -r TOKEN FILENAME <<< "${FILES[$i]}"
  NUM=$((i+2))  # 从2开始（第1个已完成）
  echo ""
  echo "[$NUM/42] 处理: $FILENAME (token: $TOKEN)"
  echo "[$NUM/42] $FILENAME" >> "$LOG_FILE"

  # 步骤1: drive copy 到临时文件夹
  echo "  步骤1: drive copy..."
  COPY_RESULT=$(lark-cli drive files copy \
    --params "{\"file_token\":\"$TOKEN\"}" \
    --data "{\"name\":\"$FILENAME\",\"type\":\"file\",\"folder_token\":\"$TEMP_FOLDER\"}" \
    --as user 2>&1)
  echo "  copy结果: $COPY_RESULT" >> "$LOG_FILE"

  # 提取副本 token
  COPY_TOKEN=$(echo "$COPY_RESULT" | grep -o '"token":"[^"]*"' | head -1 | sed 's/"token":"//;s/"//')
  COPY_CODE=$(echo "$COPY_RESULT" | grep -o '"code":[0-9]*' | head -1 | sed 's/"code"://')

  if [ "$COPY_CODE" != "0" ] || [ -z "$COPY_TOKEN" ]; then
    echo "  ❌ copy 失败: $COPY_RESULT"
    echo -e "$TOKEN\t$FILENAME\t-\t-\tcopy失败" >> "$RESULT_FILE"
    echo "  ❌ copy 失败" >> "$LOG_FILE"
    FAIL=$((FAIL+1))
    sleep 2
    continue
  fi

  echo "  ✅ copy 成功, 副本token: $COPY_TOKEN"
  sleep 2

  # 步骤2: move_docs_to_wiki
  echo "  步骤2: move_docs_to_wiki..."
  MOVE_RESULT=$(lark-cli api POST "/open-apis/wiki/v2/spaces/$SPACE_ID/nodes/move_docs_to_wiki" \
    --data "{\"parent_wiki_token\":\"$PARENT_NODE\",\"obj_type\":\"file\",\"obj_token\":\"$COPY_TOKEN\"}" \
    --as user 2>&1)
  echo "  move结果: $MOVE_RESULT" >> "$LOG_FILE"

  # 提取 task_id
  TASK_ID=$(echo "$MOVE_RESULT" | grep -o '"task_id":"[^"]*"' | head -1 | sed 's/"task_id":"//;s/"//')
  MOVE_CODE=$(echo "$MOVE_RESULT" | grep -o '"code":[0-9]*' | head -1 | sed 's/"code"://')

  if [ "$MOVE_CODE" != "0" ] || [ -z "$TASK_ID" ]; then
    echo "  ❌ move 失败: $MOVE_RESULT"
    echo -e "$TOKEN\t$FILENAME\t$COPY_TOKEN\t-\tmove失败" >> "$RESULT_FILE"
    echo "  ❌ move 失败" >> "$LOG_FILE"
    FAIL=$((FAIL+1))
    sleep 2
    continue
  fi

  echo "  ✅ move 提交成功, task_id: $TASK_ID"
  sleep 3

  # 步骤3: 查询 task 状态获取 wiki_token
  echo "  步骤3: 查询任务状态..."
  TASK_RESULT=$(lark-cli api GET "/open-apis/wiki/v2/tasks/$TASK_ID" \
    --params '{"task_type":"move"}' --as user 2>&1)
  echo "  task结果: $TASK_RESULT" >> "$LOG_FILE"

  WIKI_TOKEN=$(echo "$TASK_RESULT" | grep -o '"node_token":"[^"]*"' | head -1 | sed 's/"node_token":"//;s/"//')

  if [ -z "$WIKI_TOKEN" ]; then
    echo "  ⚠️ 获取 wiki_token 失败，但 move 已提交"
    echo -e "$TOKEN\t$FILENAME\t$COPY_TOKEN\t未知(task:$TASK_ID)\t部分成功" >> "$RESULT_FILE"
  else
    echo "  ✅ 完成: $FILENAME → wiki_token: $WIKI_TOKEN"
    echo -e "$TOKEN\t$FILENAME\t$COPY_TOKEN\t$WIKI_TOKEN\t成功" >> "$RESULT_FILE"
  fi

  echo "  ✅ 完成" >> "$LOG_FILE"
  SUCCESS=$((SUCCESS+1))
  sleep 2
done

echo ""
echo "=== 同步完成 ==="
echo "总计: 42, 成功: $SUCCESS, 失败: $FAIL"
echo "=== 同步完成 $(date) 总计:42 成功:$SUCCESS 失败:$FAIL ===" >> "$LOG_FILE"
echo "结果文件: $RESULT_FILE"
