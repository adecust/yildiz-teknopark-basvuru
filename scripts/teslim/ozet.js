// YTÜ Yıldız Teknopark başvurusu için "Proje Özeti" Word belgesini üretir.
// Kullanım: node scripts/teslim/ozet.js  ->  teslim/KAYNAK-YZ_Proje_Ozeti.docx
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, HeadingLevel, Header, Footer, PageNumber, BorderStyle, LevelFormat, PageBreak, VerticalAlign,
} = require("docx");

const OUT = path.resolve(__dirname, "..", "..", "teslim", "KAYNAK-YZ_Proje_Ozeti.docx");
const TEAL = "0B3D3A", TEAL2 = "14786E", ZEBRA = "EEF4F2", HEDEF = "FDF1DE", PH = "C8553D", GRI = "5B6770", AMBER = "F2A541";
const W = 9638; // A4, 2 cm kenar boşluğu

// ‹…› ile işaretli alanlar kurum tarafından doldurulacaktır: kırmızı ve sarı vurgulu
function runs(text, o = {}) {
  return String(text).split(/(‹[^›]*›)/).filter(Boolean).map((t) =>
    t.startsWith("‹")
      ? new TextRun({ text: t, bold: true, color: PH, highlight: "yellow", size: o.size })
      : new TextRun({ text: t, bold: o.bold, italics: o.italics, color: o.color, size: o.size, font: o.font }));
}
const P = (t, o = {}) => new Paragraph({ children: Array.isArray(t) ? t : runs(t, o), alignment: o.align ?? AlignmentType.JUSTIFIED, spacing: { after: o.after ?? 120 } });
const H1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)] });
const M = (t, o = {}) => new Paragraph({ numbering: { reference: "madde", level: 0 }, alignment: AlignmentType.JUSTIFIED, children: Array.isArray(t) ? t : runs(t, o), spacing: { after: 60 } });
const B = (bas, t) => M([new TextRun({ text: bas, bold: true, color: TEAL })].concat(runs(t)));
const NOT = (t) => P(t, { italics: true, color: GRI, size: 18, align: AlignmentType.LEFT });
const BOS = () => new Paragraph({ spacing: { after: 80 }, children: [] });

const sinir = { style: BorderStyle.SINGLE, size: 4, color: "D9E2DF" };
const kenar = { top: sinir, bottom: sinir, left: sinir, right: sinir };
const yok = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
function tablo(basliklar, satirlar, oranlar, vurguSutun = -1) {
  const top = oranlar.reduce((a, b) => a + b, 0);
  const gen = oranlar.map((x) => Math.round((W * x) / top));
  gen[gen.length - 1] = W - gen.slice(0, -1).reduce((a, b) => a + b, 0);
  const hucre = (t, i, baslik, zemin) => new TableCell({
    width: { size: gen[i], type: WidthType.DXA }, borders: kenar, verticalAlign: VerticalAlign.CENTER,
    shading: { type: ShadingType.CLEAR, color: "auto", fill: baslik ? TEAL : zemin },
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [new Paragraph({ spacing: { after: 0 }, children: baslik ? [new TextRun({ text: t, bold: true, color: "FFFFFF", size: 19 })] : runs(t, { size: 19, bold: i === 0 }) })],
  });
  return new Table({
    width: { size: W, type: WidthType.DXA }, columnWidths: gen,
    rows: [new TableRow({ tableHeader: true, children: basliklar.map((t, i) => hucre(t, i, true)) })].concat(
      satirlar.map((s, r) => new TableRow({ cantSplit: true, children: s.map((t, i) => hucre(t, i, false, i === vurguSutun ? HEDEF : r % 2 ? "FFFFFF" : ZEBRA)) }))),
  });
}
function kapakBlok() {
  const satir = (t, o) => new Paragraph({ spacing: { after: o.after ?? 120 }, children: [new TextRun(Object.assign({ text: t, color: "FFFFFF" }, o))] });
  return new Table({
    width: { size: W, type: WidthType.DXA }, columnWidths: [W],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: W, type: WidthType.DXA }, borders: { top: yok, bottom: yok, left: yok, right: yok },
      shading: { type: ShadingType.CLEAR, color: "auto", fill: TEAL }, margins: { top: 600, bottom: 600, left: 500, right: 500 },
      children: [
        satir("YTÜ YILDIZ TEKNOPARK · ADAY FİRMA BAŞVURUSU", { bold: true, size: 20, color: AMBER, after: 360 }),
        satir("PROJE ÖZETİ", { bold: true, size: 60, font: "Cambria", after: 240 }),
        satir("Türkçe Eğitim İçeriği İçin Kaynağa Dayalı Üretken Yapay Zekâ ile Soru-Cevap ve Rubrik Tabanlı Otomatik Ödev Değerlendirme Platformu", { size: 30, font: "Cambria", after: 240 }),
        satir("KAYNAK-YZ", { bold: true, size: 24, color: "8FC1B5", after: 0 }),
      ],
    })] })],
  });
}

const govde = [];
const ekle = (...x) => govde.push(...x);

