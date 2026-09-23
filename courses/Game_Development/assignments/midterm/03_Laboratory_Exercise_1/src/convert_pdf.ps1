$word = New-Object -ComObject Word.Application
$word.Visible = $false
$docPath = "C:\Users\Godwyn\Downloads\03_Laboratory_Exercise_1_Godwyn_Neri_BSIT711.docx"
$pdfDlPath = "C:\Users\Godwyn\Downloads\03_Laboratory_Exercise_1_Godwyn_Neri_BSIT711.pdf"
$gamedevPdf = "c:\Users\Godwyn\Documents\Projects\Browser activity\courses\Game_Development\assignments\midterm\03_Laboratory_Exercise_1\03_Laboratory_Exercise_1_Godwyn_Neri_BSIT711.pdf"
$cgpPdf = "c:\Users\Godwyn\Documents\Projects\Browser activity\courses\Computer_Graphics_Programming\assignments\midterm\03_Laboratory_Exercise_1\03_Laboratory_Exercise_1_Godwyn_Neri_BSIT711.pdf"

try {
    $doc = $word.Documents.Open($docPath)
    $doc.SaveAs([ref]$pdfDlPath, [ref]17)
    $doc.Close()
    Copy-Item $pdfDlPath $gamedevPdf -Force
    if (Test-Path "c:\Users\Godwyn\Documents\Projects\Browser activity\courses\Computer_Graphics_Programming\assignments\midterm\03_Laboratory_Exercise_1") {
        Copy-Item $pdfDlPath $cgpPdf -Force
    }
    Write-Output "PDF successfully generated and mirrored: $pdfDlPath and $gamedevPdf"
} finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
}
