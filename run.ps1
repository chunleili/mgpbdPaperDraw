# 确保所有必要目录存在
$dirs = @(
    "figures",
    "figures/draw-figure0",
    "figures/draw-figure1"
)

foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force
    }
}

# 清理之前的临时文件
Remove-Item -Path "figures\*" -Force -Recurse -ErrorAction SilentlyContinue

# 运行pdflatex两次
pdflatex -shell-escape -interaction=nonstopmode -pool-size=1000000000 -extra-mem-top=1000000000 "draw.tex"
pdflatex -shell-escape -interaction=nonstopmode -pool-size=1000000000 -extra-mem-top=1000000000 "draw.tex"

# 运行clean.ps1 删除临时文件
.\clean.ps1