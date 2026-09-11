from pathlib import Path

index = Path("index.html")
text = index.read_text(encoding="utf-8")

css_anchor = ".rikaNav{width:min(100%,520px);margin-top:10px}button{appearance:none;"
css_new = ".rikaNav{width:min(100%,520px);margin-top:10px}.tocSpecial{width:100%;margin-top:16px;text-align:left;border-radius:18px;padding:15px 17px;background:linear-gradient(135deg,#3b1555,#6b2f8f);border:1px solid #d9b5ef66}.tocSpecial small{display:block;color:var(--gold);font-size:10px;letter-spacing:.16em;margin-bottom:5px}.tocSpecial strong{font-size:15px}.endStory{margin-top:28px;width:min(82vw,390px)}.storyPage{padding:20px 16px 30px}.storySheet{width:min(100%,560px)}.storyCard{position:relative;background:radial-gradient(circle at 85% 8%,#6b2e8b,#35134b 34%,#1c0b2b 74%);border:1px solid #c58af075;border-radius:24px;padding:28px 24px 24px;min-height:min(680px,calc(100dvh - 42px));display:flex;flex-direction:column;box-shadow:0 22px 70px #0005}.storyTop{margin-bottom:22px}.storyKicker{font:10px Georgia,serif;letter-spacing:.18em;color:var(--gold);margin-bottom:10px}.storyTimeline{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding:0 0 7px}.storyTimeline::-webkit-scrollbar{display:none}.storyStep{flex:0 0 auto;font-size:10px;color:#8e7799;white-space:nowrap}.storyStep.on{color:#f2ddff;font-weight:700}.storyStep.done{color:#bca4c8}.storyLine{height:1px;background:#ffffff1f;position:relative}.storyLineFill{height:1px;background:var(--gold);transition:width .35s ease}.storyBody{flex:1;display:flex;flex-direction:column;justify-content:center}.storyTitle{font-size:28px;line-height:1.35;margin:0 0 22px;font-weight:650}.storyText{font-size:18px;line-height:1.9;color:#f4edf7}.storyText p{margin:0 0 18px}.storyText p:last-child{margin-bottom:0}.storyText strong{display:block;font-size:22px;line-height:1.65;color:#fff;margin:24px 0;font-weight:750}.storyText .beat{font-size:24px;line-height:1.6;margin:30px 0}.storyNav{margin-top:24px}.storyCount{text-align:center;color:#aa91b5;font-size:11px;margin-top:11px}.storyFinal .storyCard{justify-content:center;min-height:calc(100dvh - 50px);text-align:center}.storyFinal .storyTop{display:none}.storyFinal .storyBody{justify-content:center}.storyFinal .storyTitle{font-size:30px;line-height:1.65;margin:0}.storyFinal .storySign{font-size:18px;margin-top:32px;color:#eadcff}.storyFinal .storyNav{margin-top:48px}button{appearance:none;"
if css_anchor not in text:
    raise SystemExit("CSS anchor not found")
text = text.replace(css_anchor, css_new, 1)

media_anchor = "@media(max-width:380px){.tocList{grid-template-columns:1fr}.message,.favorite{font-size:18px}.long-name .senderName{font-size:19px}}"
media_new = "@media(max-width:380px){.tocList{grid-template-columns:1fr}.message,.favorite{font-size:18px}.long-name .senderName{font-size:19px}.storyCard{padding:24px 19px 20px}.storyTitle{font-size:25px}.storyText{font-size:17px}.storyText strong{font-size:20px}}"
if media_anchor not in text:
    raise SystemExit("media anchor not found")
text = text.replace(media_anchor, media_new, 1)