// ---------------- Kapak ----------------
ekle(
  new Paragraph({ spacing: { before: 600, after: 0 }, children: [] }),
  kapakBlok(),
  new Paragraph({ spacing: { after: 360 }, children: [] }),
  tablo(["Alan", "Bilgi"], [
    ["Başvuran kurum", "‹Kurum Unvanı›"],
    ["Kurumun faaliyet alanı", "Eğitim hizmetleri (‹eğitim alanları›)"],
    ["Vergi dairesi / numarası", "‹Vergi dairesi› / ‹Vergi numarası›"],
    ["Başvuru sahibi", "‹Ad Soyad›, ‹Görevi›"],
    ["İletişim", "‹E-posta› · ‹Telefon›"],
    ["Proje türü", "Ar-Ge ve yazılım"],
    ["Proje süresi", "12 ay (tahmini başlangıç 01.04.2027)"],
    ["Belge tarihi", "Aralık 2026"],
  ], [3, 7]),
  BOS(),
  NOT("Bu belge proje önerisinin özetidir. Ayrıntılı teknik tasarım, deney protokolleri ve sprint düzeyinde iş planı talep hâlinde proje dosyası olarak sunulacaktır. Belgedeki başarım değerleri projenin hedefleridir; literatür değerleri kaynakçada belirtilmiştir."),
  new Paragraph({ children: [new PageBreak()] }),
);

// ---------------- 1. Kurum ve amaç ----------------
ekle(H1("1. Başvuran Kurum ve Projenin Amacı"),
  P("‹Kurum Unvanı›, ‹kuruluş yılı› yılından bu yana ‹eğitim alanları› alanlarında bireylere eğitim hizmeti sunan bir eğitim kurumudur. Kurumun asıl faaliyet alanı eğitimdir; aylık 200–300 aktif öğrenciye hizmet verilmekte ve yıllık gelir yaklaşık 240 milyon TL düzeyindedir."),
  P("Bu proje, kurumun eğitim hizmetini güçlendirmek amacıyla geliştirilmektedir. Yapay zekâ, eğitmenin yerini almak için değil; eğitmenin öğrenciye ayırdığı zamanı artırmak, öğrenciye ders dışında güvenilir destek sağlamak ve ödev geri bildirimini hızlandırmak için tasarlanmaktadır. Geliştirilecek sistemin ilk kullanıcısı kurumun kendisi olacak; gerçek ortamda doğrulandıktan sonra aynı ihtiyacı yaşayan kurslara, okullara ve kurumsal akademilere sunulacaktır."),
  P("Teknopark şubesinde yalnızca Ar-Ge ve yazılım geliştirme faaliyeti yürütülecek; eğitim hizmeti kurum merkezinde sürdürülecektir."));

// ---------------- 2. Künye ----------------
ekle(H1("2. Proje Künyesi"), tablo(["Alan", "Değer"], [
  ["Proje adı", "Türkçe Eğitim İçeriği İçin Kaynağa Dayalı Üretken Yapay Zekâ ile Soru-Cevap ve Rubrik Tabanlı Otomatik Ödev Değerlendirme Platformu"],
  ["Kısa ad", "KAYNAK-YZ (çalışma adı)"],
  ["Faaliyet alanı", "Yapay Zekâ · Yazılım Geliştirme · SaaS / Bulut · EdTech · Veri / Analitik"],
  ["Ar-Ge kategorileri", "Yenilik unsuru içeren yazılım geliştirme · kavram geliştirme · teknik yapılabilirlik etüdü · prototip geliştirme · patent çalışmaları"],
  ["Anahtar kelimeler", "Kaynağa dayalı üretim (RAG) · Türkçe doğal dil işleme · büyük dil modelleri · otomatik ödev değerlendirme · halüsinasyon tespiti · öğrenme yönetim sistemi · bilgi erişimi"],
  ["Teknoloji hazırlık seviyesi", "Başlangıç TRL 2–3; hedef TRL 6–7 (gerçek kullanıcılarla pilot)"],
  ["Teknoparkta Ar-Ge personeli", "7 kişi (6,5 tam zamanlı eşdeğer; 78 kişi-ay)"],
  ["Akademik iş birliği", "YTÜ Bilgisayar Mühendisliği (Türkçe dil modelleri) · YTÜ Eğitim Fakültesi (ölçme-değerlendirme) · 2 YTÜ stajyer"],
  ["Tahmini bütçe", "≈ 17,6 milyon TL (teşvik sonrası; teşvik öncesi ≈ 21,2 milyon TL); öz kaynak"],
  ["Faz zinciri", "Faz 1 (bu proje) · Faz 2: avatarlı sanal sınıf ve sınıf içi YZ asistanı · Faz 3: uyarlanabilir öğrenme"],
], [3, 7]));

// ---------------- 3. Özet ----------------
ekle(H1("3. Proje Özeti"),
  P("Projenin amacı, eğitmenin yüklediği ders kaynaklarına (ders notu, PDF, slayt, ders kaydı) bağlı kalan ve Türkçe için optimize edilmiş bir eğitim yapay zekâsı ile bu yapay zekânın çalıştığı bir eğitim platformu geliştirmektir. Genel amaçlı sohbet araçları ders kaynağına bağlı kalmadığı için hatalı bilgi üretebilmekte, ödev yanıtını doğrudan vererek öğrenmeyi zayıflatabilmekte ve öğrenci verisini yurt dışında işlemektedir."),
  P("Geliştirilecek sistem, öğrencinin sorusunu yalnızca ilgili dersin kaynaklarından ve sayfa ya da dakika atfı vererek yanıtlayacak; kaynakta bulunmayan sorularda yanıt üretmek yerine bu durumu açıkça belirtecek; ödev sorularında yanıt yerine kademeli ipuçlarıyla öğrenciyi yönlendirecek ve eğitmenin rubriğine göre ödevleri ön-değerlendirerek kanıtlı ve gerekçeli geri bildirim üretecektir. Nihai not kararı her zaman eğitmende kalacaktır."),
  P("Sistem, kurumun kendi öğrencileri ve eğitmenleriyle gerçek ortamda pilot edilecek, ardından en az bir dış kurumda doğrulanacaktır."));

