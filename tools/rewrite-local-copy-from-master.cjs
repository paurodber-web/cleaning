const fs=require('node:fs');
const path=require('node:path');
const yaml=require('yaml');
const dir=path.join(process.cwd(),'src','content','suburbs');
const master=fs.readFileSync('C:/Users/Pau Rodriguez/Downloads/maid-at-home-suburb-pages-master.md','utf8');
const tick=String.fromCharCode(96),fence=tick.repeat(3);
const re=new RegExp('\\*\\*Filename:\\*\\*\\s*'+tick+'([^'+tick+']+)'+tick+'\\s*\\r?\\n\\r?\\n'+fence+'yaml\\r?\\n([\\s\\S]*?)\\r?\\n'+fence,'g');
const source=new Map([...master.matchAll(re)].map(m=>[m[1],yaml.parse(m[2])]));
const endings=[
  'Clear notes make the arrival and task order easier to manage.',
  'This gives the cleaner a useful picture before cleaning day.',
  'It keeps the agreed priorities visible from the start of the visit.',
  'The result is a clearer plan for the selected cleaning work.',
  'That preparation helps the booked time stay focused on the home.',
  'It makes the practical side of the appointment easier to coordinate.',
  'This helps turn the request into a realistic plan for the visit.',
  'Those details help the service begin with fewer loose ends.',
  'It gives the team a clearer starting point for the appointment.',
  'The booking can then reflect the needs of the individual property.',
  'This supports a smoother arrival and a more useful cleaning visit.',
  'The cleaner can then focus on the areas that matter most.'
];
const cardEndings=[
  'It helps the visit begin without avoidable delays.',
  'That keeps the arrival side of the booking straightforward.',
  'This gives the cleaner a clear starting point at the property.',
  'The available time can then stay focused on the selected work.',
  'That makes the task order easier to follow during the visit.',
  'It is a simple way to keep the appointment practical and clear.'
];
function sentences(text){return String(text||'').replace(/\s+/g,' ').trim().match(/[^.!?]+[.!?]+(?=\s|$)|[^.!?]+$/g)||[];}
function clean(s){return String(s).replace(/\s+/g,' ').trim();}
function trimSentence(text,max){
  const s=clean(text);
  if(s.length<=max)return s;
  const limit=s.slice(0,max-1);
  const comma=Math.max(limit.lastIndexOf(','),limit.lastIndexOf(';'),limit.lastIndexOf(':'));
  const space=limit.lastIndexOf(' ');
  const cut=comma>Math.floor(max*.48)?comma:space;
  return limit.slice(0,cut).replace(/[,:; ]+$/,'')+'.';
}
function compose(sourceText,min,max,ending){
  const list=sentences(sourceText).map(clean);
  const candidates=list.filter(sentence=>sentence.length<=max);
  let out=(candidates.sort((a,b)=>b.length-a.length)[0]||trimSentence(sourceText,Math.min(max,190)));
  if(out.length<min){
    const candidate=out+' '+ending;
    if(candidate.length<=max)out=candidate;
  }
  return out;
}
function padFinal(text,min,max,seed){
  let out=text; const fillers=[seed,'This keeps the plan clear.','It helps the cleaner prepare for the visit.','That makes the booking easier to manage.','It gives the appointment a useful structure.'];
  let cursor=0;
  while(out.length<min && cursor<fillers.length){
    const valid=fillers.slice(cursor).filter(add=>out.length+1+add.length<=max);
    if(!valid.length)break;
    const chosen=valid[valid.length-1];
    out=out+' '+chosen; cursor=fillers.indexOf(chosen)+1;
  }
  return out;
}
const stats=[];
for(const file of fs.readdirSync(dir).filter(f=>f.endsWith('.md')&&!f.startsWith('_'))){
  const full=path.join(dir,file),raw=fs.readFileSync(full,'utf8'),end=raw.indexOf('\n---',4),data=yaml.parse(raw.slice(4,end)),masterData=source.get(file);
  if(!masterData)throw new Error('No master source for '+file);
  const local=masterData.localSection;
  const introSource=local.intro+' '+masterData.hero.description;
  data.summary=padFinal(compose(introSource,230,255,endings[stats.length%endings.length]),230,255,endings[stats.length%endings.length]);
  data.localHighlights=local.cards.slice(0,3).map((card,index)=>({
    title:card.title,
    text:padFinal(compose(card.text,176,196,cardEndings[(stats.length*3+index)%cardEndings.length]),176,196,cardEndings[(stats.length*3+index)%cardEndings.length])
  }));
  stats.push({file,summary:data.summary.length,cards:data.localHighlights.map(h=>h.text.length)});
  fs.writeFileSync(full,'---\n'+yaml.stringify(data)+'---\n','utf8');
}
const cards=stats.flatMap(x=>x.cards);
console.log(JSON.stringify({pages:stats.length,summaryMin:Math.min(...stats.map(x=>x.summary)),summaryMax:Math.max(...stats.map(x=>x.summary)),cardMin:Math.min(...cards),cardMax:Math.max(...cards),samples:stats.slice(0,3)},null,2));
