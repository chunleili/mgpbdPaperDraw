# 删除临时文件
Remove-Item -Path "*.aux", "*.auxlock", "*.figlist", "*.log", "*.makefile", "*.out", "*.xcp",
    "*.dvi", "*.ps", "*.synctex.gz", 
    "draw-figure*.log", "draw-figure*.dpth", "draw-figure*.md5", "*.fls",  "draw.fdb_latexmk" -Force  -ErrorAction SilentlyContinue

# 清理figures目录中的临时文件
if (Test-Path ".\figures") {
    Remove-Item -Path ".\figures\*.aux", ".\figures\*.log", ".\figures\*.dpth", 
        ".\figures\*.md5",".\figures\*.dep"  -Force -ErrorAction SilentlyContinue
}

# 保留最终的PDF文件和figures目录中的文件