set ruler
set nu
set cursorline
"set number
call pathogen#infect()
syntax on

filetype plugin indent on
let g:pydiction_location = '~/.vim/vimfiles/ftplugin/pydiction/complete-dict'

"General config
syntax enable	"Show syntax highlighting
set title	"Show the name of the file
set showmode 	"show current mode on bottom

"Search
set hlsearch	"highlight searches
set ignorecase	"ignore search case
set incsearch	"dynamic highlight with search pattern

"Indentation
set autoindent
set smartindent

filetype plugin indent on

" Solarized stuff
let g:solarized_termtrans = 1
set background=dark
colorscheme solarized

"mapping
"Maps autocomplete to tab
map <F2> <Esc>:w<CR>:!%:p<CR>