toc_anchor = '''<section id="toc" class="page"><div class="sheet toc"><div class="eyebrow">LETTERS FOR MIBU　☆</div><h1>届いた手紙 🐈‍⬛</h1><div id="tocList" class="tocList"></div><div class="nav"><button onclick="showPage('intro',-1)">← はじめに</button><button onclick="openLetter(0,1)">最初から読む →</button></div></div></section>'''
toc_new = '''<section id="toc" class="page"><div class="sheet toc"><div class="eyebrow">LETTERS FOR MIBU　☆</div><h1>届いた手紙 🐈‍⬛</h1><div id="tocList" class="tocList"></div><button class="tocSpecial" onclick="openStory(0,1)"><small>SPECIAL CONTENT</small><strong>このアプリができるまで。</strong></button><div class="nav"><button onclick="showPage('intro',-1)">← はじめに</button><button onclick="openLetter(0,1)">最初から読む →</button></div></div></section>'''
if toc_anchor not in text:
    raise SystemExit("TOC anchor not found")
text = text.replace(toc_anchor, toc_new, 1)

end_anchor = '''<section id="end" class="page"><div class="sheet end"><div class="eyebrow">HAPPY BIRTHDAY · MIBU　☆ 🐈‍⬛</div><div class="big">Thank you<br>for being MIBU.</div><div class="names">たくさんの「おめでとう」と<br>「ありがとう」を込めて。</div></div></section>'''
end_new = '''<section id="end" class="page"><div class="sheet end"><div class="eyebrow">HAPPY BIRTHDAY · MIBU　☆ 🐈‍⬛</div><div class="big">Thank you<br>for being MIBU.</div><div class="names">たくさんの「おめでとう」と<br>「ありがとう」を込めて。</div><button class="endStory" onclick="openStory(0,1)">このアプリができるまで。</button></div></section>
<section id="storyPage" class="page storyPage"><div id="storySheet" class="sheet storySheet"><div class="storyCard"><div class="storyTop"><div class="storyKicker">SPECIAL CONTENT</div><div id="storyTimeline" class="storyTimeline"></div><div class="storyLine"><div id="storyLineFill" class="storyLineFill"></div></div></div><div class="storyBody"><h1 id="storyTitle" class="storyTitle"></h1><div id="storyText" class="storyText"></div></div><div id="storyNav" class="nav storyNav"><button onclick="prevStory()">← 前へ</button><button onclick="nextStory()">次へ →</button></div><div id="storyCount" class="storyCount"></div></div></div></section>'''
if end_anchor not in text:
    raise SystemExit("end anchor not found")
text = text.replace(end_anchor, end_new, 1)