// ---------------- 4. Sorun ----------------
ekle(H1("4. Sorun ve İhtiyaç"),
  B("Öğrenci: ", "Ders sonrasında ortaya çıkan sorular yanıtsız kalmakta; genel amaçlı araçlar dersle uyumsuz ya da hatalı yanıtlar verebilmektedir."),
  B("Eğitmen: ", "Tekrar eden soruların yanıtlanması ve ödev değerlendirmesi önemli zaman almaktadır (kurum içi anket: haftada ‹X› saat); geri bildirim gecikmektedir."),
  B("Kurum: ", "Çoğu döviz bazlı 3–5 ayrı araç kullanılmakta; öğrenme kalitesi ölçülememekte ve yurt dışı veri aktarımı KVKK yükümlülüğü doğurmaktadır."),
  P("Genel amaçlı yapay zekâ araçlarının temel sınırlılıkları şunlardır:", { bold: true, after: 60 }),
  M("Kaynağa bağlılık yoktur. Kaynağa dayalı ticari ürünlerde dahi reddetme davranışı %0,2 ile %11,1 arasında değişmekte ve en büyük kalite farkını oluşturmaktadır [1]."),
  M("Öğrenmeyi zayıflatabilir. Türkiye'de yaklaşık 1.000 lise öğrencisiyle yapılan randomize kontrollü saha deneyinde, korumasız sohbet botu kullanan öğrenciler yapay zekâ kaldırıldıktan sonraki sınavda kontrol grubuna göre %17 daha düşük puan almış; öğrenmeyi koruyacak şekilde tasarlanmış sürüm bu kaybı büyük ölçüde önlemiştir [2]."),
  M("Veri yurt dışında işlenir. KVKK md. 9 (7499 sayılı Kanun ile değişik) kapsamında standart sözleşme ve Kurul'a bildirim yükümlülüğü doğar [3]."),
  M("Ödev puanlamasında güvenilir değildir. Hazır büyük dil modellerinin insan puanıyla uyumu ağırlıklı Kappa ile yaklaşık 0,4–0,7 aralığındadır ve veri setine göre büyük ölçüde değişmektedir [4][5]."));

// ---------------- 5. Çözüm ----------------
ekle(H1("5. Önerilen Çözüm"),
  B("Kaynağa bağlı soru-cevap: ", "Yalnızca dersin yayımlanmış kaynaklarından, sayfa, slayt ya da ders kaydı dakikası atfıyla yanıt; kaynakta bulunmayan sorularda gerekçeli ret ve eğitmene bildirim."),
  B("Pedagojik mod: ", "Ödev sorularında yanıt yerine kademeli ipucu (kavram hatırlatma, yönlendirici soru, ilk adım, benzer örnek); yanıt sızıntısı tarayıcısı; eğitmen tarafından seçilen serbest, Sokratik ve kapalı modlar."),
  B("Rubrik tabanlı ön-değerlendirme: ", "Kriter başına kanıt çıkarımı, eğitmen puanlı örneklerle karşılaştırma, belirsizlik ölçümü; belirsiz kriterlerin eğitmene yönlendirilmesi; ders kaynağına atıflı geri bildirim; notun eğitmen onayıyla kesinleşmesi."),
  B("Platform (test yatağı): ", "Kayıt ve roller, ders alanları, canlı ders, ödev teslimi, takvim, bireysel ve kurumsal abonelik. Hazır bileşenlerle kurulacak ve toplam eforun %24'ü ile sınırlı tutulacaktır."));

// ---------------- 6. Yenilik ----------------
ekle(H1("6. Yenilikçi Yön ve Tekniğin Bilinen Durumu"),
  P("Kaynağa dayalı eğitim yapay zekâsı kategorisi oluşmaya başlamıştır (örneğin 2026'da Google Classroom'a eklenen NotebookLM ve Gemini özellikleri [6]). Ancak mevcut çözümler sadakat, reddetme, sızıntı ve puan uyumunu ölçülmüş olarak sunmamakta; yerli çözümler ise üretken yapay zekâyı kaynağa bağlı ve ölçülebilir biçimde kullanmamaktadır."),
  tablo(["Özellik", "Google Classroom + NotebookLM", "Moodle / Canvas + eklenti", "Yerli LMS'ler", "KAYNAK-YZ (hedef)"], [
    ["Ders kaynağına bağlı soru-cevap", "Var", "Kısmen", "Kısmen", "Var"],
    ["Sayfa / slayt / ders kaydı dakikası atfı", "Kısmen", "Yok", "Yok", "Var"],
    ["Ölçülmüş reddetme (kaynak dışı soru)", "Bilgi yok", "Yok", "Yok", "Var (≥ %90)"],
    ["Ödev yanıtı sızıntı denetimi", "Kısmen", "Yok", "Yok", "Var (≤ %2)"],
    ["Ölçülmüş rubrik puan uyumu", "Kısmen", "Kısmen", "Yok", "Var (Kappa ≥ 0,75)"],
    ["Yurt içi / kurum içi kurulum", "Yok", "Var", "Var", "Var"],
    ["Kurs işletme işlevleri (kayıt, ödeme)", "Yok", "Kısmen", "Var", "Var"],
  ], [3.2, 1.8, 1.7, 1.4, 1.9], 4),
  NOT("Rakip bilgileri kamuya açık kaynaklardan ve firma beyanlarından derlenmiştir."));

