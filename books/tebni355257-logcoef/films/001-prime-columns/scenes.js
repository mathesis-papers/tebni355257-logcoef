'use strict';

const headline = (label, y, size, alpha, color = C.white) =>
  txt(label, W / 2, y, { size, align: 'center', fam: F.mono, c: color, a: alpha });

const terms = (scene, survivor) => {
  const pieces = ['3n(n+1)', '9n', '14'];
  pieces.forEach((piece, index) => {
    const left = 270 + index * 465;
    const reveal = at(scene, 0, 0.65);
    const isolate = at(scene, 1, 0.6);
    const selected = index === survivor;
    const alpha = reveal * (selected ? 1 : 1 - 0.72 * isolate);
    const color = selected ? C.now : C.cyan;
    panel(left, 340, 425, 230, alpha, color, `j = ${index + 1}`);
    txt(piece, left + 212, 475, { size: 74, align: 'center', fam: F.mono, c: color, a: alpha });
  });
};

SCENES.open = scene => {
  headline('WHAT SURVIVES AT A PRIME COLUMN?', 230, 54, at(scene, 0, 0.7));
  headline('14     29     50', 460, 110, at(scene, 0, 0.8), C.cyan);
  headline('DIVIDE BY THREE  /  DIVIDE BY TWO', 665, 45, at(scene, 1, 0.6), C.now);
};

SCENES.last = scene => {
  headline('MODULO 3: THE LAST TERM SURVIVES', 225, 52, at(scene, 0, 0.6));
  terms(scene, 2);
  headline('14 ≡ 2  (MOD 3)', 695, 62, at(scene, 1, 0.7), C.now);
};

SCENES.penultimate = scene => {
  headline('MODULO 2: THE MIDDLE TERM SURVIVES', 225, 50, at(scene, 0, 0.6));
  terms(scene, 1);
  headline('9n ≡ n  (MOD 2)', 665, 56, at(scene, 0, 0.7, 1.8), C.now);
  headline('ONLY 3 AND 5 CAN FAIL', 770, 38, at(scene, 1, 0.6));
};

SCENES.close = scene => {
  headline('ODD ROWS FAIL ONLY AT 3 AND 5', 255, 54, at(scene, 0, 0.65), C.now);
  headline('P₃(n) = 3n² + 12n + 14', 490, 78, at(scene, 1, 0.75), C.cyan);
  headline('HAOBO MA AND WENLIN ZHANG  /  PAPER V2', 680, 35, at(scene, 1, 0.65));
  headline('DOI 10.5281/zenodo.24406609', 745, 32, at(scene, 1, 0.65));
};