const_anchor = 'const rikaAfter=publicationOrder.indexOf("ネビル🥸")+1;\nlet current=0,timer=null,startX=0,startY=0;'
story_js = r'''const rikaAfter=publicationOrder.indexOf("ネビル🥸")+1;
const storyStages=["7月","8月","8/11","8月後半","9/1","9/10","9/11","9/12"];
const storyPages=[
{stage:"7月",title:"このアプリができるまで。",html:`<p>7月　はじまり</p><p>ミブが休止していた頃。</p><p>「生誕までに、できるだけたくさん<br><br>ミブのいいところ、好きなところを集めたいな」</p><p>最初は、ほんまにそれくらいの思いつきでした。</p><p>まだ何を作るかも、<br><br>どうやって渡すかも決まってませんでした。</p>`},
{stage:"8月",title:"8月　「本にしよう」",html:`<p>ミブが戻ってきて、</p><p>「せっかくなら、生誕の日に本にして渡そう」</p><p>と決定。</p><p>配信で出会ってから約2年。</p><p>今ライブに来ている人だけじゃなく、</p><p>これまでミブと出会ってきた人たちの言葉も集めたい。</p><p>だから、手書きの色紙ではなく、</p><p>DMやTikTokのメッセージでも参加できる形にしました。</p>`},
{stage:"8/11",title:"8/11　だんだん本気になる",html:`<p>いそやんに企画を相談。</p><p>そしてリバプレのライブでは、<br><br>社長にも直接相談。</p><p>「ファンだけじゃなくて、<br><br>ミブを支えてくれている関係者からのメッセージもほしいです」</p><p>気づけば、最初に思っていたより<br><br>ずっと大きな企画になり始めていました。</p>`},
{stage:"8月後半",title:"8月後半　ちょっと困る",html:`<p>本にするなら制作期間が必要なので、</p><p>メッセージの締め切りは8月いっぱい。</p><p>でも、</p><p>「ちゃんと考えたいから、もう少し待ってほしい」</p><p>という人も出てきました。</p><p>同時に、どこで本にしようか<br><br>色々調べていたものの……</p><p>「なんか、ありきたりやなぁ……」</p>`},
{stage:"8月後半",title:"そこで、ひらめく。",html:`<p>ちょうどその頃、</p><p>AIの勉強も進んでいました。</p><strong class="beat">「……あれ？<br><br>これ、アプリ作れるんちゃう？」</strong><p>しかもアプリなら、</p><p>もう少しメッセージを待てるかもしれない。</p><p>ということで、9月頭に試作開始。</p>`},
{stage:"8月後半",title:"……思ってたより、いいやん。",html:`<p>試しに作ってみたアプリが、</p><p>想像していたよりいい感じに完成。</p><strong class="beat">「よし、アプリでいこう。」</strong><p>こうして、メインはアプリに決まりました。</p>`},
{stage:"8月後半",title:"でも。",html:`<p>作っているうちに、また思います。</p><p>「でも、物として残るものも<br><br>作ってあげたいよなぁ……」</p><p>それなら——</p><strong class="beat">自分で作ろう。</strong><p>アプリと同じメッセージを<br><br>ハガキサイズのカードにして、</p><p>リアル版のメッセージBOOKも<br><br>作ることになりました。</p>`},
{stage:"9/1",title:"9/1　ファイル購入",html:`<p>80枚入るファイルを購入。</p><p>この時の気持ち。</p><strong class="beat">「80枚あったら余裕でいけるやろ。」</strong><p>…………。</p>`},
{stage:"9/1",title:"ちなみに、ひとりだけ特別参加。",html:`<p>うみうからは、</p><p>本にする予定だった頃から</p><p>「別で手紙として渡したい」</p><p>と申し出があったので、</p><p>今回は手紙で<br><br>参加してもらうことになりました。</p>`},
{stage:"9/10",title:"9/10　事件発生。",html:`<p>完成したカードを裁断しながら、<br><br>枚数を確認。</p><p>予想していた以上に、<br><br>たくさんのメッセージが集まっていました。</p><p>そして気づく。</p><strong class="beat">「……80枚じゃ足りん。」</strong><p>余裕とは。</p>`},
{stage:"9/10",title:"9/10　事件発生。",html:`<p>急遽、いそやんとジンベイの複数カードを<br><br>それぞれ1つのポケットにまとめることに。</p><p>計算し直して……</p><strong class="beat">「よし。これでちょうど！」</strong>`},
{stage:"9/11",title:"9/11 夜",html:`<p>りかさんから<br><br>メッセージカードが届く。</p><p>もちろん入れたい。</p><p>でも……</p><strong class="beat">「もう入れるところないやん。」</strong><p>80ポケット、満員です。</p>`},
{stage:"9/11",title:"9/11 夜",html:`<p>悩んだ結果、</p><p>同じモデレーターのネビルのポケットに<br><br>りかさんのカードをこっそり忍ばせることに。</p><p>最後のひとりまで、<br><br>無事入りました。</p>`},
{stage:"9/12",title:"9/12 朝方",html:`<p>生誕祭当日。</p><p>まだ残りのカードを<br><br>裁断している途中で、ふと思う。</p><strong class="beat">「あ、制作秘話みたいなん入れたら<br><br>面白いんちゃう？」</strong><p>……ということで、</p><p>最後の最後に<br><br>このページまで増えました。笑</p>`},
{stage:"9/12",title:"そして、完成。",html:`<p>たくさんの人から届いた言葉を、</p><p>ひとつの場所に残すことができました。</p>`},
{stage:"9/12",title:"リアルBOOKを見るミブへ",html:`<p>実は、80ポケットでは<br><br>全員分が入りきらなかったので、</p><strong>いそやんとジンベイのメッセージは、<br><br>それぞれ複数枚を1つのポケットに入れています。</strong><p>そして、最後に届いた</p><strong>りかさんのメッセージカードは、<br><br>ネビルのメッセージカードと同じポケットに<br><br>こっそり入っています。</strong><p>見落とさないように、</p><p>ちゃんと中まで見てね。笑</p>`},
{stage:"9/12",title:"このアプリが、\nミブのお守りになりますように。",html:`<div class="storySign">—— ジンベイ</div>`,final:true}
];
let current=0,currentStory=0,timer=null,startX=0,startY=0;'''
if const_anchor not in text:
    raise SystemExit("const anchor not found")