// ---------------- 7. Ar-Ge ----------------
ekle(H1("7. Ar-Ge İçeriği ve Ölçülebilir Hedefler"),
  P("Projenin Ar-Ge çekirdeği aşağıdaki teknik belirsizliklere dayanmaktadır. Hedeflere ulaşılabilirlik önceden bilinmemektedir; her biri için hipotez, deney tasarımı ve B planı tanımlanmıştır."),
  tablo(["#", "Araştırma sorusu", "Bugünkü durum (literatür)", "Hedef", "B planı"], [
    ["AR-1", "Türkçe içerikte kaynağa sadakat ve doğru reddetme", "Ticari ürünlerde reddetme %0,2–11,1 [1]", "Sadakat ≥ %95 · ret ≥ %90 · atıf doğruluğu ≥ %95", "Kurum bazlı eşik; kısmi yanıt şablonu"],
    ["AR-2", "Sondan eklemeli Türkçe için hibrit bilgi erişimi", "Türkçe gömme model sıralaması çalışmaya göre değişmektedir [7][8]", "Recall@5 ≥ %90 · MRR@10 ≥ 0,75", "Alan uyarlamalı ince ayar"],
    ["AR-3", "Rubrik tabanlı puanlamada eğitmenle uyum", "Ağırlıklı Kappa ≈ 0,4–0,7 [4][5]; rubrik iyileştirmeyle artış raporlanmıştır [9]", "Kappa ≥ 0,75; tutarlılık ≥ 0,90", "Asistan modu: kanıt ve taslak geri bildirim, puan eğitmende"],
    ["AR-4", "Pedagojik yanıt sızıntısının önlenmesi", "Korumasız sohbet botu öğrenmeyi düşürmektedir [2]", "Sızıntı ≤ %2 · aşırı kısıtlama ≤ %5", "Ödev süresince kapalı mod"],
    ["AR-5", "PDF, slayt, görsel ve ders kaydından çok kipli bilgi tabanı", "Whisper Türkçe kelime hata oranı ≈ %6–8 (standart veri setleri) [10]", "Ders kaydı WER ≤ %10 · video atfı ≥ %90", "Ders terim sözlüğüyle düzeltme"],
    ["AR-6", "Yurt içi açık ağırlıklı modelle maliyet ve veri egemenliği", "Ticari ve yurt dışı modellere bağımlılık", "Kalite farkı ≤ %5 · p50 ≤ 3 sn", "Anonimleştirilmiş hibrit model"],
  ], [0.7, 2.2, 2.6, 2.2, 1.9], 3));

// ---------------- 8. Yöntem ve teknoloji ----------------
ekle(H1("8. Yöntem ve Teknoloji Altyapısı"),
  B("Soru-cevap hattı: ", "Niyet ve pedagojik politika, Türkçe normalizasyon, hibrit erişim (yoğun ve kök bulmalı seyrek) ile yeniden sıralama, ceza-duyarlı cevaplanabilirlik kapısı, atıflı kısıtlı üretim ve iddia düzeyinde doğrulama."),
  B("Değerlendirme hattı: ", "İstem enjeksiyonu taraması, kriter başına kanıt çıkarımı, örneklerle karşılaştırmalı seviye tahmini, çoklu örnekleme ve belirsizlik ölçümü, ders bazında kalibrasyon, geri bildirim ve eğitmen onayı."),
  B("Doğrulama: ", "Geliştirmeden önce sabitlenen test setleri: en az 500 soru (en az 150'si kaynak dışı), en az 300 ödev (en az %20'si iki eğitmenden), en az 500 sızıntı istemi ve en az 5 saat ders kaydı. Sonuçlar %95 güven aralığıyla raporlanacak; model ve istem değişiklikleri otomatik regresyon kapısından geçecektir."),
  BOS(),
  tablo(["Katman", "Seçim", "Gerekçe"], [
    ["Uygulama", "FastAPI · Next.js · Keycloak", "Yapay zekâ ekosistemiyle aynı dil; kurumsal tek oturum açma"],
    ["Veri ve arama", "PostgreSQL · pgvector · Türkçe tam metin arama", "İlişkisel, vektör ve metin arama tek sistemde; satır düzeyi güvenlikle kurum ayrımı"],
    ["Belge ve ses işleme", "Docling · Tesseract · faster-whisper (large-v3)", "Ticari kullanıma uygun lisans; Türkçe başarım kanıtı"],
    ["Dil modelleri", "YTÜ COSMOS Türkçe modelleri (Cosmos T1, Turkish-Llama) · bge-m3 · turkish-e5-large [11]", "Yerli ve açık ağırlıklı; seçim kurumun Türkçe test setinde deneyle yapılacaktır"],
    ["Model servis ve altyapı", "vLLM · yurt içi GPU bulutu · Kubernetes", "Veri yurt içinde; ölçeklenebilir servis"],
    ["Canlı ders", "BigBlueButton (Faz 1) · LiveKit (Faz 2)", "Eğitim odaklı; kayıt ve beyaz tahta"],
    ["Kalite ve izleme", "Langfuse · RAGAS ve kendi değerlendirme düzeneğimiz · pytest · Playwright · k6", "AB YZ Yasası kayıt tutma gereği; sürekli kalite kapısı"],
  ], [2, 4, 4]),
  NOT("Her teknoloji seçimi alternatifleriyle karşılaştırılmış ve ilgili sprintte deneyle kesinleşecek şekilde planlanmıştır (20 karar)."),
  B("Mevzuata uyum: ", "Veri ve modeller yurt içinde; açık rıza ve 18 yaş altı için veli onayı; öğrenci verisi varsayılan olarak model eğitiminde kullanılmaz. Öğrenme çıktısını değerlendiren yapay zekâ AB YZ Yasası'nda yüksek riskli kabul edildiğinden [12] insan gözetimi, kayıt tutma ve şeffaflık tasarımın parçasıdır."));

