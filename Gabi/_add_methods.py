import re

path = "index.html"
content = open(path, encoding="utf-8").read()
orig_len = len(content)

# ---------- 1) Two new tab buttons ----------
TAB_BUTEYKO = '<button class="lc-tab cursor-interaction" type="button" role="tab" id="lc-tab-buteyko" aria-controls="lc-panel-buteyko" aria-selected="false"><svg data-lucide="activity" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2" /></svg><span>Respirația Buteyko<small>RESPIRAȚIE &amp; ECHILIBRU</small></span><svg class="lc-chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></button>\n'
TAB_RESUMI = '<button class="lc-tab cursor-interaction" type="button" role="tab" id="lc-tab-resumi" aria-controls="lc-panel-resumi" aria-selected="false"><svg data-lucide="waves" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1" /><path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1" /><path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1" /></svg><span>ReSuMi<small>RESPIRAȚIE &middot; SUNET &middot; MIȘCARE</small></span><svg class="lc-chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></button>\n'

marker_aside = '</div></aside>'
occ = content.count(marker_aside)
assert occ == 1, f"marker_aside occ={occ}"
content = content.replace(marker_aside, TAB_BUTEYKO + TAB_RESUMI + marker_aside)

# ---------- 2) Two new panels ----------
PANEL_BUTEYKO = '''<article class="lc-panel" role="tabpanel" id="lc-panel-buteyko" aria-labelledby="lc-tab-buteyko" hidden>
<div class="lc-kicker">Respirație &amp; echilibru</div><h3>Respirația Buteyko</h3><p class="lc-tagline">Respiră conștient. Descoperă-ți ritmul.</p>
<div class="lc-description"><p>Metoda Buteyko este o practică de reeducare respiratorie dezvoltată de medicul Konstantin Buteyko. Ea urmărește observarea și reducerea tendinței de a respira excesiv, pentru a susține un tipar respirator mai confortabil și adaptat nevoilor corpului.</p><p>Prin exerciții ghidate, îți aduci atenția asupra felului în care respiri și explorezi o respirație nazală, liniștită și silențioasă. Practica poate include pauze respiratorii scurte și explorarea treptată a senzației de nevoie de aer, fără forțare.</p><p>Exercițiile sunt adaptate fiecărei persoane și se practică progresiv. Înveți să recunoști schimbările respirației în diferite contexte și să îți dezvolți o relație mai conștientă cu propriul ritm respirator.</p></div>
<div class="lc-preparation"><svg data-lucide="info" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10" /><path d="M12 16v-4" /><path d="M12 8h.01" /></svg><div><h4>Precizare importantă</h4><p>Dacă ai astm sau alte afecțiuni respiratorii, discută cu medicul înainte de practică. Metoda poate fi folosită complementar îngrijirii medicale și nu înlocuiește medicația, investigațiile sau recomandările medicului.</p></div></div>
</article>
'''

PANEL_RESUMI = '''<article class="lc-panel" role="tabpanel" id="lc-panel-resumi" aria-labelledby="lc-tab-resumi" hidden>
<div class="lc-kicker">Respirație &middot; sunet &middot; mișcare</div><h3>ReSuMi &ndash; Respirație, Sunet și Mișcare</h3><p class="lc-tagline">Mișcă-te. Respiră. Ascultă.</p>
<div class="lc-description"><p>ReSuMi este o practică integrativă pe care am creat-o prin îmbinarea a trei elemente: respirația, sunetul și mișcarea. Împreună, ele creează o experiență care te invită să te reconectezi cu propriul corp, să observi tensiunile acumulate și să faci loc echilibrului interior.</p><p>Practica începe prin mișcare conștientă, care îți aduce atenția în corp și te invită să observi senzațiile și zonele în care simți tensiune. Treptat, mișcarea deschide calea către respirația conștientă, prin care explorezi legătura dintre corp, gânduri și emoții.</p><p>Experiența este completată de sunetele și vibrațiile bolurilor tibetane, care creează un cadru pentru relaxare, prezență și introspecție. La final, îți oferi timp să observi și să integrezi ceea ce ai trăit.</p><p>ReSuMi este o invitație de a te întoarce la tine prin trei căi care se întâlnesc într-o singură experiență: mișcarea te aduce în corp, respirația te conectează cu interiorul tău, iar sunetul te invită să îți dai voie.</p></div>
</article>
'''

marker_panels_end = '</div></div>\n<h3 class="lc-footer-title">'
occ2 = content.count(marker_panels_end)
assert occ2 == 1, f"marker_panels_end occ={occ2}"
content = content.replace(marker_panels_end, PANEL_BUTEYKO + PANEL_RESUMI + marker_panels_end)

# ---------- 3) benefits JS object ----------
OLD_BENEFITS_TAIL = """'lc-tab-prana':[
['Observarea mecanicii și amplitudinii respirației','Recunoașterea respirației superficiale și a pauzelor involuntare','Învățarea unui ritm respirator confortabil'],
['Recunoașterea schimbărilor de stare prin respirație','Relaxare și reducerea stresului prin tehnici blânde, adaptate persoanei','Crearea unui răgaz înainte de reacțiile automate'],
['Antrenarea concentrării pe ritm și respirație','Pregătirea atenției pentru meditație','Un reper simplu pentru revenirea în prezent']]
};"""

NEW_BENEFITS_TAIL = """'lc-tab-prana':[
['Observarea mecanicii și amplitudinii respirației','Recunoașterea respirației superficiale și a pauzelor involuntare','Învățarea unui ritm respirator confortabil'],
['Recunoașterea schimbărilor de stare prin respirație','Relaxare și reducerea stresului prin tehnici blânde, adaptate persoanei','Crearea unui răgaz înainte de reacțiile automate'],
['Antrenarea concentrării pe ritm și respirație','Pregătirea atenției pentru meditație','Un reper simplu pentru revenirea în prezent']],
'lc-tab-buteyko':[
['Conștientizarea și ajustarea tiparelor respiratorii.','Încurajarea unei respirații nazale mai liniștite.','Explorarea treptată a confortului respirator.'],
['Recunoașterea schimbărilor respirației în situații stresante.','Un instrument de sprijin pentru relaxare și calm.','Mai multă conștientizare a reacțiilor personale la stres.'],
['Antrenarea atenției asupra ritmului respirator.','O ancoră pentru revenirea în prezent.','Dezvoltarea unei relații mai conștiente cu respirația în viața de zi cu zi.']],
'lc-tab-resumi':[
['Conștientizarea senzațiilor și a tensiunilor din corp.','Mișcare conștientă și susținerea relaxării musculare.','O relație mai atentă cu propria respirație.'],
['Un spațiu pentru observarea și exprimarea emoțiilor.','Susținerea echilibrului emoțional și a gestionării stresului.','Reconectare cu propriile nevoi, într-un ritm personal.'],
['Revenirea cu atenția în momentul prezent.','Un răgaz de la ritmul alert al vieții cotidiene.','Spațiu pentru liniște, introspecție și integrare.']]
};"""

occ3 = content.count(OLD_BENEFITS_TAIL)
assert occ3 == 1, f"benefits tail occ={occ3}"
content = content.replace(OLD_BENEFITS_TAIL, NEW_BENEFITS_TAIL)

open(path, 'w', encoding='utf-8').write(content)
print("OK. length before:", orig_len, "after:", len(content))
