$word = New-Object -ComObject Word.Application
$word.Visible = $false
$docPath = "C:\Users\Godwyn\Downloads\03_Laboratory_Exercise_1_Godwyn_Neri_BSIT711.docx"
$pdfPath = "C:\Users\Godwyn\Downloads\03_Laboratory_Exercise_1_Godwyn_Neri_BSIT711.pdf"
$coursePdf = "C:\Users\Godwyn\Documents\Projects\Browser activity\courses\Computer_Graphics_Programming\assignments\midterm\03_Laboratory_Exercise_1\03_Laboratory_Exercise_1_Godwyn_Neri_BSIT711.pdf"

try {
    $doc = $word.Documents.Open($docPath)
    $doc.SaveAs([ref]$pdfPath, [ref]17)
    $doc.Close()
    Copy-Item $pdfPath $coursePdf -Force
    Write-Output "PDF successfully generated: $pdfPath and $coursePdf"
} finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
}