// ---------------- 9. Kavram kanıtı ----------------
ekle(H1("9. Kavram Kanıtı: İlk Ölçümler (Kasım 2026)"),
  P("Başvuru öncesinde Ar-Ge çekirdeği, tamamen yerel ve açık modellerle çalışan bir prototiple iki gerçek ders içeriğinde (gerontoloji ve matematik; 100 kaynak parçası) ölçülmüştür. Kullanılan modeller: Cosmos T1 ve turkish-e5-large (YTÜ COSMOS), bge-m3, bge-reranker-v2-m3 ve çok dilli bir NLI modeli."),
  tablo(["Ölçüm", "Sonuç", "Proje hedefi"], [
    ["Doğru kaynağın ilk 5 sonuçta bulunması (Recall@5, 83 soru)", "%100 (Recall@1 %78)", "≥ %90"],
    ["Türkçe kök bulmanın katkısı (BM25)", "%88 → %94", "—"],
    ["Hibrit arama ve yeniden sıralamanın katkısı", "+4,8 puan (GA +1,2 … +9,6)", "≥ +8 puan"],
    ["Kaynak dışı soruyu doğru reddetme (47 soru, uçtan uca)", "Kapı olmadan %74 → kapıyla %98", "≥ %90"],
    ["Uydurma cevap sayısı (47 kaynak dışı soru)", "12 → 1", "—"],
    ["Cevaplanan sorularda doğruluk", "%97 (35/36)", "—"],
    ["Ödev cevabı sızıntısı (40 saldırı istemi)", "Tarayıcı olmadan %67,5 → tarayıcıyla %2,5", "≤ %2"],
  ], [5, 3, 2], 1),
  P("Deneyler aynı zamanda hazır bileşenlerle çözülemeyen teknik belirsizlikleri somut olarak göstermiştir: konusu eşleşip ayrıntısı eşleşmeyen sorular (örneğin kaynakta olmayan bir yılın verisi) alaka kapısını geçebilmekte; hazır çok dilli doğal dil çıkarımı modeli Türkçe sayısal cümlelerde ve matematik içeriğinde güvenilir iddia doğrulaması yapamamaktadır. Bu bulgular projenin AR-1 ve AR-4 kapsamındaki araştırma sorularını doğrudan desteklemektedir."),
  NOT("Küçük örneklemli bir kavram kanıtıdır; sorular proje ekibince yazılmıştır ve gerçek öğrenci sorularının yerini tutmaz. Gecikme dizüstü bilgisayarda ölçülmüştür. Ayrıntılı rapor ve kod talep hâlinde sunulacaktır."));

// ---------------- 10. İş planı ----------------
ekle(H1("10. İş Planı"),
  P("Proje üç düzeyde planlanmıştır: fazlar, iş paketleri (epikler) ve iki haftalık sprintlere yerleştirilmiş görevler. Faz 1, iki haftalık 26 sprintte 46 kullanıcı hikâyesi, 19 Ar-Ge araştırması ve 20 görev olarak ayrıntılandırılmıştır; her öğede fonksiyonel gereksinimler, kabul kriterleri, sorumlu, öncelik ve kullanılacak teknolojiler tanımlıdır."),
  tablo(["İP", "İş paketi", "Ay", "Kişi-ay", "Ana çıktı"], [
    ["İP-0", "Proje yönetimi ve teknopark raporlaması", "1–12", "4,0", "Aylık muafiyet ve izleme raporları"],
    ["İP-1", "Gereksinim, literatür, Türkçe test setleri", "1–2", "4,5", "Test setleri ve değerlendirme protokolü"],
    ["İP-2", "Platform çekirdeği (test yatağı)", "1–4", "18,5", "Çok kiracılı platform"],
    ["İP-3", "İçerik işleme ve Türkçe bilgi erişimi", "2–5", "7,5", "İçerik ve konuşma tanıma hattı; erişim deney raporu"],
    ["İP-4", "Kaynağa dayalı soru-cevap ve pedagojik sınırlar", "4–7", "9,0", "Soru-cevap ve politika motoru; deney raporu"],
    ["İP-5", "Rubrik tabanlı ödev değerlendirme", "5–9", "11,5", "Değerlendirme ve kalibrasyon modülü; deney raporu"],
    ["İP-6", "Ölçeklenebilirlik, KVKK, yurt içi model", "6–9", "8,5", "Yurt içi model servisi; maliyet ve yük raporu"],
    ["İP-7", "Pilot (kendi kurumumuz ve dış kurum)", "7–12", "10,5", "Pilot raporları"],
    ["İP-8", "Fikri mülkiyet, ticarileşme, Faz 2 başvurusu", "8–12", "4,0", "Tescil/patent başvurusu; satış paketi; Faz 2 dosyası"],
    ["", "Toplam", "12 ay", "78,0", "Platform payı %24"],
  ], [0.8, 3.4, 0.8, 0.9, 3.6]),
  BOS(),
  tablo(["Kilometre taşı", "Tarih", "Devam kriteri"], [
    ["KT-1 Test setleri hazır", "31.05.2027", "En az 500 soru ve 300 ödev; etiketleyici uyumu raporlandı"],
    ["KT-2 Platform", "30.07.2027", "Kritik akışlar ve iç testler tamamlandı"],
    ["KT-3 Bilgi erişimi", "31.08.2027", "Recall@5 ≥ %85 (ara eşik)"],
    ["KT-4 Soru-cevap ve pedagoji", "29.10.2027", "Sadakat ≥ %93, sızıntı ≤ %3 (ara eşik)"],
    ["KT-5 Değerlendirme ve ölçek", "24.12.2027", "Kappa ≥ 0,70 (ara eşik), p95 ≤ 6 sn"],
    ["KT-6 Faz 2 başvurusu", "14.01.2028", "Bitişten en az 60 gün önce teslim"],
    ["KT-7 Faz 1 kapanışı", "31.03.2028", "Kabul kriterleri ve proje sonuç raporu"],
  ], [3, 1.6, 5.4]));