text = text.replace(const_anchor, story_js, 1)

build_anchor = '''function buildToc(){const x=document.getElementById('tocList');x.innerHTML='';letters.forEach((l,i)=>{if(i===rikaAfter)x.appendChild(rikaTocButton());if(i===specialAfter)x.appendChild(specialTocButton());let b=document.createElement('button');b.className='tocItem';b.innerHTML=`<span class="tocNo">${String(i+1).padStart(2,'0')}</span><span class="tocName">${l.name}</span><span>${i%2?'🐈‍⬛':'☆'}</span>`;b.onclick=()=>openLetter(i,1);x.appendChild(b)})}'''
story_functions = build_anchor + r'''
function openStory(i=0,dir=1){currentStory=Math.max(0,Math.min(i,storyPages.length-1));renderStory();showPage('storyPage',dir)}
function renderStory(){const p=storyPages[currentStory],sheet=document.getElementById('storySheet'),title=document.getElementById('storyTitle'),body=document.getElementById('storyText'),timeline=document.getElementById('storyTimeline'),fill=document.getElementById('storyLineFill'),nav=document.getElementById('storyNav'),count=document.getElementById('storyCount');sheet.classList.toggle('storyFinal',!!p.final);title.innerHTML=p.title.replace(/\n/g,'<br>');body.innerHTML=p.html;timeline.innerHTML='';const stageIndex=Math.max(0,storyStages.indexOf(p.stage));storyStages.forEach((s,i)=>{const span=document.createElement('span');span.className='storyStep '+(i===stageIndex?'on':i<stageIndex?'done':'');span.textContent=s;timeline.appendChild(span)});fill.style.width=((stageIndex+1)/storyStages.length*100)+'%';count.textContent=`${currentStory+1} / ${storyPages.length}`;nav.innerHTML=p.final?'<button onclick="prevStory()">← 前へ</button><button onclick="showToc(-1)">☰ 目次へ戻る</button>':'<button onclick="prevStory()">← 前へ</button><button onclick="nextStory()">次へ →</button>'}
function nextStory(){if(currentStory<storyPages.length-1)openStory(currentStory+1,1);else showToc(1)}
function prevStory(){if(currentStory>0)openStory(currentStory-1,-1);else showToc(-1)}'''
if build_anchor not in text:
    raise SystemExit("buildToc anchor not found")
text = text.replace(build_anchor, story_functions, 1)

touch_forward = "else if(active==='letterPage')nextLetter();else if(active==='rikaPage')openLetter(rikaAfter,1);else if(active==='special')openLetter(specialAfter,1)"
touch_forward_new = "else if(active==='letterPage')nextLetter();else if(active==='rikaPage')openLetter(rikaAfter,1);else if(active==='special')openLetter(specialAfter,1);else if(active==='storyPage')nextStory()"
if touch_forward not in text:
    raise SystemExit("touch forward anchor not found")
text = text.replace(touch_forward, touch_forward_new, 1)

touch_back = "else if(active==='letterPage')prevLetter();else if(active==='rikaPage')openLetter(rikaAfter-1,-1);else if(active==='special')openLetter(specialAfter-1,-1);else if(active==='end')openLetter(letters.length-1,-1)"
touch_back_new = "else if(active==='letterPage')prevLetter();else if(active==='rikaPage')openLetter(rikaAfter-1,-1);else if(active==='special')openLetter(specialAfter-1,-1);else if(active==='end')openLetter(letters.length-1,-1);else if(active==='storyPage')prevStory()"
if touch_back not in text:
    raise SystemExit("touch back anchor not found")
text = text.replace(touch_back, touch_back_new, 1)

index.write_text(text, encoding="utf-8")
