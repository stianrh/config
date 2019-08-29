set exrc
set secure
"let g:ycm_key_list_select_completion=[]
"let g:ycm_key_list_previous_completion=[]
filetype off
call pathogen#infect()
call pathogen#helptags()
"nnoremap <leader>v <Plug>TaskList
let g:CommandTAcceptSelectionMap = '<CR>'
let g:CommandTAcceptSelectionTabMap = '<C-t>'
let g:CommandTMaxFiles=200000 
nnoremap <C-n> :tabn<CR>
nnoremap <C-p> :tabp<CR>
nnoremap <C-w>t :tabedit<CR>
map <Leader>n <plug>NERDTreeTabsToggle<CR>
syntax on 
filetype on 
filetype plugin indent on 
set pastetoggle=<F2> 
nnoremap <F2> :set invpaste paste?<CR> 
set pastetoggle=<F2> 
set showmode 
set number 
set wildignore=*.pyc 
set tabstop=4 
set shiftwidth=4 
set expandtab 
set foldlevel=99 
map <c-j> <c-w>j 
map <c-k> <c-w>k 
map <c-l> <c-w>l 
map <c-h> <c-w>h 
nmap <S-Enter> O<Esc> 
nmap <CR> o<Esc> 
nmap <C-Down> <C-e> 
nmap <C-Up> <C-y> 
imap jk <Esc>
"map <leader>g :GundoToggle<CR> 
"let g:pyflakes_use_quickfix = 0 
au FileType python set omnifunc=pythoncomplete#Complete 
let g:SuperTabDefaultCompletionType = "context" 
set completeopt=menuone,longest,preview 
"map <leader>j :RopeGotoDefinition<CR> 
"map <leader>r :RopeRename<CR> 
"nmap <leader>a <Esc>:Ack! 
nnoremap <leader>j :YcmCompleter GoTo<CR> 
"let g:ycm_collect_identifiers_from_tags_files = 1
" Add the virtualenv's site-packages to vim path 

let $NVIM_TUI_ENABLE_TRUE_COLOR=1
set termguicolors
colorscheme molokai
set background=dark
"hi CursorLine   cterm=NONE ctermbg=darkgray ctermfg=white guibg=darkred guifg=white
"hi CursorColumn cterm=NONE ctermbg=darkgray ctermfg=white guibg=darkred guifg=white
augroup CursorLine
  au!
  au VimEnter,WinEnter,BufWinEnter * setlocal cursorline
  au WinLeave * setlocal nocursorline
augroup END
nnoremap <Leader>c :set cursorline!<CR>
"set t_Co=256
map <Leader>o0 :! DISPLAY=:0 notepad %<CR>
map <Leader>o10 :! DISPLAY=localhost:10 notepad %<CR>
map <Leader>o11 :! DISPLAY=localhost:11 notepad %<CR>
map <Leader>o12 :! DISPLAY=localhost:12 notepad %<CR>
