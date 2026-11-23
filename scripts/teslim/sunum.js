// YTÜ Yıldız Teknopark başvurusu için "Firma / Proje Sunumu" üretir.
// Kullanım: PPTX_SKILL_DIR=<pptx skill dizini> node scripts/teslim/sunum.js
//   →  teslim/KAYNAK-YZ_Firma_Proje_Sunumu.pptx
const path = require("path");
const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa6");

const SKILL = process.env.PPTX_SKILL_DIR;
const { applyTheme } = require(path.join(SKILL, "scripts", "apply_theme.js"));
const OUT = path.resolve(__dirname, "..", "..", "teslim", "KAYNAK-YZ_Firma_Proje_Sunumu.pptx");

const THEME = {
  name: "KAYNAK-YZ",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1F2933", lt1: "FFFFFF", dk2: "0B3D3A", lt2: "EEF4F2",
    accent1: "F2A541", accent2: "14786E", accent3: "8FC1B5",
    accent4: "C8553D", accent5: "5B6770", accent6: "2E5E8C",
    hlink: "14786E", folHlink: "5B6770",
  },
};
const HEX = THEME.colors;
const PH = "C8553D"; // firma tarafından doldurulacak alanların rengi

async function ikon(ad, renk = "FFFFFF") {
  const Comp = fa[ad];
  if (!Comp) throw new Error("Bilinmeyen ikon: " + ad);
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Comp, { color: "#" + renk, size: 256 }));
  const png = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + png.toString("base64");
}

