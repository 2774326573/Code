# nvim快捷键

## nvim模式

<table>
<tr>
<th rowspan="6">nvim模式</th>
<th>normal_mode = "n"</th>
<th>命令模式</th>
</tr>
<tr>
<td>insert_mode = "i"</td>
<td>插入模式</td>
<tr>
<td>visual_mode = "v"</td>
<td>可视模式</td>
</tr>
</tr>
<tr>
<td>term_mode = "t"</td>
<td></td>
</tr>
<tr>
<td>command_mode = "c"</td>
<td></td>
</tr>
</table>

> 命令行下上一个下一个

|  模式          | 命令           | 快捷键      |
| -------------  | -------------  | -------        |
|    c           | <\C-n>          | <\C-j>          |
|    c           | <\C-p>          | <\C-k>          |

> $跳到行尾不带空格(交换$和g_)

|  模式          | 命令           | 快捷键      |
| -------------  | -------------  | -------        |
|    v           | g_             | \$             |
|    v           | \$             | g_             |
|    n           | g_             | \$             |
|    n           | \$             | g_             |

> 上下滚动游览 <br/> ctrl+u /ctrl+d 移动半屏

|  模式          | 命令           | 快捷键      |
|    n           | 5j             | <\C-j>             |
|    n           | 5k             | <\C-k>             |
| -------------  | -------------  | -------        |
|    v           | 5j             | <\C-j>             |
|    v           | 5k             | <\C-k>             |

>Visual模式下缩进代码

|  模式          | 命令           | 快捷键      |
| -------------  | -------------  | -------        |
|    v           | \<\gv             | \<             |
|    v           | \>gv             | >             |

>Visual模式下上下移动选中文本

|  模式          | 命令                  | 快捷键       |
| -------------  | -------------         | -------        |
|    v           | :move '>+1<\CR>gv-gv'  | J              |
|    v           | :move '<\-2<\CR>gv-gv'  | K              |

>在Visual mode里粘贴不要复制

|  模式        | 命令           | 快捷键    |
| -------------  | -------------  | -------        |
|    v           | \_dP           | p              |

## 退出控制
>保存退出快捷键

|  模式        | 命令           | 快捷键    |
| -------------  | -------------  | -------        |
|    n           | \<\cmd>w<\CR> | w              |
|    n           | \:wq<\CR> | wq              |
|    n           | \:q<\CR> | <\leader>q              |
|    n           | \:qa!<\CR> | <\leader>qq              |

## 插入模式控制
>在Visual mode里粘贴不要复制

|  模式          | 命令           | 快捷键      |
| -------------  | -------------  | -------        |
|    i           | <\ESC>I         | <\C-h>          |
|    i           | <\ESC>A         | <\C-l>          |
|    i           | <\ESC>ja        | <\C-j>          |
|    i           | <\ESC>ka        | <\C-k>          |

## 窗口控制
>取消s默认功能,开启分配快捷键

| 模式          | 命令          | 快捷键  |
| ------------- | ------------- | ------- |
| n             | :vsp<\CR>      | sv      |
| n             | :sp<\CR>       | sb      |

>关闭当前窗口

| 模式          | 命令          | 快捷键  |
| ------------- | ------------- | ------- |
| n             | <\C-w>c        | sc      |

>关闭当前窗口

| 模式          | 命令          | 快捷键  |
| ------------- | ------------- | ------- |
| n             | <\C-w>o        | so      |

>窗口之间跳转

| 模式          | 命令          | 快捷键    |
| ------------- | ------------- | -------   |
| n             | <\C-w>h        | <\leader>h |
| n             | <\C-w>j        | <\leader>j |
| n             | <\C-w>k        | <\leader>k |
| n             | <\C-w>l        | <\leader>l |

>左右比例控制

| 模式          | 命令                    | 快捷键    |
| ------------- | -------------           | -------   |
| n             | :vertical resize -1<\CR> | <\C-Right> |
| n             | :vertical resize +1<\CR> | <\C-Left>  |
| n             | :vertical resize +5<\CR> | s,        |
| n             | :vertical resize -5<\CR> | s.        |

>上下比例控制

| 模式          | 命令           | 快捷键  |
| ------------- | -------------  | ------- |
| n             | :resize -1<\CR> | sj      |
| n             | :resize +1<\CR> | sk      |

>相等比例

| 模式          | 命令          | 快捷键  |
| ------------- | ------------- | ------- |
| n             | <\C-w>=        | s=      |

>相等比例

| 模式          | 命令          | 快捷键                    |
| ------------- | ------------- | -------                   |
| n             | :sp \| terminal pwsh -nologo<\CR> | stb |
| n             | :vsp \| terminal pwsh -nologo<\CR> | stv |
| n             | \| terminal pwsh -nologo<\CR> | ss  |