// ---------------- 10. Ekip ----------------
ekle(H1("11. Proje Ekibi ve Üniversite-Sanayi İş Birliği"),
  tablo(["Rol", "Kişi / TZE", "Sorumluluk"], [
    ["Proje yöneticisi", "1 / 1,0", "Planlama, teknopark raporlaması, pilot, paydaş yönetimi"],
    ["Kıdemli yapay zekâ / dil işleme mühendisi (teknik lider)", "1 / 1,0", "AR-1, AR-2, AR-6; deney tasarımı (istihdam süreci devam etmektedir)"],
    ["Yapay zekâ mühendisi", "1 / 1,0", "AR-3, AR-4, AR-5; değerlendirme düzeneği"],
    ["Arka uç geliştirici", "2 / 2,0", "Platform, servis entegrasyonu, güvenlik"],
    ["Ön yüz geliştirici", "1 / 1,0", "Öğrenci, eğitmen ve kurum arayüzleri; erişilebilirlik"],
    ["Altyapı ve güvenlik", "1 / 0,5", "Altyapı, yük testi, KVKK teknik önlemleri"],
    ["YTÜ akademik danışman, Bilgisayar Mühendisliği", "‹Ad, unvan›", "Türkçe dil modelleri, bilgi erişimi, deney tasarımı denetimi, ortak yayın"],
    ["YTÜ akademik danışman, Eğitim Fakültesi", "‹Ad, unvan›", "Rubrik geçerliliği, ölçme-değerlendirme, pilot tasarımı ve etik"],
    ["YTÜ stajyer / tez öğrencisi", "2 / 2 × 0,5", "Etiketleme, deney yürütme, test"],
  ], [3.6, 1.4, 5]),
  P("Kurumun eğitmenleri, test setlerinin hazırlanması, rubrik tasarımı ve pilot uygulamada alan uzmanı olarak yer alacaktır. Akademik danışmanlık Yıldız TTO aracılığıyla yürütülecek; danışmanlar çeyreklik deney değerlendirmelerine katılacak ve ortak yayın hedeflenmektedir."));

// ---------------- 11. Ticarileşme ----------------
ekle(H1("12. Ticarileşme Planı"),
  P("Yaygınlaştırma sırası şöyledir: önce kurumun kendi eğitimleri, ardından sektördeki kurslar ve okullar, Yıldız ekosistemi ve YTÜ Sürekli Eğitim Merkezi, bireysel eğitmenler ve API ortakları."),
  tablo(["Katman", "Büyüklük", "Dayanak"], [
    ["TAM: Türkiye eğitim teknolojileri pazarı", "≈ 2,2 milyar $ (2024); 2033'te > 6 milyar $", "IMARC, Ekonomist [13]"],
    ["SAM: platform ve YZ değerlendirme (hedef segmentler)", "≈ 180–250 milyon $", "Tahmin (TAM'ın ≈ %8–10'u)"],
    ["SOM: 3. yıl", "≈ 1–2 milyon $", "Tahmin (SAM'ın ≈ %0,5–1'i)"],
  ], [4, 3, 3]),
  BOS(),
  tablo(["Paket", "Hedef müşteri", "Fiyat (KDV hariç, 2027)"], [
    ["Kurum Asistan / Kurum Tam", "Kurs, etüt merkezi, özel okul, SEM", "60 / 85 TL / aktif öğrenci / ay"],
    ["Eğitmen Başlangıç / Pro", "Bireysel eğitmen", "499 / 999 TL / ay"],
    ["Kurum içi kurulum lisansı", "Kurumsal akademi, kamu, üniversite", "1,5–3 milyon TL / yıl + %20 bakım"],
    ["API", "LMS'ler, yayınevleri", "1.000 sorgu başına ücret"],
  ], [3, 3.6, 3.4]),
  BOS(),
  tablo(["Yıl", "Kurum (ortalama)", "Bireysel eğitmen (ortalama)", "Toplam gelir (temkinli)"], [
    ["2028", "10", "300", "≈ 3,2 milyon TL"],
    ["2029", "40", "1.200", "≈ 17,1 milyon TL"],
    ["2030", "120", "3.000", "≈ 54,4 milyon TL"],
  ], [1.5, 2.5, 3, 3], 3));

