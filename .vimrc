set ruler
set nu
set cursorline
"set number
call pathogen#infect()
syntax on

filetype plugin indent on
let g:pydiction_location = '~/.vim/vimfiles/ftplugin/pydiction/complete-dict'
syntax enable

filetype plugin indent on

" Solarized stuff
let g:solarized_termtrans = 1
set background=dark
colorscheme solarized

"mapping
"Maps autocomplete to tab
imap <Tab> <C-N>
map <F2> <Esc>:w<CR>:!%:p<CR>