(async () => {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.title = "KAYNAK-YZ · Firma / Proje Sunumu";
  pres.subject = "YTÜ Yıldız Teknopark Aday Firma Başvurusu";
  pres.author = "Başvuran Firma";
  const C = pres.SchemeColor;

  // ---------- Yerleşimler ----------
  pres.defineSlideMaster({
    title: "KOYU",
    background: { color: HEX.dk2 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.1, w: 11.7, h: 1.9, fontFace: "Cambria", fontSize: 40, bold: true, color: C.background1, valign: "bottom" }, text: "" } },
      { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 4.15, w: 11.7, h: 1.2, fontFace: "Calibri", fontSize: 20, color: C.accent3, valign: "top" }, text: "" } },
    ],
  });
  pres.defineSlideMaster({
    title: "ICERIK",
    background: { color: HEX.lt1 },
    margin: [0.5, 0.6, 0.7, 0.6],
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.35, w: 12.1, h: 0.85, fontFace: "Cambria", fontSize: 32, bold: true, color: C.text2, valign: "middle" }, text: "" } },
      { text: { text: "KAYNAK-YZ · YTÜ Yıldız Teknopark Aday Firma Başvurusu", options: { x: 0.6, y: 7.0, w: 8, h: 0.3, fontSize: 10, color: C.accent5, fontFace: "Calibri" } } },
    ],
    slideNumber: { x: 12.2, y: 7.0, w: 0.5, h: 0.3, fontSize: 10, color: C.accent5, fontFace: "Calibri", align: "right" },
  });

  const yeni = (bolum) => pres.addSlide({ masterName: "ICERIK", sectionTitle: bolum });
  const baslik = (s, t) => s.addText(t, { placeholder: "title" });
  const metin = (s, t, o) => s.addText(t, Object.assign({ isTextBox: true, fontSize: 14, color: C.text1, margin: 0, valign: "top" }, o));
  const kart = (s, o) => s.addShape(pres.shapes.ROUNDED_RECTANGLE, Object.assign({ rectRadius: 0.12, fill: { color: C.background2 }, line: { color: C.background2 } }, o));
  async function ikonDaire(s, ad, x, y, d = 0.7, renk = C.accent2) {
    s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: renk }, line: { color: renk } });
    const p = d * 0.26;
    s.addImage({ data: await ikon(ad), x: x + p, y: y + p, w: d - 2 * p, h: d - 2 * p, altText: ad });
  }

  // ---------- 1 · Kapak ----------
  pres.addSection({ title: "Giriş" });
  let s = pres.addSlide({ masterName: "KOYU", sectionTitle: "Giriş" });
  s.addText("KAYNAK-YZ: Türkçe Eğitim İçeriği İçin Kaynağa Dayalı Üretken Yapay Zekâ", { placeholder: "title" });
  s.addText([
    { text: "Kaynağa kilitli soru-cevap · Sokratik ödev desteği · Rubrik tabanlı ön-değerlendirme", options: { breakLine: true } },
    { text: "YTÜ Yıldız Teknopark Aday Firma Başvurusu · Aralık 2026", options: { fontSize: 16, color: C.background1 } },
  ], { placeholder: "body" });
  s.addImage({ data: await ikon("FaGraduationCap", HEX.accent1), x: 0.8, y: 0.8, w: 0.9, h: 0.9, altText: "Mezuniyet kepi" });
  s.addText("‹Firma Unvanı›", { isTextBox: true, x: 0.8, y: 6.3, w: 8, h: 0.5, fontSize: 16, color: C.accent1, margin: 0, bold: true });
  s.addNotes("Açılış: Kurumumuz bir eğitim kurumudur; bu projede eğitim hizmetimizi güçlendirecek, ders kaynağına bağlı kalan ve öğrenmeyi destekleyen bir yapay zekâ geliştirilmektedir.");

  // ---------- 2 · Sunum akışı ----------
  s = yeni("Giriş");
  baslik(s, "Sunum Akışı");
  const gundem = ["Kurum profili ve projenin kurum için anlamı", "Sorun tanımı ve mevcut yaklaşımların sınırlılıkları", "Tekniğin bilinen durumu ve önerilen çözüm", "Ar-Ge içeriği ve ölçülebilir hedefler", "Sistem mimarisi ve teknoloji altyapısı", "Doğrulama yaklaşımı ve uygulama takvimi", "Proje ekibi ve üniversite-sanayi iş birliği", "Pazar, ticarileşme, ithal ikame ve ihracat", "Bütçe, finansman ve Yıldız Teknopark'a katkı"];
  gundem.forEach((g, i) => {
    const x = 0.6 + (i % 2) * 6.15, y = 1.55 + Math.floor(i / 2) * 1.05;
    kart(s, { x, y, w: 5.95, h: 0.85 });
    metin(s, String(i + 1).padStart(2, "0"), { x: x + 0.25, y, w: 0.8, h: 0.85, fontSize: 24, bold: true, color: C.accent2, fontFace: "Cambria", valign: "middle" });
    metin(s, g, { x: x + 1.1, y, w: 4.7, h: 0.85, fontSize: 16, valign: "middle", color: C.text2 });
  });
  s.addNotes("Sunum dokuz bölümden oluşmaktadır. Tahmini süre 20 dakika ve ardından soru-cevap.");

  // ---------- 3 · Kurum profili ----------
  s = yeni("Giriş");
  baslik(s, "Kurum Profili");
  metin(s, [
    { text: "‹Firma Unvanı›", options: { bold: true, color: PH } },
    { text: ", ‹kuruluş yılı› yılından bu yana ‹eğitim alanları› alanlarında bireylere eğitim hizmeti sunan bir eğitim kurumudur. Kurumun asıl faaliyet alanı eğitimdir; yapay zekâ, bu hizmetin kalitesini ve erişilebilirliğini artırmak amacıyla geliştirilmektedir." },
  ], { x: 0.6, y: 1.45, w: 12.1, h: 1.0, fontSize: 16 });
  const istat = [
    ["240 M TL", "yıllık gelir (yaklaşık)", false],
    ["200–300", "aylık aktif öğrenci", false],
    ["‹X›", "eğitmen", true],
    ["7 kişi", "Ar-Ge ekibi (teknoparkta, planlanan)", false],
  ];
  istat.forEach(([n, a, ph], i) => {
    const x = 0.6 + i * 3.1;
    kart(s, { x, y: 2.85, w: 2.85, h: 2.4 });
    metin(s, n, { x: x + 0.2, y: 3.15, w: 2.5, h: 1.0, fontSize: 36, bold: true, color: ph ? PH : C.accent2, fontFace: "Cambria" });
    metin(s, a, { x: x + 0.25, y: 4.25, w: 2.4, h: 0.8, fontSize: 16, color: C.text1 });
  });
  await ikonDaire(s, "FaCode", 0.6, 5.75, 0.6);
  metin(s, "Proje; kurum bünyesindeki yazılım ekibi, istihdam edilecek kıdemli yapay zekâ mühendisi ve YTÜ akademik danışmanları tarafından yürütülecektir.", { x: 1.4, y: 5.8, w: 11.2, h: 0.6, fontSize: 15, valign: "middle" });
  s.addNotes("Kurumun mali gücü projenin gerçekleştirilebilirliğinin teminatıdır. Proje öz kaynakla finanse edilecektir (bütçe yıllık gelirin yaklaşık %7–9'u). Kırmızı ‹…› alanları kurum bilgisiyle doldurulmalıdır.");

  // ---------- 4 · Projenin kurum için anlamı ----------
  s = yeni("Giriş");
  baslik(s, "Projenin Kurumumuz İçin Anlamı");
  const anlam = [
    ["FaBookOpen", "Pedagoji önceliklidir", "Yapay zekâ, eğitmenin yerini almak için değil; eğitmenin öğrenciye ayırdığı zamanı artırmak ve öğrenciye ders dışında destek sağlamak için tasarlanmaktadır."],
    ["FaSchool", "İlk kullanıcı kurumumuzdur", "Sistem, aylık 200–300 öğrencimiz ve eğitmenlerimizle gerçek ortamda geliştirilecek ve doğrulanacaktır."],
    ["FaHandshake", "Ardından sektöre sunulacaktır", "Aynı ihtiyacı yaşayan kurslar, okullar ve kurumsal akademiler için yerli ve güvenilir bir çözüm oluşturulacaktır."],
  ];
  for (let i = 0; i < anlam.length; i++) {
    const [ic, b, tx] = anlam[i];
    const x = 0.6 + i * 4.1;
    kart(s, { x, y: 1.5, w: 3.85, h: 3.45 });
    await ikonDaire(s, ic, x + 0.3, 1.8, 0.8);
    metin(s, b, { x: x + 0.3, y: 2.8, w: 3.3, h: 0.5, fontSize: 19, bold: true, color: C.text2 });
    metin(s, tx, { x: x + 0.3, y: 3.35, w: 3.3, h: 1.5, fontSize: 15 });
  }
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 5.3, w: 12.1, h: 1.2, rectRadius: 0.12, fill: { color: C.text2 }, line: { color: C.text2 } });
  metin(s, [
    { text: "Kurumsal yapı: ", options: { bold: true, color: C.accent1 } },
    { text: "Teknopark şubesinde yalnızca Ar-Ge ve yazılım geliştirme faaliyeti yürütülecek; eğitim hizmeti kurum merkezinde sürdürülecektir.", options: { color: C.background1 } },
  ], { x: 0.95, y: 5.4, w: 11.4, h: 1.0, fontSize: 16, valign: "middle" });
  s.addNotes("Kurum bir yazılım şirketi değil, bir eğitim kurumudur. Bu durum projenin en güçlü yanıdır: hangi sorunun çözülmesi gerektiğini, gerçek öğrenci ve eğitmen verisini ve pilot sahasını kurum sağlamaktadır.");

  // ---------- 5 · Sorun tanımı ----------
  pres.addSection({ title: "Sorun ve çözüm" });
  s = yeni("Sorun ve çözüm");
  baslik(s, "Sorun Tanımı: Ders Sonrasında Öğrenme Desteği");
  const sorun = [
    ["FaUserGraduate", "Öğrenci", "Ders sonrasında ortaya çıkan sorular yanıtsız kalmakta; genel amaçlı araçlar dersle uyumsuz ya da hatalı yanıtlar verebilmektedir."],
    ["FaChalkboardUser", "Eğitmen", "Tekrar eden soruların yanıtlanması ve ödev değerlendirmesi haftada ‹X saat› zaman almakta; geri bildirim gecikmektedir."],
    ["FaBuilding", "Kurum", "Çoğu döviz bazlı 3–5 ayrı araç kullanılmakta; öğrenme kalitesi ölçülememekte ve KVKK yükümlülükleri artmaktadır."],
  ];
  for (let i = 0; i < sorun.length; i++) {
    const [ic, b, t] = sorun[i];
    const x = 0.6 + i * 4.1;
    kart(s, { x, y: 1.5, w: 3.85, h: 3.3 });
    await ikonDaire(s, ic, x + 0.3, 1.8, 0.8);
    metin(s, b, { x: x + 0.3, y: 2.8, w: 3.3, h: 0.5, fontSize: 20, bold: true, color: C.text2 });
    metin(s, t, { x: x + 0.3, y: 3.35, w: 3.3, h: 1.4, fontSize: 15 });
  }
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 5.15, w: 12.1, h: 1.45, rectRadius: 0.12, fill: { color: C.text2 }, line: { color: C.text2 } });
  metin(s, [
    { text: "Kanıt: ", options: { bold: true, color: C.accent1 } },
    { text: "Yaklaşık 1.000 lise öğrencisiyle yapılan randomize kontrollü çalışmada, korumasız sohbet botu kullanan öğrencilerin sonraki sınavda daha düşük puan aldığı; Sokratik korumalı sürümün bu kaybı ortadan kaldırdığı gösterilmiştir.", options: { color: C.background1 } },
    { text: "  (Bastani ve ark., PNAS 2025)", options: { color: C.accent3, fontSize: 12 } },
  ], { x: 0.95, y: 5.3, w: 11.4, h: 1.15, fontSize: 16, valign: "middle" });
  s.addNotes("Eğitmen saat değeri, başvuru öncesi yapılacak eğitmen anketinden gelecek (proje dosyası belge 01 §1.3). RKÇ kanıtı: cevap sızıntısını önlemek bir özellik değil, pedagojik zorunluluk.");

  // ---------- 4 · Genel YZ neden yetmiyor ----------
  s = yeni("Sorun ve çözüm");
  baslik(s, "Genel Amaçlı Yapay Zekâ Araçlarının Sınırlılıkları");
  const neden = [
    ["FaTriangleExclamation", "Kaynağa bağlılık yoktur", "Yanıtlar ders kaynağına dayanmamaktadır. Kaynağa dayalı ürünlerde dahi reddetme oranı %0,2–%11,1 arasında değişmekte ve en büyük kalite farkını oluşturmaktadır."],
    ["FaUserSecret", "Öğrenmeyi zayıflatabilir", "Ödev yanıtını doğrudan verebilmekte ve öğrencinin öğrenme sürecini atlamasına yol açabilmektedir."],
    ["FaLock", "Veri yurt dışında işlenir", "KVKK md. 9 kapsamında yurt dışı aktarım; standart sözleşme ve beş iş günü içinde Kurul'a bildirim yükümlülüğü doğar."],
    ["FaScaleBalanced", "Puanlama güvenilir değildir", "Hazır modellerde insan puanıyla uyum ağırlıklı Kappa ile yaklaşık 0,4–0,7 aralığındadır ve veri setine göre büyük ölçüde değişmektedir."],
  ];
  for (let i = 0; i < neden.length; i++) {
    const [ic, b, t] = neden[i];
    const x = 0.6 + (i % 2) * 6.15, y = 1.55 + Math.floor(i / 2) * 2.55;
    kart(s, { x, y, w: 5.95, h: 2.3 });
    await ikonDaire(s, ic, x + 0.3, y + 0.3, 0.75, C.accent4);
    metin(s, b, { x: x + 1.3, y: y + 0.3, w: 4.4, h: 0.5, fontSize: 20, bold: true, color: C.text2 });
    metin(s, t, { x: x + 1.3, y: y + 0.85, w: 4.4, h: 1.35, fontSize: 15 });
  }
  s.addNotes("Kaynaklar: arXiv 2608.26385 (reddetme davranışı), KVKK yurt dışı aktarım rehberi (7499 s. Kanun), arXiv 2508.02442 ve Springer s44163-026-01002-y (puanlama uyumu).");

  // ---------- 5 · Rekabet ----------
  s = yeni("Sorun ve çözüm");
  baslik(s, "Tekniğin Bilinen Durumu ve Boşluk");
  const hb = (t) => ({ text: t, options: { bold: true, color: HEX.lt1, fill: { color: HEX.dk2 }, align: "center", valign: "middle" } });
  const hc = (t) => {
    const renk = t === "✓" ? HEX.accent2 : t === "✗" ? HEX.accent4 : HEX.accent5;
    return { text: t, options: { align: "center", color: renk, bold: true, fontSize: 18 } };
  };
  const satir = [
    ["Ders kaynağına kilitli soru-cevap", "✓", "~", "~", "✓"],
    ["Sayfa / slayt / video dakikası atfı", "~", "✗", "✗", "✓"],
    ["Kaynak dışı soruyu ölçülmüş biçimde reddetme", "?", "✗", "✗", "✓"],
    ["Ödev cevabı sızıntı kontrolü (Sokratik)", "~", "✗", "✗", "✓"],
    ["Ölçülmüş rubrik puan uyumu", "~", "~", "✗", "✓"],
    ["Yurt içi barındırma / kurum içi kurulum", "✗", "✓", "✓", "✓"],
    ["Kurs işletme işlevleri (kayıt, ödeme)", "✗", "~", "✓", "✓"],
  ];
  const rows = [[hb("Özellik"), hb("Google Classroom + NotebookLM"), hb("Moodle / Canvas + eklenti"), hb("Yerli LMS'ler"), hb("KAYNAK-YZ (hedef)")]];
  satir.forEach((r, i) => {
    const zemin = i % 2 ? HEX.lt1 : HEX.lt2;
    rows.push(r.map((v, j) => {
      const c = j === 0 ? { text: v, options: { color: HEX.dk1 } } : hc(v);
      c.options.fill = { color: j === 4 ? "FDF1DE" : zemin };
      return c;
    }));
  });
  s.addTable(rows, { x: 0.6, y: 1.45, w: 12.1, colW: [4.3, 2.2, 2.0, 1.7, 1.9], fontSize: 14, fontFace: "Calibri", rowH: 0.56, border: { type: "solid", color: "D9E2DF", pt: 0.75 }, valign: "middle" });
  metin(s, "✓ var   ~ kısmen   ✗ yok   ? kamuya açık bilgi yok · Kaynak: Google Workspace Updates (2026), firma web siteleri; rakip iddiaları firma beyanıdır.", { x: 0.6, y: 6.15, w: 12.1, h: 0.5, fontSize: 11, color: C.accent5 });
  s.addNotes("Ana mesaj: Kimse sadakati, reddetmeyi, sızıntıyı ve puan uyumunu ölçüp kuruma göstermiyor. Google'a karşı farkımız: yurt içi veri ve kurum içi kurulum, kurs ve kurumsal eğitim segmenti, ölçülmüş güvenilirlik, Türkçe derinlik.");

  // ---------- 6 · Çözüm ----------
  s = yeni("Sorun ve çözüm");
  baslik(s, "Önerilen Çözüm");
  const adim = [
    ["FaUpload", "Eğitmen kaynak yükler", "PDF, slayt ve ders kaydı"],
    ["FaComments", "Öğrenci soru sorar", "Ders sayfasındaki asistana"],
    ["FaMagnifyingGlass", "Atıflı yanıt ya da ret", "Sayfa ve dakika atfı; kaynakta yoksa yanıt üretilmez"],
    ["FaLightbulb", "Ödevde Sokratik destek", "Yanıt yerine kademeli ipucu"],
    ["FaClipboardCheck", "Rubrikle ön-değerlendirme", "Kanıtlı geri bildirim; not eğitmende"],
  ];
  for (let i = 0; i < adim.length; i++) {
    const [ic, b, t] = adim[i];
    const x = 0.6 + i * 2.48;
    await ikonDaire(s, ic, x + 0.6, 1.65, 1.0, i < 2 ? C.accent5 : C.accent2);
    metin(s, String(i + 1), { x: x + 0.15, y: 1.65, w: 0.45, h: 0.45, fontSize: 18, bold: true, color: C.accent1, fontFace: "Cambria" });
    metin(s, b, { x, y: 2.85, w: 2.25, h: 0.75, fontSize: 16, bold: true, color: C.text2, align: "center" });
    metin(s, t, { x, y: 3.6, w: 2.25, h: 0.9, fontSize: 14, align: "center" });
    if (i < adim.length - 1) s.addShape(pres.shapes.RIGHT_ARROW, { x: x + 1.85, y: 2.0, w: 0.5, h: 0.3, fill: { color: C.accent3 }, line: { color: C.accent3 } });
  }
  kart(s, { x: 0.6, y: 4.95, w: 12.1, h: 1.6 });
  await ikonDaire(s, "FaLayerGroup", 0.9, 5.3, 0.85, C.text2);
  metin(s, [
    { text: "Platform (test yatağı): ", options: { bold: true, color: C.text2 } },
    { text: "kayıt ve roller · ders alanları · canlı ders (yurt içi BigBlueButton) · ödev teslimi · takvim ve bildirim · bireysel ve kurumsal abonelik. Hazır bileşenlerle kurulacak ve toplam eforun %24'ü ile sınırlı tutulacaktır; Ar-Ge içeriği yapay zekâ katmanındadır." },
  ], { x: 2.0, y: 5.25, w: 10.4, h: 1.05, fontSize: 15, valign: "middle" });
  s.addNotes("Platform kısmının rutin yazılım olduğunu açıkça kabul ediyoruz; YZ'nin gerçek kullanıcılarla ölçüleceği zemin olarak ayrı iş paketinde (İP-2) izleniyor.");

  // ---------- 7 · Ar-Ge ----------
  pres.addSection({ title: "Ar-Ge ve yöntem" });
  s = yeni("Ar-Ge ve yöntem");
  baslik(s, "Ar-Ge İçeriği ve Ölçülebilir Hedefler");
  const ar = [
    ["AR-1", "Kaynağa sadakat ve doğru reddetme", "Ticari RAG'lerde ret %0,2–11,1; standart ölçücüler reddetmeyi ölçmüyor", "Sadakat ≥ %95 · ret ≥ %90"],
    ["AR-2", "Türkçe için hibrit bilgi erişimi", "Türkçe gömme sıralaması karşılaştırmalara göre değişiyor", "Recall@5 ≥ %90"],
    ["AR-3", "Rubrik tabanlı puanlama uyumu", "Hazır modellerde ağırlıklı Kappa ≈ 0,4–0,7", "Kappa ≥ 0,75"],
    ["AR-4", "Pedagojik cevap sızıntısı", "Korumasız bot öğrenmeyi düşürüyor (PNAS 2025)", "Sızıntı ≤ %2"],
    ["AR-5", "Çok kipli içerik (PDF, slayt, video)", "Whisper Türkçe WER ≈ %6–8 (temiz veri setleri)", "Ders kaydı WER ≤ %10"],
    ["AR-6", "Yurt içi açık model, maliyet", "Ticari, yurt dışı modellere bağımlılık", "Kalite farkı ≤ %5 · p50 ≤ 3 sn"],
  ];
  const arRows = [[hb("#"), hb("Teknik belirsizlik"), hb("Bugün (literatür)"), hb("Hedef")]];
  ar.forEach((r, i) => {
    const zemin = i % 2 ? HEX.lt1 : HEX.lt2;
    arRows.push([
      { text: r[0], options: { bold: true, color: HEX.accent2, fill: { color: zemin }, align: "center" } },
      { text: r[1], options: { bold: true, color: HEX.dk2, fill: { color: zemin } } },
      { text: r[2], options: { color: HEX.dk1, fill: { color: zemin } } },
      { text: r[3], options: { bold: true, color: HEX.dk2, fill: { color: "FDF1DE" } } },
    ]);
  });
  s.addTable(arRows, { x: 0.6, y: 1.45, w: 12.1, colW: [0.8, 3.6, 4.7, 3.0], fontSize: 14, fontFace: "Calibri", rowH: 0.62, border: { type: "solid", color: "D9E2DF", pt: 0.75 }, valign: "middle" });
  metin(s, "Teknoloji hazırlık seviyesi: TRL 2–3'ten 6–7'ye (gerçek kullanıcılarla pilot). Hedeflere ulaşılabilirlik önceden bilinmemektedir; her biri için hipotez, deney tasarımı ve B planı tanımlanmıştır.", { x: 0.6, y: 6.05, w: 12.1, h: 0.6, fontSize: 13, color: C.accent5 });
  s.addNotes("Hakemin 'Bu sadece RAG mi?' sorusunun cevabı bu slayt: Ar-Ge modelin kendisinde değil, güvenilirlik katmanında. Sadakat ve reddetme aynı anda sağlanmalı; birini artırmak diğerini düşürebilir. Kaynaklar: arXiv 2608.26385, TR-MTEB (EMNLP 2025), TR-TEB, arXiv 2508.02442, arXiv 2510.09030, PNAS 2025, arXiv 2611.03605.");

  // ---------- 8 · Mimari ----------
  s = yeni("Ar-Ge ve yöntem");
  baslik(s, "Sistem Mimarisi");
  const kutu = (x, y, w, h, t, alt, dolgu, yazi) => {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.1, fill: { color: dolgu }, line: { color: dolgu } });
    metin(s, [{ text: t, options: { bold: true, breakLine: !!alt } }].concat(alt ? [{ text: alt, options: { fontSize: 13 } }] : []), { x: x + 0.15, y, w: w - 0.3, h, fontSize: 15, color: yazi, align: "center", valign: "middle" });
  };
  kutu(0.6, 1.45, 7.4, 0.7, "İstemciler", "Öğrenci · Eğitmen · Kurum paneli (web, mobil uyumlu)", C.background2, C.text2);
  kutu(0.6, 2.35, 7.4, 0.6, "API geçidi · kimlik doğrulama · kiracı ayrımı", null, C.background2, C.text2);
  kutu(0.6, 3.15, 2.35, 1.35, "Platform", "ders · ödev · canlı ders", C.accent5, C.background1);
  kutu(3.12, 3.15, 2.35, 1.35, "YZ orkestrasyon", "Ar-Ge çekirdeği", C.accent2, C.background1);
  kutu(5.65, 3.15, 2.35, 1.35, "İçerik işleme", "PDF · slayt · video", C.accent5, C.background1);
  kutu(0.6, 4.7, 7.4, 0.7, "PostgreSQL (pgvector + Türkçe tam metin) · nesne deposu", "satır düzeyi güvenlik ile kurum ayrımı", C.background2, C.text2);
  kutu(0.6, 5.6, 7.4, 0.85, "Yurt içi GPU · açık ağırlıklı modeller", "üretim · gömme · yeniden sıralama · konuşma tanıma", C.text2, C.background1);
  kart(s, { x: 8.4, y: 1.45, w: 4.3, h: 5.0 });
  metin(s, "Soru-cevap hattı", { x: 8.7, y: 1.65, w: 3.8, h: 0.45, fontSize: 18, bold: true, color: C.text2 });
  metin(s, [
    { text: "Niyet ve pedagojik politika", options: { bullet: { type: "number" }, breakLine: true } },
    { text: "Hibrit erişim (yoğun + Türkçe kök bulmalı seyrek) ve yeniden sıralama", options: { bullet: { type: "number" }, breakLine: true } },
    { text: "Cevaplanabilirlik kapısı (ceza-duyarlı eşik)", options: { bullet: { type: "number" }, breakLine: true } },
    { text: "Atıflı, kısıtlı üretim", options: { bullet: { type: "number" }, breakLine: true } },
    { text: "İddia düzeyinde doğrulama → cevap ya da ret", options: { bullet: { type: "number" } } },
  ], { x: 8.7, y: 2.2, w: 3.8, h: 3.0, fontSize: 14, paraSpaceAfter: 6 });
  metin(s, "Aday modeller: Cosmos T1 / Turkish-Llama (YTÜ COSMOS), bge-m3, turkish-e5-large; seçim deneyle yapılır.", { x: 8.7, y: 5.35, w: 3.8, h: 0.95, fontSize: 12, color: C.accent5 });
  s.addNotes("Ar-Ge katmanı (YZ orkestrasyon) kurumun kendi kodudur; platform olgun hazır bileşenlerle kurulur. Mimari modelden bağımsızdır. AB YZ Yasası gereği her YZ kararı kanıt ve model sürümüyle kaydedilir.");

  // ---------- Teknoloji altyapısı ----------
  s = yeni("Ar-Ge ve yöntem");
  baslik(s, "Teknoloji Altyapısı ve Seçim Gerekçeleri");
  const tk = [
    ["Uygulama", "FastAPI · Next.js · Keycloak", "YZ ekosistemiyle aynı dil; kurumsal tek oturum açma", "Django · Nuxt"],
    ["Veri ve arama", "PostgreSQL + pgvector + Türkçe tam metin", "Tek sistemde ilişkisel, vektör ve metin arama; kurum ayrımı", "Qdrant (ölçek eşiğinde)"],
    ["Belge ve ses", "Docling · Tesseract · faster-whisper large-v3", "MIT lisansı; Türkçe kelime hata oranı ≈ %6–8", "Marker (GPL, yalnız deney)"],
    ["Dil modelleri", "Cosmos T1 / Turkish-Llama (YTÜ) · bge-m3 · turkish-e5", "Yerli, açık ağırlıklı; deneyle seçilir", "Ticari API (yalnız kıyas)"],
    ["Model servis", "vLLM · yurt içi GPU bulutu", "Olgun, sürekli toplu işleme; veri yurt içinde", "SGLang (kıyas kolu)"],
    ["Canlı ders", "BigBlueButton (Faz 1) · LiveKit (Faz 2)", "Eğitim odaklı, kayıt ve beyaz tahta", "Jitsi"],
    ["Kalite ve izleme", "Langfuse · RAGAS + kendi düzeneğimiz · pytest · Playwright · k6", "Kayıt tutma ve regresyon kapısı", "Arize Phoenix"],
  ];
  const tkRows = [[hb("Katman"), hb("Seçim"), hb("Gerekçe"), hb("Alternatif")]];
  tk.forEach((r, i) => {
    const z = i % 2 ? HEX.lt1 : HEX.lt2;
    tkRows.push([
      { text: r[0], options: { bold: true, color: HEX.dk2, fill: { color: z } } },
      { text: r[1], options: { bold: true, color: HEX.accent2, fill: { color: z } } },
      { text: r[2], options: { color: HEX.dk1, fill: { color: z } } },
      { text: r[3], options: { color: HEX.accent5, fill: { color: z } } },
    ]);
  });
  s.addTable(tkRows, { x: 0.6, y: 1.45, w: 12.1, colW: [1.9, 3.9, 4.0, 2.3], fontSize: 13, fontFace: "Calibri", rowH: 0.6, border: { type: "solid", color: "D9E2DF", pt: 0.75 }, valign: "middle" });
  metin(s, "Her seçim ilgili sprintte kurumun kendi Türkçe test setiyle doğrulanarak kesinleşecektir. Ayrıntılı karşılaştırma: teknoloji kararları belgesi (20 karar).", { x: 0.6, y: 6.4, w: 12.1, h: 0.4, fontSize: 12, color: C.accent5 });
  s.addNotes("Seçim ilkeleri: veri egemenliği, ticari kullanıma uygun lisans, Türkçe başarım kanıtı, olgunluk ve küçük ekip tarafından yönetilebilirlik. GPL lisanslı bileşenler kurum içi kurulum paketinde kullanılmaz.");

  // ---------- Doğrulama ----------
  s = yeni("Ar-Ge ve yöntem");
  baslik(s, "Doğrulama Yaklaşımı");
  const ts = [
    ["≥ 500", "soru", "Türkçe soru-cevap test seti; ≥ 150'si kaynak dışı"],
    ["≥ 300", "ödev", "Rubrik ve eğitmen puanlı; ≥ %20'si iki eğitmenden"],
    ["≥ 500", "istem", "Sızıntı ve manipülasyon test seti"],
    ["≥ 5 saat", "ders kaydı", "Elle düzeltilmiş transkript"],
  ];
  ts.forEach(([n, b, t], i) => {
    const y = 1.45 + i * 1.2;
    kart(s, { x: 0.6, y, w: 6.2, h: 1.05 });
    metin(s, n, { x: 0.85, y: y + 0.12, w: 1.9, h: 0.8, fontSize: 28, bold: true, color: C.accent2, fontFace: "Cambria", valign: "middle" });
    metin(s, [{ text: b, options: { bold: true, breakLine: true, color: C.text2 } }, { text: t }], { x: 2.8, y: y + 0.1, w: 3.85, h: 0.85, fontSize: 14, valign: "middle" });
  });
  metin(s, "Yöntem", { x: 7.2, y: 1.45, w: 5.5, h: 0.45, fontSize: 18, bold: true, color: C.text2 });
  metin(s, [
    { text: "Kilitli test seti; metrikler geliştirmeden önce sabitlenir", options: { bullet: true, breakLine: true } },
    { text: "Her sonuç %95 güven aralığıyla raporlanır", options: { bullet: true, breakLine: true } },
    { text: "6 deney, her birinde kontrollü kollar (ablasyon)", options: { bullet: true, breakLine: true } },
    { text: "Model ya da istem değişikliği regresyon kapısından geçmeden canlıya çıkmaz", options: { bullet: true, breakLine: true } },
    { text: "İki aşamalı pilot: kendi kurumumuz + en az bir dış kurum", options: { bullet: true } },
  ], { x: 7.2, y: 2.0, w: 5.5, h: 2.8, fontSize: 15, paraSpaceAfter: 6 });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 7.2, y: 5.0, w: 5.5, h: 1.25, rectRadius: 0.1, fill: { color: "FBE9E5" }, line: { color: PH, width: 1 } });
  metin(s, [
    { text: "Ön kavram kanıtı (n = 60 soru, 20 ödev): ", options: { bold: true, color: PH } },
    { text: "‹Recall@5 = …, sadakat = …, reddetme = …, Kappa = …›. Küçük örneklem; proje kapsamında doğrulanacak.", options: { color: PH } },
  ], { x: 7.45, y: 5.1, w: 5.05, h: 1.05, fontSize: 13, valign: "middle" });
  s.addNotes("Kavram kanıtı yapılmadıysa sağ alttaki kırmızı kutu silinmeli ve formda aşama 'Fikir aşaması' seçilmeli. Sonuç ne çıkarsa çıksın dürüstçe yazılmalı; düşük değer Ar-Ge belirsizliğinin kanıtıdır.");

  // ---------- 10 · İş planı (Gantt) ----------
  pres.addSection({ title: "Plan ve ekip" });
  s = yeni("Plan ve ekip");
  baslik(s, "Uygulama Takvimi (Faz 1: 12 Ay)");
  const aylar = ["Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara", "Oca", "Şub", "Mar"];
  const ip = [
    ["İP-0 Proje yönetimi ve raporlama", 1, 12, HEX.accent5],
    ["İP-1 Gereksinim ve test setleri", 1, 2, HEX.accent6],
    ["İP-2 Platform (test yatağı)", 1, 4, HEX.accent5],
    ["İP-3 Türkçe erişim, çok kipli içerik", 2, 5, HEX.accent2],
    ["İP-4 Soru-cevap ve pedagoji", 4, 7, HEX.accent2],
    ["İP-5 Rubrik değerlendirme", 5, 9, HEX.accent2],
    ["İP-6 Ölçek, KVKK, yurt içi model", 6, 9, HEX.accent2],
    ["İP-7 Pilot (kendi + dış kurum)", 7, 12, HEX.dk2],
    ["İP-8 FMH, ticarileşme, Faz 2", 8, 12, HEX.accent1],
  ];
  const gx = 4.3, gw = 8.4, cw = gw / 12, gy = 1.75, rh = 0.44;
  aylar.forEach((a, i) => metin(s, a, { x: gx + i * cw, y: 1.4, w: cw, h: 0.3, fontSize: 11, color: C.accent5, align: "center" }));
  metin(s, "2027 →", { x: gx, y: 1.15, w: 2, h: 0.25, fontSize: 10, color: C.accent5 });
  metin(s, "2028", { x: gx + 9 * cw, y: 1.15, w: 1, h: 0.25, fontSize: 10, color: C.accent5 });
  ip.forEach(([ad, b, e, renk], i) => {
    const y = gy + i * rh;
    if (i % 2 === 0) s.addShape(pres.shapes.RECTANGLE, { x: 0.6, y, w: 12.1, h: rh, fill: { color: HEX.lt2 }, line: { color: HEX.lt2 } });
    metin(s, ad, { x: 0.7, y, w: 3.5, h: rh, fontSize: 13, valign: "middle", color: C.text1 });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: gx + (b - 1) * cw + 0.04, y: y + 0.1, w: (e - b + 1) * cw - 0.08, h: rh - 0.2, rectRadius: 0.08, fill: { color: renk }, line: { color: renk } });
  });
  const kt = [[2, "KT-1"], [4, "KT-2"], [5, "KT-3"], [7, "KT-4"], [9, "KT-5"], [10, "KT-6"], [12, "KT-7"]];
  const ky = gy + ip.length * rh + 0.1;
  kt.forEach(([ay, ad]) => {
    const x = gx + ay * cw - 0.15;
    s.addShape(pres.shapes.DIAMOND, { x, y: ky, w: 0.3, h: 0.3, fill: { color: ad === "KT-6" ? HEX.accent4 : HEX.accent1 }, line: { color: HEX.lt1 } });
    metin(s, ad, { x: x - 0.25, y: ky + 0.32, w: 0.8, h: 0.25, fontSize: 10, align: "center", color: C.accent5 });
  });
  metin(s, [
    { text: "KT-6 (14.01.2028): Faz 2 başvurusu. ", options: { bold: true, color: C.accent4 } },
    { text: "Ayrıntılı plan: 33 iki haftalık sprint ve 148 görev; her görevde tarih, sorumlu, teknoloji ve kabul kriteri tanımlıdır." },
  ], { x: 0.6, y: 6.5, w: 12.1, h: 0.4, fontSize: 13 });
  s.addNotes("Tahmini başlangıç 01.04.2027 (faaliyet onay yazısına bağlı). Her kilometre taşında devam/dur kriteri var: KT-3 Recall@5 ≥ %85, KT-4 sadakat ≥ %93, KT-5 Kappa ≥ 0,70 ara eşikleri. Ayrıntı: proje dosyası belge 04.");

  // ---------- 11 · Ekip ----------
  s = yeni("Plan ve ekip");
  baslik(s, "Proje Ekibi ve Üniversite-Sanayi İş Birliği");
  const rol = [
    ["FaUserTie", "Proje yöneticisi", "1,0"],
    ["FaBrain", "Kıdemli YZ / dil işleme mühendisi", "1,0"],
    ["FaRobot", "YZ mühendisi", "1,0"],
    ["FaServer", "Backend geliştirici", "2,0"],
    ["FaDesktop", "Frontend geliştirici", "1,0"],
    ["FaGears", "DevOps / güvenlik", "0,5"],
  ];
  for (let i = 0; i < rol.length; i++) {
    const [ic, r, fte] = rol[i];
    const x = 0.6 + (i % 2) * 3.55, y = 1.5 + Math.floor(i / 2) * 1.2;
    kart(s, { x, y, w: 3.35, h: 1.0 });
    await ikonDaire(s, ic, x + 0.18, y + 0.17, 0.66);
    metin(s, [{ text: r, options: { bold: true, breakLine: true, color: C.text2 } }, { text: fte + " tam zamanlı eşdeğer", options: { fontSize: 12, color: C.accent5 } }], { x: x + 1.0, y: y + 0.1, w: 2.25, h: 0.8, fontSize: 14, valign: "middle" });
  }
  metin(s, "7 Ar-Ge personeli · 78 kişi-ay · destek ve kapsam dışı personel: 0", { x: 0.6, y: 5.2, w: 6.9, h: 0.4, fontSize: 14, bold: true, color: C.accent2 });
  metin(s, "Kıdemli YZ mühendisi istihdam edilecek; diğer roller kurum içi yazılım ekibinden karşılanacaktır.", { x: 0.6, y: 5.6, w: 6.9, h: 0.4, fontSize: 13, color: C.accent5 });
  const akd = [
    ["FaMicrochip", "YTÜ Bilgisayar Mühendisliği", "Türkçe büyük dil modelleri ve bilgi erişimi · deney tasarımı", "‹Danışman adı, unvanı›"],
    ["FaChalkboardUser", "YTÜ Eğitim Fakültesi", "Ölçme-değerlendirme · rubrik geçerliliği · pilot etiği", "‹Danışman adı, unvanı›"],
    ["FaUserGraduate", "YTÜ stajyer / tez öğrencisi", "2 kişi · etiketleme, deney koşturma, test", "Yıldız TTO üzerinden"],
  ];
  for (let i = 0; i < akd.length; i++) {
    const [ic, b, t, ad] = akd[i];
    const y = 1.5 + i * 1.6;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 7.85, y, w: 4.85, h: 1.4, rectRadius: 0.12, fill: { color: C.text2 }, line: { color: C.text2 } });
    await ikonDaire(s, ic, 8.05, y + 0.32, 0.75, C.accent1);
    metin(s, [
      { text: b, options: { bold: true, breakLine: true, color: C.background1 } },
      { text: t, options: { breakLine: true, color: C.accent3, fontSize: 13 } },
      { text: ad, options: { color: ad.startsWith("‹") ? "F6B7A9" : C.accent1, fontSize: 13, bold: true } },
    ], { x: 9.0, y: y + 0.1, w: 3.6, h: 1.2, fontSize: 15, valign: "middle" });
  }
  s.addNotes("Hedef akademik ortaklık: YTÜ Bilgisayar Mühendisliği'nin Türkçe dil modeli çalışmaları (COSMOS grubu) ve Eğitim Fakültesi. Görüşmeler Yıldız TTO üzerinden yürütülüyor; niyet mektubu alındığında isimler eklenmeli.");

  // ---------- 12 · Pazar ve ticarileşme ----------
  pres.addSection({ title: "Ticarileşme" });
  s = yeni("Ticarileşme");
  baslik(s, "Pazar ve Ticarileşme");
  const pz = [["TAM", "≈ 2,2–2,45 milyar $", "Türkiye eğitim teknolojileri pazarı (2024–25)"], ["SAM", "≈ 180–250 milyon $", "Platform + YZ değerlendirme; kurs, okul, SEM, kurumsal akademi, bireysel eğitmen"], ["SOM", "≈ 1–2 milyon $", "3. yılda SAM'ın ≈ %0,5–1'i"]];
  pz.forEach(([k, v, t], i) => {
    const y = 1.45 + i * 1.3;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y, w: 4.2, h: 1.15, rectRadius: 0.1, fill: { color: [HEX.lt2, "DCEBE7", "C5DED8"][i] }, line: { color: HEX.lt1 } });
    metin(s, [{ text: k + "  ", options: { bold: true, color: C.accent2 } }, { text: v, options: { bold: true, color: C.text2, breakLine: true } }, { text: t, options: { fontSize: 12 } }], { x: 0.8, y: y + 0.08, w: 3.85, h: 1.0, fontSize: 16, valign: "middle" });
  });
  metin(s, "Kaynak: IMARC (Ekonomist), Ken Research. SAM ve SOM tahmindir.", { x: 0.6, y: 5.4, w: 4.2, h: 0.4, fontSize: 11, color: C.accent5 });
  const fiyat = [[hb("Paket"), hb("Fiyat (KDV hariç)")],
    ["Kurum Asistan", "60 TL / öğrenci / ay"], ["Kurum Tam (+ değerlendirme)", "85 TL / öğrenci / ay"],
    ["Eğitmen Başlangıç / Pro", "499 / 999 TL / ay"], ["Kurum içi kurulum lisansı", "1,5–3 M TL / yıl + bakım"], ["API", "1.000 sorgu başına"]];
  s.addTable(fiyat.map((r, i) => i === 0 ? r : r.map((v) => ({ text: v, options: { fill: { color: i % 2 ? HEX.lt2 : HEX.lt1 }, color: HEX.dk1 } }))), { x: 5.05, y: 1.45, w: 3.9, colW: [2.05, 1.85], fontSize: 13, fontFace: "Calibri", rowH: 0.55, border: { type: "solid", color: "D9E2DF", pt: 0.75 }, valign: "middle" });
  metin(s, "Hedef brüt kâr marjı ≥ %70", { x: 5.05, y: 5.0, w: 3.9, h: 0.4, fontSize: 14, bold: true, color: C.accent2 });
  s.addChart(pres.charts.BAR, [{ name: "Gelir (milyon TL)", labels: ["2028", "2029", "2030"], values: [3.2, 17.1, 54.4] }], {
    x: 9.2, y: 1.35, w: 3.5, h: 4.4, barDir: "col", chartColors: [HEX.accent2], showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: "0.0", dataLabelFontSize: 12, dataLabelFontFace: "+mn-lt", dataLabelColor: HEX.dk2,
    showTitle: true, title: "Temkinli gelir projeksiyonu (M TL)", titleFontSize: 13, titleFontFace: "+mn-lt", titleColor: HEX.dk2,
    catAxisLabelColor: HEX.accent5, catAxisLabelFontSize: 12, catAxisLabelFontFace: "+mn-lt", valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" }, showLegend: false, barGapWidthPct: 60,
  });
  metin(s, "Yaygınlaştırma sırası: kurumumuzun kendi eğitimleri → sektördeki kurslar ve okullar → Yıldız ekosistemi ve YTÜ SEM → bireysel eğitmenler → API ortakları", { x: 0.6, y: 6.1, w: 12.1, h: 0.6, fontSize: 13, color: C.text1 });
  s.addNotes("Varsayımlar: 2028'de 10 kurum × 150 öğrenci + 300 bireysel eğitmen; 2029'da 40 kurum + 1.200 eğitmen; 2030'da 120 kurum + 3.000 eğitmen + lisans ve ihracat. 2027 sabit fiyatları. Pilot sonrası güncellenecek.");

  // ---------- 13 · İthal ikame, ihracat, uyum ----------
  s = yeni("Ticarileşme");
  baslik(s, "İthal İkame, İhracat ve Mevzuata Uyum");
  metin(s, "İkame edilen döviz bazlı ürünler", { x: 0.6, y: 1.45, w: 4.0, h: 0.45, fontSize: 18, bold: true, color: C.text2 });
  const ikame = [["Zoom / Teams / Meet", "Yurt içi canlı ders"], ["Yabancı LMS abonelikleri", "Yerli platform"], ["ChatGPT / Gemini kurumsal + API", "Yurt içi açık model"], ["Yabancı değerlendirme araçları", "Rubrik tabanlı değerlendirme"]];
  ikame.forEach(([a, b], i) => {
    const y = 2.0 + i * 1.0;
    kart(s, { x: 0.6, y, w: 4.0, h: 0.85 });
    metin(s, [{ text: a, options: { color: C.accent4, breakLine: true } }, { text: "→ " + b, options: { bold: true, color: C.accent2 } }], { x: 0.8, y: y + 0.05, w: 3.7, h: 0.75, fontSize: 14, valign: "middle" });
  });
  metin(s, "İhracat yol haritası", { x: 5.0, y: 1.45, w: 4.0, h: 0.45, fontSize: 18, bold: true, color: C.text2 });
  const ihr = [["2028", "Azerbaycan · KKTC", "Dil ve kültür yakınlığı"], ["2028–29", "Kazakistan · Özbekistan", "Türk dilli, dijitalleşen pazarlar"], ["2029+", "Almanya / AB", "AB YZ Yasası uyumu giriş avantajı"]];
  s.addShape(pres.shapes.LINE, { x: 5.35, y: 2.2, w: 0, h: 3.2, line: { color: HEX.accent3, width: 2 } });
  for (let i = 0; i < ihr.length; i++) {
    const [y0, p, t] = ihr[i];
    const y = 2.05 + i * 1.25;
    await ikonDaire(s, "FaEarthEurope", 5.05, y, 0.6, i === 2 ? C.accent1 : C.accent2);
    metin(s, [{ text: y0 + "  ", options: { bold: true, color: C.accent2 } }, { text: p, options: { bold: true, color: C.text2, breakLine: true } }, { text: t, options: { fontSize: 13 } }], { x: 5.85, y: y - 0.05, w: 3.2, h: 0.9, fontSize: 15 });
  }
  metin(s, "Uyumluluk tasarımın parçası", { x: 9.4, y: 1.45, w: 3.3, h: 0.45, fontSize: 18, bold: true, color: C.text2 });
  const uy = [["FaShieldHalved", "KVKK", "Yurt içi barındırma, açık rıza, satır düzeyi güvenlik"], ["FaScaleBalanced", "AB YZ Yasası Ek III", "İnsan gözetimi, kayıt tutma, şeffaflık"], ["FaUniversalAccess", "WCAG 2.2 AA", "Erişilebilir arayüz"]];
  for (let i = 0; i < uy.length; i++) {
    const [ic, b, t] = uy[i];
    const y = 2.0 + i * 1.35;
    kart(s, { x: 9.4, y, w: 3.3, h: 1.2 });
    await ikonDaire(s, ic, 9.55, y + 0.25, 0.65, C.text2);
    metin(s, [{ text: b, options: { bold: true, breakLine: true, color: C.text2 } }, { text: t, options: { fontSize: 12 } }], { x: 10.3, y: y + 0.08, w: 2.3, h: 1.05, fontSize: 14, valign: "middle" });
  }
  s.addNotes("AB YZ Yasası Ek III(3)(b): öğrenme çıktısını değerlendiren YZ yüksek riskli; yükümlülükler 02.12.2027 (Digital Omnibus ile ertelendi, teyit edilmeli). Not kararı eğitmende olduğu için tasarım uyumlu.");

  // ---------- 14 · Bütçe ----------
  s = yeni("Ticarileşme");
  baslik(s, "Bütçe ve Finansman (Faz 1)");
  s.addChart(pres.charts.DOUGHNUT, [{ name: "Bütçe", labels: ["Personel (teşvik sonrası)", "Altyapı (GPU, bulut, API)", "Hizmet, FMH, pilot, diğer", "Beklenmeyen (%7)", "Akademik danışmanlık", "Kira ve işletme"], values: [10.4, 2.26, 2.0, 1.15, 0.96, 0.84] }], {
    x: 0.6, y: 1.35, w: 7.2, h: 5.2, holeSize: 55, chartColors: [HEX.dk2, HEX.accent2, HEX.accent3, HEX.accent5, HEX.accent1, HEX.accent6],
    showPercent: true, showValue: false, dataLabelColor: HEX.lt1, dataLabelFontSize: 12, dataLabelFontFace: "+mn-lt",
    showLegend: true, legendPos: "r", legendFontSize: 13, legendFontFace: "+mn-lt", legendColor: HEX.dk1, showTitle: false,
  });
  kart(s, { x: 8.2, y: 1.45, w: 4.5, h: 1.75 });
  metin(s, [{ text: "≈ 17,6 M TL", options: { fontSize: 40, bold: true, color: C.accent2, fontFace: "Cambria", breakLine: true } }, { text: "teşvik sonrası toplam (teşvik öncesi ≈ 21,2 M TL)", options: { fontSize: 14 } }], { x: 8.45, y: 1.55, w: 4.1, h: 1.55, valign: "middle" });
  metin(s, [
    { text: "Yıllık gelirin ≈ %7–9'u: proje öz kaynakla finanse edilebilir", options: { bullet: true, breakLine: true } },
    { text: "78 kişi-ay Ar-Ge personeli; teşviklerle personel maliyetinde ≈ %20–28 azalma (tahmini)", options: { bullet: true, breakLine: true } },
    { text: "Ek kaynak: TÜBİTAK 1507 / 1501 başvurusu planlanıyor", options: { bullet: true, breakLine: true } },
    { text: "GPU satın alma seçeneğinde 4691 makine-teçhizat KDV istisnası", options: { bullet: true } },
  ], { x: 8.2, y: 3.45, w: 4.5, h: 2.9, fontSize: 15, paraSpaceAfter: 8 });
  s.addNotes("Tüm tutarlar 2027 fiyatlarıyla tahmindir; İK ve mali müşavirle güncellenmeli. Kalem ayrıntısı: proje dosyası belge 04 §4. Kira güvence bedeli gider değildir.");

  // ---------- 15 · Kapanış ----------
  pres.addSection({ title: "Kapanış" });
  s = pres.addSlide({ masterName: "KOYU", sectionTitle: "Kapanış" });
  s.addText("Eğitimi güçlendiren yerli, güvenilir ve ölçülebilir yapay zekâ", { placeholder: "title" });
  s.addText("Faz 1: platform + kaynağa dayalı YZ  →  Faz 2: sanal sınıf + YZ asistanı  →  Faz 3: uyarlanabilir öğrenme", { placeholder: "body" });
  const kpi = [["15+", "Ar-Ge personeli (36 ay)"], ["3+", "patent / tescil başvurusu"], ["2+", "destekli proje"], ["6+", "YTÜ stajyer ve tez öğrencisi"]];
  kpi.forEach(([n, t], i) => {
    const x = 0.8 + i * 3.0;
    metin(s, n, { x, y: 5.45, w: 2.7, h: 0.75, fontSize: 36, bold: true, color: C.accent1, fontFace: "Cambria" });
    metin(s, t, { x, y: 6.2, w: 2.7, h: 0.6, fontSize: 14, color: C.background1 });
  });
  s.addNotes("Kapanış: teknoparka katkı göstergeleri (Bakanlık TGB performans endeksinde sayılan metrikler) ve faz zinciri. Teşekkür ve sorular.");

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("yazıldı:", OUT);
})().catch((e) => { console.error(e); process.exit(1); });