// ---------------- 12. İthal ikame ve ihracat ----------------
ekle(H1("13. İthal İkame ve İhracat"),
  B("İthal ikame: ", "Kurumların döviz bazlı ödediği video konferans hizmetleri, yabancı öğrenme yönetim sistemleri, kurumsal yapay zekâ abonelikleri ve API'leri ile yabancı değerlendirme araçlarının yerine yerli ve yurt içinde barındırılan tek bir platform sunulacaktır."),
  B("İhracat: ", "2028'de Azerbaycan ve KKTC; 2028–2029'da Kazakistan ve Özbekistan; 2029'dan itibaren AB YZ Yasası uyumlu tasarımla Almanya ve AB pazarı. Dil bağımsız mimari ve çok dilli modeller Faz 1'de kurulacaktır."));

// ---------------- 13. Etkiler ----------------
ekle(H1("14. Beklenen Etkiler"),
  tablo(["Alan", "Beklenen etki", "Ölçüm"], [
    ["Eğitim kalitesi", "Öğrenciye ders dışında kaynağa dayalı destek; Sokratik tasarımla öğrenmenin korunması", "Pilot kullanım ve memnuniyet"],
    ["Verimlilik", "Eğitmenin ödev değerlendirme süresinde en az %40 azalma (hedef)", "Pilotta denek içi süre ölçümü"],
    ["Kalite ve standart", "AB YZ Yasası ve KVKK uyumlu tasarım; WCAG 2.2 AA erişilebilirlik", "Kalite panosu; sızma testi; erişilebilirlik denetimi"],
    ["Maliyet", "Döviz bazlı araçların tek yerli platformda birleşmesi; yurt içi modelle yapay zekâ maliyetinde en az %60 düşüş (hedef)", "Maliyet karşılaştırma deneyi"],
    ["Katma değer", "Nitelikli istihdam; YTÜ'de geliştirilen Türkçe modellerin ticari kullanımı; ihraç edilebilir yazılım", "İstihdam, ihracat ve yayın göstergeleri"],
    ["Teknolojik bilgi", "Türkçe eğitim test setleri; doğrulama ve kalibrasyon yöntemleri", "Yayın ve fikri mülkiyet başvuruları"],
  ], [2, 5, 3]));

// ---------------- 14. Bütçe ----------------
ekle(H1("15. Bütçe ve Finansman"),
  tablo(["Kalem", "Tutar (TL, 12 ay)"], [
    ["Ar-Ge personeli (78 kişi-ay, teşvik sonrası tahmini) ve stajyerler", "≈ 10.400.000"],
    ["Altyapı: yurt içi GPU, uygulama bulutu, karşılaştırma amaçlı API", "2.260.000"],
    ["Akademik danışmanlık (YTÜ TTO)", "960.000"],
    ["Kira ve işletme gideri (≈ 70 m²)", "840.000"],
    ["Hizmet alımları: etiketleme, sızma testi, hukuk/KVKK, fikri mülkiyet, pilot, yazılım, seyahat", "2.000.000"],
    ["Beklenmeyen giderler (%7)", "≈ 1.150.000"],
    ["TOPLAM (teşvik sonrası)", "≈ 17.600.000"],
  ], [7, 3]),
  NOT("Teşvik öncesi toplam ≈ 21,2 milyon TL. Tutarlar 2027 fiyatlarıyla tahmindir. Proje, kurumun yıllık gelirinin (≈ 240 milyon TL) yaklaşık %7–9'u olup öz kaynakla finanse edilecektir; TÜBİTAK 1507/1501 başvurusu planlanmaktadır."));

// ---------------- 15. Riskler ----------------
ekle(H1("16. Başlıca Riskler ve B Planları"),
  tablo(["Risk", "Önlem", "B planı"], [
    ["Kappa ≥ 0,75 hedefine ulaşılamaması", "Kanıt çıkarımı, eğitmen puanlı örnekler, kalibrasyon, rubrik iyileştirme", "Asistan modu; eğitmen süresindeki kazanç korunur"],
    ["Sadakat ve reddetmenin birlikte sağlanamaması", "Ceza-duyarlı eşik, iddia doğrulama", "Kurum bazlı eşik, kısmi yanıt"],
    ["Kıdemli YZ mühendisi istihdamının gecikmesi", "Erken ilan, teknopark ücret avantajı", "Sözleşmeli uzman ve akademik destek"],
    ["Yerli açık model kalitesinin yetersiz kalması", "Çoklu aday model, ince ayar", "Anonimleştirilmiş hibrit model"],
    ["Dış kurum pilotunun bulunamaması", "Hedef kurum listesi, Yıldız ağı, ücretsiz pilot", "Ortak kurslar"],
    ["Faz 2 başvurusunun gecikmesi", "Ertelenemez kilometre taşı (KT-6)", "Faz 1 ek süre talebi ve erken başvuru"],
  ], [3.2, 3.6, 3.2]));

