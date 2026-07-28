const fs=require('node:fs'),path=require('node:path'),yaml=require('yaml');
const dir=path.join(process.cwd(),'src','content','suburbs');
const profiles=new Map(fs.readFileSync('tools/suburb-profiles.psv','utf8').trim().split(/\r?\n/).map(line=>{const a=line.split('|');return [a[1],{homes:a[5],access:a[6],focus:a[8]}]}));
const extras={'south-melbourne':{homes:'apartments, terraces and townhouses on the city fringe',access:'intercoms, key collection and permit requirements',focus:'regular upkeep, targeted help and move-related cleaning'},'north-melbourne':{homes:'terraces, apartments and townhouses near major institutions',access:'intercoms, key collection and building-entry details',focus:'selected tasks, regular upkeep and broader home resets'},'east-melbourne':{homes:'heritage apartments, terraces and compact city-fringe homes',access:'intercoms, key collection and permit requirements',focus:'careful upkeep across detailed interiors'},'west-melbourne':{homes:'apartments, terraces and city-fringe residences',access:'intercoms, key collection and shared-entry details',focus:'routine upkeep, one-off cleaning and moving support'}};
Object.entries(extras).forEach(function(x){profiles.set(x[0],x[1])});
const summaries=[
 p=>'Homes in this area include '+p.homes+'. A useful booking explains '+p.access+' and identifies the rooms that matter most, so the service can be shaped around '+p.focus+'.',
 p=>'The local housing mix ranges across '+p.homes+'. Share '+p.access+' before the visit, then use the task list to guide '+p.focus+' in a practical way.',
 p=>'For '+p.homes+', the booking can set out '+p.access+' alongside the work that needs attention. Those details make it easier to organise '+p.focus+'.',
 p=>'A clear local brief starts with '+p.homes+' and any '+p.access+'. Add the important rooms and tasks so the appointment reflects '+p.focus+'.',
 p=>'Different properties need different plans. Describe '+p.homes+', confirm '+p.access+' and use the booking notes to give '+p.focus+' a clear direction.'
];
const cards=[
 [p=>'Before the visit, explain '+p.access+'. Clear arrival notes help the cleaner reach the home prepared and begin the appointment with a practical plan.',p=>'Choose the service around '+p.focus+'. Compare a focused hourly visit with regular or detailed cleaning, based on the condition of the property.',p=>'For '+p.homes+', flag the rooms that receive the most daily use. Include extras at the same time so the task order stays useful.'],
 [p=>'Share '+p.access+' early in the booking. It gives the cleaner a clearer route into the property and keeps the start of the visit straightforward.',p=>'When the aim is '+p.focus+', match the service to the workload. A priority list and a broader clean should be planned differently.',p=>'The room list can guide the whole appointment. This is especially useful for '+p.homes+', where different spaces may need attention first.'],
 [p=>'Access can affect the start of cleaning day. Add '+p.access+' before confirmation so the cleaner has the right information on arrival.',p=>'Think about the outcome rather than a generic package. Homes needing '+p.focus+' may suit a different scope from a light maintenance visit.',p=>'Set the priorities in the order they matter to the household. That helps the cleaner work through '+p.homes+' with a clear purpose.'],
 [p=>'A smoother arrival begins with '+p.access+'. Include those details in the booking so the cleaner can focus time inside the home rather than at the entry.',p=>'Service choice should reflect '+p.focus+'. Use hourly cleaning for selected work, or choose a broader option when more of the home needs care.',p=>'List the important rooms, surfaces and extras before cleaning day. For '+p.homes+', this makes the available time easier to use well.'],
 [p=>'Give the cleaner a practical arrival plan by noting '+p.access+'. It is a simple step that helps the visit start without unnecessary uncertainty.',p=>'Compare the options against the real workload. '+p.focus+' may call for a more detailed plan than a routine clean.',p=>'Make the task list specific to the home. Clear priorities help the cleaner organise work across '+p.homes+' and focus on what matters most.']
];
function pad(text,min,max){const fillers=[' This keeps the booking clear.',' It gives the visit a practical structure.',' The cleaner can then prepare with confidence.'];let out=text;for(const filler of fillers){if(out.length>=min)break;if(out.length+filler.length<=max)out+=filler;}return out;}
const stats=[];
for(const file of fs.readdirSync(dir).filter(f=>f.endsWith('.md')&&!f.startsWith('_'))){
 const full=path.join(dir,file),raw=fs.readFileSync(full,'utf8'),end=raw.indexOf('\n---',4),data=yaml.parse(raw.slice(4,end)),slug=file.slice(0,-3),p=profiles.get(slug);
 if(!p)throw new Error('Missing profile '+slug);
 const i=stats.length,set=cards[i%cards.length];
 data.summary=pad(summaries[i%summaries.length](p),230,270);
 data.localHighlights=data.localHighlights.slice(0,3).map((h,n)=>({title:h.title,text:pad(set[n](p),176,205)}));
 stats.push({file:file,summary:data.summary.length,cards:data.localHighlights.map(h=>h.text.length)});
 fs.writeFileSync(full,'---\n'+yaml.stringify(data)+'---\n','utf8');
}
const values=stats.flatMap(x=>x.cards);console.log(JSON.stringify({pages:stats.length,summaryMin:Math.min(...stats.map(x=>x.summary)),summaryMax:Math.max(...stats.map(x=>x.summary)),cardMin:Math.min(...values),cardMax:Math.max(...values),kew:stats.find(x=>x.file==='kew.md')},null,2));