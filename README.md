# Lietojumprogrammaturas-automatizanas-riki-projekts
### Apraksts
Šajā projektā es apstrādāju 3 PDF failus (dažādi maksājumi par dzīvokli), lai no katra izvilktu summu un beigās to saskaitītu. Šim nolūkam es izmantoju divas bibliotēkas. Es apstrādāju pirmos divus PDF failus, izmantojot PyPDF2, bet trešo, izmantojot fitz, jo 3. PDF failā tiek izmantotas rakstzīmes, kuras PyPDF2 nevar apstrādāt.
### Darbības princips
Programmas darbības princips ir PDF failu atvēršana, ierakstot tos kā teksta failus, pēc tam tekstā atslēgvārdu atrašana, lai noteiktu nepieciešamās informācijas atrašanās vietu par nepieciešamo summu, un beigās visu summu aprēķināšana
### lejupielādējot bibliotēku
pip install PyPDF2
pip install fitz