// ---------------- 16. FMH ----------------
ekle(H1("17. Fikri Mülkiyet"),
  M("Teknik yöntemler için Yıldız TTO ve patent vekiliyle patentlenebilirlik değerlendirmesi yapılacaktır: (1) ceza-duyarlı cevaplanabilirlik kapısı ve iddia düzeyinde atıf doğrulama, (2) örneklerle karşılaştırmalı rubrik değerlendirme ve seçici eğitmen yönlendirmesi, (3) konuşma düzeyinde birikimli pedagojik sızıntı takibi."),
  M("Kaynak kod FSEK kapsamında korunacak; model ağırlıkları, istemler ve kalibrasyon verisi ticari sır olarak saklanacak; ürün adı için marka tescili yapılacaktır."),
  M("Yayın politikası: önce başvuru, ardından YTÜ ile ortak akademik yayın."));

// ---------------- 17. Katkı ----------------
ekle(H1("18. Yıldız Teknopark'a Katkı"),
  tablo(["Gösterge", "Faz 1 sonu (12 ay)", "36 ay"], [
    ["Teknoparktaki Ar-Ge personeli", "7", "15+"],
    ["YTÜ akademik danışman", "2", "3+"],
    ["YTÜ stajyer / tez öğrencisi", "2", "6+"],
    ["Destekli proje (TÜBİTAK / KOSGEB)", "1 başvuru", "2+"],
    ["Patent / tescil başvurusu", "1", "3+"],
    ["Ortak akademik yayın", "1 gönderim", "3+"],
    ["İhracat", "Ön temas", "2+ ülke"],
  ], [5, 2.5, 2.5]));

// ---------------- Kaynakça ----------------
ekle(H1("Kaynakça"),
  ...[
    "[1] Do Rosario, Younes, Pires. Why RAGs Hallucinate: Penalty-Aware Evaluation of Retrieval-Augmented Generation Systems with Knowledge-Gap Canaries, arXiv:2608.26385 (2026).",
    "[2] Bastani, Bastani, Sungu, Ge, Kabakcı, Mariman. Generative AI without guardrails can harm learning: Evidence from high school mathematics, PNAS 122(26) (2025).",
    "[3] KVKK, Kişisel Verilerin Yurt Dışına Aktarılması Rehberi; 7499 sayılı Kanun ile değişik KVKK md. 9.",
    "[4] Assessing the Reliability and Validity of LLMs for Automated Assessment of Student Essays in Higher Education, arXiv:2508.02442 (2025).",
    "[5] Exploring potential of large language models for automated essay scoring in education, Discover Artificial Intelligence, Springer (2026).",
    "[6] Google Workspace Updates: NotebookLM in Google Classroom (Nisan 2026); Gemini in Classroom (Ağustos 2026).",
    "[7] TR-MTEB: A Comprehensive Benchmark and Embedding Model for Turkish, Findings of EMNLP (2025).",
    "[8] TR-TEB: Turkish Text Embedding Benchmark (2025–2026).",
    "[9] Harada ve ark. Automated Refinement of Essay Scoring Rubrics for Language Models via Reflect-and-Revise, arXiv:2510.09030 (CoNLL 2026).",
    "[10] ufakzeka-kulak: Building and Evaluating a Turkish Speech Recognizer, arXiv:2611.03605 (2026).",
    "[11] YTÜ COSMOS Araştırma Grubu, Hugging Face model kartları (Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, turkish-e5-large).",
    "[12] AB Yapay Zekâ Yasası (Regulation (EU) 2024/1689), Ek III(3).",
    "[13] IMARC Group, Türkiye EdTech pazar raporu (Ekonomist, 2025); Ken Research, Turkey E-Learning and Upskilling Platforms Market (2025).",
  ].map((t) => P(t, { size: 18, after: 60, align: AlignmentType.LEFT })));

// ---------------- Belge ----------------
const doc = new Document({
  creator: "Başvuran Kurum",
  title: "KAYNAK-YZ · Proje Özeti",
  description: "YTÜ Yıldız Teknopark Aday Firma Başvurusu – Proje Özeti",
  styles: {
    default: { document: { run: { font: "Calibri", size: 21, color: "1F2933" }, paragraph: { spacing: { line: 276 } } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: "Cambria", size: 28, bold: true, color: TEAL }, paragraph: { spacing: { before: 320, after: 140 }, keepNext: true, keepLines: true, outlineLevel: 0, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "D9E2DF", space: 4 } } } },
    ],
  },
  numbering: { config: [{ reference: "madde", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1134, right: 1134, header: 567, footer: 567 } }, titlePage: true },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: "KAYNAK-YZ · YTÜ Yıldız Teknopark Aday Firma Başvurusu · Proje Özeti", color: GRI, size: 16 })] })] }) },
    footers: {
      default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Gizlidir; yalnızca değerlendirme amacıyla kullanılabilir · Sayfa ", color: GRI, size: 16 }), new TextRun({ children: [PageNumber.CURRENT], color: GRI, size: 16 }), new TextRun({ text: " / ", color: GRI, size: 16 }), new TextRun({ children: [PageNumber.TOTAL_PAGES], color: GRI, size: 16 })] })] }),
      first: new Footer({ children: [new Paragraph({ children: [] })] }),
    },
    children: govde,
  }],
});

Packer.toBuffer(doc).then((b) => { fs.writeFileSync(OUT, b); console.log("yazıldı:", OUT); });