>相等比例

| 模式          | 命令          | 快捷键                    |
| ------------- | ------------- | -------                   |
| n             | :sp \| terminal pwsh -nologo<\CR> | stb |
| t | <\C-\\>\<\C-n> | jk |
| t | [[ \<\C-\>\<\C-N>\<\C-w>h ]] | \<\C-h> |
| t | [[ \<\C-\>\<\C-N>\<\C-w>l ]] | \<\C-l> |
| t | [[ \<\C-\>\<\C-N>\<\C-w>k ]] | \<\C-k> |
| t | [[ \<\C-\>\<\C-N>\<\C-w>j ]] | \<\C-j> |
| t | [[ \<\C-\>\<\C-N>\<\C-w>h ]] | \<\leader>h |
| t | [[ \<\C-\>\<\C-N>\<\C-w>l ]] | \<\leader>l |
| t | [[ \<\C-\>\<\C-N>\<\C-w>k ]] | \<\leader>k |
| t | [[ \<\C-\>\<\C-N>\<\C-w>j ]] | \<\leader>j |

## 插件快捷键

<table>
<tr>
<th rowspan="145">nvim快捷键</th>
<th>插件 </th>
<th>命令 </th>
<th>快捷键 </th>
</tr>
<tr>
<th rowspan="2">treesitter折叠</th>
<th>:foldclose\<\CR> </th>
<th>zz </th>
</tr>
<tr>
<td>:foldclose\<\CR> </td>
<td>Z </td>
</tr>
<tr>
<th rowspan="2">markdown</th>
<th>:MarkdownPreview\<\CR> </th>
<th><\leader>mb </th>
</tr>
<tr>
<td>:MarkdownPreviewStop\<\CR> </td>
<td><\leader>me </td>
</tr>
<tr>
<th rowspan="1">跳转</th>
<th>:HopWord\<\CR> </th>
<th><\leader>w </th>
</tr>
<tr>
<th rowspan="1">nvim-tree</th>
<th>:NvimTreeToggle\<\CR> </th>
<th><\A-m> </th>
</tr>
<tr>
<th rowspan="2">左右Tab切换</th>
<th>:BufferLineCyclePrev\<\CR> </th>
<th><\A-h> </th>
</tr>
<tr>
<td>:BufferLineCycleNext\<\CR> </td>
<td><\A-l> </td>
</tr>
<tr>
<th rowspan="2">vim-bbye 关闭当前buffer</th>
<th>:Bdelete!\<\CR> </th>
<th>xx</th>
</tr>
<tr>
<td>:<\cmd>Bdelete!<\CR><\cmd>close<\CR> </td>
<td>xc</td>
</tr>
<tr>
<th rowspan="2">关闭左/右标签页</th>
<th>:BufferLineCloseLeft!\<\CR> </th>
<th><\leader>xh</th>
</tr>
<tr>
<td>:BufferLineCloseRight<\CR> </td>
<td><\leader>xl</td>
</tr>
<tr>
<th rowspan="1">关闭其他标签页</th>
<th>:BufferLineCloseRight<\CR>:BufferLineCloseLeft<\CR> </th>
<th><\leader>xo</th>
</tr>
<tr>
<th rowspan="1">关闭选中标签页</th>
<th>:BufferLinePickClose<\CR></th>
<th><\leader>xp</th>
</tr>
<tr>
<th rowspan="1">翻译</th>
<th>:TranslateW<\CR></th>
<th>fy</th>
</tr>
<tr>
<th rowspan="3">Telescope</th>
<th>:Telescope find_files\<\CR> </th>
<th><\C-f></th>
</tr>
<tr>
<td>:Telescope live_grep<\CR> </td>
<td><\C-p></td>
</tr>
<tr>
<td>:Telescope buffers<\CR> </td>
<td><\C-b></td>
</tr>
<tr>
<th rowspan="4">Telescope 插入模式移动</th>
<th>:move_selection_next\<\CR> </th>
<th><\C-j></th>
</tr>
<tr>
<td>:move_selection_previous<\CR> </td>
<td><\C-k></td>
</tr>
<tr>
<td>:move_selection_next<\CR> </td>
<td><\C-n></td>
</tr>
<tr>
<td>:move_selection_previous<\CR> </td>
<td><\C-p></td>
</tr>
<tr>
<th rowspan="2">Telescope 历史记录</th>
<th>:cycle_history_next<\CR> </th>
<th><\Down></th>
</tr>
<tr>
<td>:cycle_history_prev<\CR> </td>
<td><\up></td>
</tr>
<tr>
<th rowspan="1">Telescope 关闭窗口</th>
<th>:close<\CR> </th>
<th><\C-c></th>
</tr>
<tr>
<th rowspan="2">Telescope 预览窗口上下移动</th>
<th>:preview_scrolling_up<\CR> </th>
<th><\C-u></th>
</tr>
<tr>
<td>:preview_scrolling_down<\CR> </td>
<td><\C-d></td>
</tr>
<tr>
<th rowspan="2">代码注释命令模式</th>
<th>行注释 </th>
<th>gcc</th>
</tr>
<tr>
<td>块注释 </td>
<td>gbc</td>
</tr>
<tr>
<th rowspan="1">代码注释可视模式</th>
<th>gc </th>
<th>gb</th>
</tr>
<tr>
<th rowspan="2">代码注释</th>
<th>gcc</th>
<th>"n" <\C-_></th>
</tr>
<tr>
<td>gcc</td>
<td>"v" <\C-_></td>
</tr>
<tr>
<th rowspan="1">格式化</th>
<th>:Format<\CR></th>
<th>"n" <\C-s></th>
</tr>
<tr>
<th rowspan="2">neoai.nvim</th>
<th>:NeoAI<\CR></th>
<th>"n" <\leader>a</th>
</tr>
<tr>
<td>:NeoAIInject</td>
<td>"n" <\leader>i</td>
</tr>
<tr>
<th rowspan="2">纯净模式</th>
<th>:TZMinimalist<\CR></th>
<th>"n" <\leader>g</th>
</tr>
<tr>
<td>:TZNarrow<\CR></td>
<td>"v" <\leader>h</td>
</tr>
<tr>
<th rowspan="1">Ctrl+g 纯净模式</th>
<th>leader+gg 选中纯净模式</th>
<th></th>
</tr>
<tr>
<th rowspan="2">纯净模式</th>
<th>:TZMinimalist<\CR></th>
<th>"n" <\leader>g</th>
</tr>
<tr>
<td>:TZNarrow<\CR></td>
<td>"v" <\leader>h</td>
</tr>
<tr>
<th rowspan="2">细胞cam 游戏cha</th>
<th>:CellularAutomaton make_it_rain<\CR></th>
<th>"n" cam</th>
</tr>
<tr>
<td>:CellularAutomaton game_of_life<\CR></td>
<td>"n" cag</td>
</tr>
<tr>
<th rowspan="13">lsp 回调函数快捷键设置</th>
<th><\cmd>lua vim.lsp.buf.format{async=ture}<\CR></th>
<th>"n" <\leader>s</th>
</tr>
<tr>
<td><\cmd>Lspsaga rename<\CR></td>
<td>"n" cm</td>
</tr>
<tr>
<td><\cmd>Lspsaga code_action<\CR></td>
<td>"n" <\leader>ca</td>
</tr>
<tr>
<td><\cmd>Lspsaga goto_definition<\CR></td>
<td>"n" gd</td>
</tr>
<tr>
<td><\cmd>Lspsaga peek_definition<\CR></td>
<td>"n" gD</td>
</tr>
<td><\cmd>Lspsaga peek_definition<\CR></td>
<td>"n" gt</td>
<tr>
</tr>
<tr>
<td><\cmd>Lspsaga hover_doc<\CR></td>
<td>"n" gh</td>
</tr>
<tr>
<td><\cmd>Lspsaga lsp_finder<\CR></td>
<td>"n" gr</td>
</tr>
<tr>
<td><\cmd>Lspsaga show_line_diagnostics<\CR></td>
<td>"n" gp</td>
</tr>
<tr>
<td><\cmd>Lspsaga diagnostic_jump_next<\CR></td>
<td>"n" gj</td>
</tr>
<tr>
<td><\cmd>Lspsaga diagnostic_jump_prev<\CR></td>
<td>"n" gk</td>
</tr>
<tr>
<td><\cmd>Lspsaga outline<\CR></td>
<td>"n" <\F8></td>
</tr>
<tr>
<th rowspan="14">nvim-dap</th>
<th>结束</th>
<th></th>
</tr>
<tr>
<td>:lua require'dap'.terminate<\CR><br/>:lua require'dap'.close<\CR><br/>:lua require'dap.repl'.close<\CR><br/>:lua require'dapui'.close<\CR><br/>:lua require('dap').clear_breakpoints()<\CR><br/><\C-w>0<\CR></td>
<td>"n" <\S-F5></td>
</tr>
<tr>
<td>开始/继续</td>
<td></td>
</tr>
<tr>
<td>:lua require'dap'.continue()<\CR></td>
<td>"n" <\C-F5></td>
</tr>
<tr>
<td>设置断点</td>
<td></td>
</tr>
<tr>
<td>:lua require'dap'.toggle_breakpoint()<\CR></td>
<td>"n" <\F6></td>
</tr>
<tr>
<td>:lua require'dap'.clear_breakpoints()<\CR></td>
<td>"n" <\S-F6></td>
</tr>
<tr>
<td>stepOver,stepOut,stepInto</td>
<td></td>
</tr>
<tr>
<td>:lua require'dap'.step_over()<\CR></td>
<td>"n" <\F12></td>
</tr>
<tr>
<td>:lua require'dap'.step_out()<\CR></td>
<td>"n" <\S-F7></td>
</tr>
<tr>
<td>:lua require'dap'.step_into()<\CR></td>
<td>"n" <\S-F12></td>
</tr>
<tr>
<td>弹窗</td>
<td></td>
</tr>
<tr>
<td>:lua require'dap'.restart()<\CR></td>
<td>"n" <\F10></td>
</tr>
<tr>
<td>:lua require'dap'.terminate()<\CR></td>
<td>"n" <\S-F10></td>
</tr>
<tr>
<th rowspan="14">nvim-cmp自动补全</th>
<th>上一个</th>
<th></th>
</tr>
<tr>
<td>=cmp.mapping.select_prev_item()</td>
<td><\C-k></td>
</tr>
<tr>
<td>下一个</td>
<td></td>
</tr>
<tr>
<td>=cmp.mapping.select_next_item()</td>
<td><\C-j></td>
</tr>
<td>出现补全</td>
<td></td>
<tr>
</tr>
<tr>
<td>=cmp.mapping(cmp.mapping.complete(),{"i","c"})</td>
<td><\A-.></td>
</tr>
<tr>
<td>确认</td>
<td></td>
</tr>
<tr>
<td>=cmp.mapping.confirm({<br/>select=true,<br/>behavior=cmp.ConfirmBehavior.Replace})</td>
<td><\CR></td>
</tr>
<tr>
<td>如果窗口内容太多，可以滚动</td>
<td></td>
</tr>
<tr>
<td>=cmp.mapping(cmp.mapping.scroll_docs(-4),{"i","c"})</td>
<td><\C-u></td>
</tr>
<tr>
<td>=cmp.mapping(cmp.mapping.scroll_docs(4),{"i","c"})</td>
<td><\C-d></td>
</tr>
<tr>
<td>=cmp.mapping(function(fallback))<br/>判断Tab是否是snippets代码片段</td>
<td><\Tab></td>
</tr>
<tr>
<td>=cmp.mapping(function())<br/>判断Tab是否是snippets代码片段</td>
<td><\S-Tab></td>
</tr>
<tr>
<th rowspan="4">toggler</th>
<th>toggleA</th>
<th>"n"/"t" tt</th>
</tr>
<tr>
<td>toggleB</td>
<td>"n"/"t" tb</td>
</tr>
<tr>
<td>toggleC</td>
<td>"n"/"t" tc</td>
</tr>
<tr>
<td>toggleG</td>
<td>"n"/"t" tg</td>
</tr>
<tr>
<th rowspan="15">gitsigns查看更改记录</th>
<th>gs.next_hunk()</th>
<th>"n" <\leader>gj</th>
</tr>
<tr>
<td>gs.prev_hunk</td>
<td>"n" <\leader>gk</td>
</tr>
<tr>
<td>:Gitsigns stage_hunk<\CR></td>
<td>"n"/"v" <\leader>gs</td>
</tr>
<tr>
<td>gs.stage_buffer</td>
<td>"n" <leader>gS</td>
</tr>
<tr>
<td>gs.undo_stage_hunk</td>
<td>"n" <leader>gu</td>
</tr>
<tr>
<td>:Gitsigns reset_hunk<\CR></td>
<td>"n"/"v" <\leader>gr</td>
</tr>
<tr>
<td>gs.stage_buffer</td>
<td>"n" <leader>gR</td>
</tr>
<tr>
<td>gs.undo_stage_hunk</td>
<td>"n" <leader>gp</td>
</tr>
<td>gs.blame_line({full=true})</td>
<tr>
<td>"n" <leader>gb</td>
</tr>
<tr>
<td>gs.diffthis</td>
<td>"n" <leader>gd</td>
</tr>
<tr>
<td>gs.diffthis(~)</td>
<td>"n" <leader>gD</td>
</tr>
<tr>
<td>gs.toggle_deleted</td>
<td>"n" <leader>gtd</td>
</tr>
<tr>
<td>gs.toggle_current_line_blame</td>
<td>"n" <leader>gtb</td>
</tr>
<tr>
<td>:<\C-U>Gitsigns_on_attach<\CR></td>
<td>"o"/"x" ig</td>
</tr>
</table>
