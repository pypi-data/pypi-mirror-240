const Ln = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], ht = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
};
Ln.reduce(
  (l, { color: e, primary: t, secondary: n }) => ({
    ...l,
    [e]: {
      primary: ht[e][t],
      secondary: ht[e][n]
    }
  }),
  {}
);
function zn(l) {
  let e, t = l[0], n = 1;
  for (; n < l.length; ) {
    const i = l[n], s = l[n + 1];
    if (n += 2, (i === "optionalAccess" || i === "optionalCall") && t == null)
      return;
    i === "access" || i === "optionalAccess" ? (e = t, t = s(t)) : (i === "call" || i === "optionalCall") && (t = s((...o) => t.call(e, ...o)), e = void 0);
  }
  return t;
}
class Ae extends Error {
  constructor(e) {
    super(e), this.name = "ShareError";
  }
}
async function An(l, e) {
  if (window.__gradio_space__ == null)
    throw new Ae("Must be on Spaces to share.");
  let t, n, i;
  if (e === "url") {
    const r = await fetch(l);
    t = await r.blob(), n = r.headers.get("content-type") || "", i = r.headers.get("content-disposition") || "";
  } else
    t = Bn(l), n = l.split(";")[0].split(":")[1], i = "file" + n.split("/")[1];
  const s = new File([t], i, { type: n }), o = await fetch("https://huggingface.co/uploads", {
    method: "POST",
    body: s,
    headers: {
      "Content-Type": s.type,
      "X-Requested-With": "XMLHttpRequest"
    }
  });
  if (!o.ok) {
    if (zn([o, "access", (r) => r.headers, "access", (r) => r.get, "call", (r) => r("content-type"), "optionalAccess", (r) => r.includes, "call", (r) => r("application/json")])) {
      const r = await o.json();
      throw new Ae(`Upload failed: ${r.error}`);
    }
    throw new Ae("Upload failed.");
  }
  return await o.text();
}
function Bn(l) {
  for (var e = l.split(","), t = e[0].match(/:(.*?);/)[1], n = atob(e[1]), i = n.length, s = new Uint8Array(i); i--; )
    s[i] = n.charCodeAt(i);
  return new Blob([s], { type: t });
}
const {
  SvelteComponent: Fn,
  assign: En,
  create_slot: Dn,
  detach: Rn,
  element: Vn,
  get_all_dirty_from_scope: Tn,
  get_slot_changes: Pn,
  get_spread_update: Nn,
  init: Xn,
  insert: Yn,
  safe_not_equal: jn,
  set_dynamic_element_data: gt,
  set_style: F,
  toggle_class: K,
  transition_in: an,
  transition_out: rn,
  update_slot_base: Zn
} = window.__gradio__svelte__internal;
function Un(l) {
  let e, t, n;
  const i = (
    /*#slots*/
    l[17].default
  ), s = Dn(
    i,
    l,
    /*$$scope*/
    l[16],
    null
  );
  let o = [
    { "data-testid": (
      /*test_id*/
      l[7]
    ) },
    { id: (
      /*elem_id*/
      l[2]
    ) },
    {
      class: t = "block " + /*elem_classes*/
      l[3].join(" ") + " svelte-1t38q2d"
    }
  ], a = {};
  for (let r = 0; r < o.length; r += 1)
    a = En(a, o[r]);
  return {
    c() {
      e = Vn(
        /*tag*/
        l[14]
      ), s && s.c(), gt(
        /*tag*/
        l[14]
      )(e, a), K(
        e,
        "hidden",
        /*visible*/
        l[10] === !1
      ), K(
        e,
        "padded",
        /*padding*/
        l[6]
      ), K(
        e,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), K(e, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), F(e, "height", typeof /*height*/
      l[0] == "number" ? (
        /*height*/
        l[0] + "px"
      ) : void 0), F(e, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : void 0), F(
        e,
        "border-style",
        /*variant*/
        l[4]
      ), F(
        e,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), F(
        e,
        "flex-grow",
        /*scale*/
        l[12]
      ), F(e, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`), F(e, "border-width", "var(--block-border-width)");
    },
    m(r, f) {
      Yn(r, e, f), s && s.m(e, null), n = !0;
    },
    p(r, f) {
      s && s.p && (!n || f & /*$$scope*/
      65536) && Zn(
        s,
        i,
        r,
        /*$$scope*/
        r[16],
        n ? Pn(
          i,
          /*$$scope*/
          r[16],
          f,
          null
        ) : Tn(
          /*$$scope*/
          r[16]
        ),
        null
      ), gt(
        /*tag*/
        r[14]
      )(e, a = Nn(o, [
        (!n || f & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          r[7]
        ) },
        (!n || f & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          r[2]
        ) },
        (!n || f & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        r[3].join(" ") + " svelte-1t38q2d")) && { class: t }
      ])), K(
        e,
        "hidden",
        /*visible*/
        r[10] === !1
      ), K(
        e,
        "padded",
        /*padding*/
        r[6]
      ), K(
        e,
        "border_focus",
        /*border_mode*/
        r[5] === "focus"
      ), K(e, "hide-container", !/*explicit_call*/
      r[8] && !/*container*/
      r[9]), f & /*height*/
      1 && F(e, "height", typeof /*height*/
      r[0] == "number" ? (
        /*height*/
        r[0] + "px"
      ) : void 0), f & /*width*/
      2 && F(e, "width", typeof /*width*/
      r[1] == "number" ? `calc(min(${/*width*/
      r[1]}px, 100%))` : void 0), f & /*variant*/
      16 && F(
        e,
        "border-style",
        /*variant*/
        r[4]
      ), f & /*allow_overflow*/
      2048 && F(
        e,
        "overflow",
        /*allow_overflow*/
        r[11] ? "visible" : "hidden"
      ), f & /*scale*/
      4096 && F(
        e,
        "flex-grow",
        /*scale*/
        r[12]
      ), f & /*min_width*/
      8192 && F(e, "min-width", `calc(min(${/*min_width*/
      r[13]}px, 100%))`);
    },
    i(r) {
      n || (an(s, r), n = !0);
    },
    o(r) {
      rn(s, r), n = !1;
    },
    d(r) {
      r && Rn(e), s && s.d(r);
    }
  };
}
function On(l) {
  let e, t = (
    /*tag*/
    l[14] && Un(l)
  );
  return {
    c() {
      t && t.c();
    },
    m(n, i) {
      t && t.m(n, i), e = !0;
    },
    p(n, [i]) {
      /*tag*/
      n[14] && t.p(n, i);
    },
    i(n) {
      e || (an(t, n), e = !0);
    },
    o(n) {
      rn(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function Hn(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { height: s = void 0 } = e, { width: o = void 0 } = e, { elem_id: a = "" } = e, { elem_classes: r = [] } = e, { variant: f = "solid" } = e, { border_mode: _ = "base" } = e, { padding: c = !0 } = e, { type: u = "normal" } = e, { test_id: d = void 0 } = e, { explicit_call: g = !1 } = e, { container: p = !0 } = e, { visible: C = !0 } = e, { allow_overflow: I = !0 } = e, { scale: S = null } = e, { min_width: m = 0 } = e, y = u === "fieldset" ? "fieldset" : "div";
  return l.$$set = (w) => {
    "height" in w && t(0, s = w.height), "width" in w && t(1, o = w.width), "elem_id" in w && t(2, a = w.elem_id), "elem_classes" in w && t(3, r = w.elem_classes), "variant" in w && t(4, f = w.variant), "border_mode" in w && t(5, _ = w.border_mode), "padding" in w && t(6, c = w.padding), "type" in w && t(15, u = w.type), "test_id" in w && t(7, d = w.test_id), "explicit_call" in w && t(8, g = w.explicit_call), "container" in w && t(9, p = w.container), "visible" in w && t(10, C = w.visible), "allow_overflow" in w && t(11, I = w.allow_overflow), "scale" in w && t(12, S = w.scale), "min_width" in w && t(13, m = w.min_width), "$$scope" in w && t(16, i = w.$$scope);
  }, [
    s,
    o,
    a,
    r,
    f,
    _,
    c,
    d,
    g,
    p,
    C,
    I,
    S,
    m,
    y,
    u,
    i,
    n
  ];
}
class Wn extends Fn {
  constructor(e) {
    super(), Xn(this, e, Hn, On, jn, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 15,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
const {
  SvelteComponent: Gn,
  append: Re,
  attr: Se,
  create_component: Kn,
  destroy_component: Jn,
  detach: Qn,
  element: bt,
  init: xn,
  insert: $n,
  mount_component: el,
  safe_not_equal: tl,
  set_data: nl,
  space: ll,
  text: il,
  toggle_class: J,
  transition_in: sl,
  transition_out: ol
} = window.__gradio__svelte__internal;
function al(l) {
  let e, t, n, i, s, o;
  return n = new /*Icon*/
  l[1]({}), {
    c() {
      e = bt("label"), t = bt("span"), Kn(n.$$.fragment), i = ll(), s = il(
        /*label*/
        l[0]
      ), Se(t, "class", "svelte-9gxdi0"), Se(e, "for", ""), Se(e, "data-testid", "block-label"), Se(e, "class", "svelte-9gxdi0"), J(e, "hide", !/*show_label*/
      l[2]), J(e, "sr-only", !/*show_label*/
      l[2]), J(
        e,
        "float",
        /*float*/
        l[4]
      ), J(
        e,
        "hide-label",
        /*disable*/
        l[3]
      );
    },
    m(a, r) {
      $n(a, e, r), Re(e, t), el(n, t, null), Re(e, i), Re(e, s), o = !0;
    },
    p(a, [r]) {
      (!o || r & /*label*/
      1) && nl(
        s,
        /*label*/
        a[0]
      ), (!o || r & /*show_label*/
      4) && J(e, "hide", !/*show_label*/
      a[2]), (!o || r & /*show_label*/
      4) && J(e, "sr-only", !/*show_label*/
      a[2]), (!o || r & /*float*/
      16) && J(
        e,
        "float",
        /*float*/
        a[4]
      ), (!o || r & /*disable*/
      8) && J(
        e,
        "hide-label",
        /*disable*/
        a[3]
      );
    },
    i(a) {
      o || (sl(n.$$.fragment, a), o = !0);
    },
    o(a) {
      ol(n.$$.fragment, a), o = !1;
    },
    d(a) {
      a && Qn(e), Jn(n);
    }
  };
}
function rl(l, e, t) {
  let { label: n = null } = e, { Icon: i } = e, { show_label: s = !0 } = e, { disable: o = !1 } = e, { float: a = !0 } = e;
  return l.$$set = (r) => {
    "label" in r && t(0, n = r.label), "Icon" in r && t(1, i = r.Icon), "show_label" in r && t(2, s = r.show_label), "disable" in r && t(3, o = r.disable), "float" in r && t(4, a = r.float);
  }, [n, i, s, o, a];
}
class fl extends Gn {
  constructor(e) {
    super(), xn(this, e, rl, al, tl, {
      label: 0,
      Icon: 1,
      show_label: 2,
      disable: 3,
      float: 4
    });
  }
}
const {
  SvelteComponent: _l,
  append: Oe,
  attr: ne,
  bubble: cl,
  create_component: ul,
  destroy_component: dl,
  detach: fn,
  element: He,
  init: ml,
  insert: _n,
  listen: hl,
  mount_component: gl,
  safe_not_equal: bl,
  set_data: wl,
  space: pl,
  text: vl,
  toggle_class: Q,
  transition_in: kl,
  transition_out: yl
} = window.__gradio__svelte__internal;
function wt(l) {
  let e, t;
  return {
    c() {
      e = He("span"), t = vl(
        /*label*/
        l[1]
      ), ne(e, "class", "svelte-xtz2g8");
    },
    m(n, i) {
      _n(n, e, i), Oe(e, t);
    },
    p(n, i) {
      i & /*label*/
      2 && wl(
        t,
        /*label*/
        n[1]
      );
    },
    d(n) {
      n && fn(e);
    }
  };
}
function Cl(l) {
  let e, t, n, i, s, o, a, r = (
    /*show_label*/
    l[2] && wt(l)
  );
  return i = new /*Icon*/
  l[0]({}), {
    c() {
      e = He("button"), r && r.c(), t = pl(), n = He("div"), ul(i.$$.fragment), ne(n, "class", "svelte-xtz2g8"), Q(
        n,
        "small",
        /*size*/
        l[4] === "small"
      ), Q(
        n,
        "large",
        /*size*/
        l[4] === "large"
      ), ne(
        e,
        "aria-label",
        /*label*/
        l[1]
      ), ne(
        e,
        "title",
        /*label*/
        l[1]
      ), ne(e, "class", "svelte-xtz2g8"), Q(
        e,
        "pending",
        /*pending*/
        l[3]
      ), Q(
        e,
        "padded",
        /*padded*/
        l[5]
      );
    },
    m(f, _) {
      _n(f, e, _), r && r.m(e, null), Oe(e, t), Oe(e, n), gl(i, n, null), s = !0, o || (a = hl(
        e,
        "click",
        /*click_handler*/
        l[6]
      ), o = !0);
    },
    p(f, [_]) {
      /*show_label*/
      f[2] ? r ? r.p(f, _) : (r = wt(f), r.c(), r.m(e, t)) : r && (r.d(1), r = null), (!s || _ & /*size*/
      16) && Q(
        n,
        "small",
        /*size*/
        f[4] === "small"
      ), (!s || _ & /*size*/
      16) && Q(
        n,
        "large",
        /*size*/
        f[4] === "large"
      ), (!s || _ & /*label*/
      2) && ne(
        e,
        "aria-label",
        /*label*/
        f[1]
      ), (!s || _ & /*label*/
      2) && ne(
        e,
        "title",
        /*label*/
        f[1]
      ), (!s || _ & /*pending*/
      8) && Q(
        e,
        "pending",
        /*pending*/
        f[3]
      ), (!s || _ & /*padded*/
      32) && Q(
        e,
        "padded",
        /*padded*/
        f[5]
      );
    },
    i(f) {
      s || (kl(i.$$.fragment, f), s = !0);
    },
    o(f) {
      yl(i.$$.fragment, f), s = !1;
    },
    d(f) {
      f && fn(e), r && r.d(), dl(i), o = !1, a();
    }
  };
}
function ql(l, e, t) {
  let { Icon: n } = e, { label: i = "" } = e, { show_label: s = !1 } = e, { pending: o = !1 } = e, { size: a = "small" } = e, { padded: r = !0 } = e;
  function f(_) {
    cl.call(this, l, _);
  }
  return l.$$set = (_) => {
    "Icon" in _ && t(0, n = _.Icon), "label" in _ && t(1, i = _.label), "show_label" in _ && t(2, s = _.show_label), "pending" in _ && t(3, o = _.pending), "size" in _ && t(4, a = _.size), "padded" in _ && t(5, r = _.padded);
  }, [n, i, s, o, a, r, f];
}
class cn extends _l {
  constructor(e) {
    super(), ml(this, e, ql, Cl, bl, {
      Icon: 0,
      label: 1,
      show_label: 2,
      pending: 3,
      size: 4,
      padded: 5
    });
  }
}
const {
  SvelteComponent: Sl,
  append: Ml,
  attr: Ve,
  binding_callbacks: Il,
  create_slot: Ll,
  detach: zl,
  element: pt,
  get_all_dirty_from_scope: Al,
  get_slot_changes: Bl,
  init: Fl,
  insert: El,
  safe_not_equal: Dl,
  toggle_class: x,
  transition_in: Rl,
  transition_out: Vl,
  update_slot_base: Tl
} = window.__gradio__svelte__internal;
function Pl(l) {
  let e, t, n;
  const i = (
    /*#slots*/
    l[5].default
  ), s = Ll(
    i,
    l,
    /*$$scope*/
    l[4],
    null
  );
  return {
    c() {
      e = pt("div"), t = pt("div"), s && s.c(), Ve(t, "class", "icon svelte-3w3rth"), Ve(e, "class", "empty svelte-3w3rth"), Ve(e, "aria-label", "Empty value"), x(
        e,
        "small",
        /*size*/
        l[0] === "small"
      ), x(
        e,
        "large",
        /*size*/
        l[0] === "large"
      ), x(
        e,
        "unpadded_box",
        /*unpadded_box*/
        l[1]
      ), x(
        e,
        "small_parent",
        /*parent_height*/
        l[3]
      );
    },
    m(o, a) {
      El(o, e, a), Ml(e, t), s && s.m(t, null), l[6](e), n = !0;
    },
    p(o, [a]) {
      s && s.p && (!n || a & /*$$scope*/
      16) && Tl(
        s,
        i,
        o,
        /*$$scope*/
        o[4],
        n ? Bl(
          i,
          /*$$scope*/
          o[4],
          a,
          null
        ) : Al(
          /*$$scope*/
          o[4]
        ),
        null
      ), (!n || a & /*size*/
      1) && x(
        e,
        "small",
        /*size*/
        o[0] === "small"
      ), (!n || a & /*size*/
      1) && x(
        e,
        "large",
        /*size*/
        o[0] === "large"
      ), (!n || a & /*unpadded_box*/
      2) && x(
        e,
        "unpadded_box",
        /*unpadded_box*/
        o[1]
      ), (!n || a & /*parent_height*/
      8) && x(
        e,
        "small_parent",
        /*parent_height*/
        o[3]
      );
    },
    i(o) {
      n || (Rl(s, o), n = !0);
    },
    o(o) {
      Vl(s, o), n = !1;
    },
    d(o) {
      o && zl(e), s && s.d(o), l[6](null);
    }
  };
}
function Nl(l) {
  let e, t = l[0], n = 1;
  for (; n < l.length; ) {
    const i = l[n], s = l[n + 1];
    if (n += 2, (i === "optionalAccess" || i === "optionalCall") && t == null)
      return;
    i === "access" || i === "optionalAccess" ? (e = t, t = s(t)) : (i === "call" || i === "optionalCall") && (t = s((...o) => t.call(e, ...o)), e = void 0);
  }
  return t;
}
function Xl(l, e, t) {
  let n, { $$slots: i = {}, $$scope: s } = e, { size: o = "small" } = e, { unpadded_box: a = !1 } = e, r;
  function f(c) {
    if (!c)
      return !1;
    const { height: u } = c.getBoundingClientRect(), { height: d } = Nl([
      c,
      "access",
      (g) => g.parentElement,
      "optionalAccess",
      (g) => g.getBoundingClientRect,
      "call",
      (g) => g()
    ]) || { height: u };
    return u > d + 2;
  }
  function _(c) {
    Il[c ? "unshift" : "push"](() => {
      r = c, t(2, r);
    });
  }
  return l.$$set = (c) => {
    "size" in c && t(0, o = c.size), "unpadded_box" in c && t(1, a = c.unpadded_box), "$$scope" in c && t(4, s = c.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty & /*el*/
    4 && t(3, n = f(r));
  }, [o, a, r, n, s, i, _];
}
class Yl extends Sl {
  constructor(e) {
    super(), Fl(this, e, Xl, Pl, Dl, { size: 0, unpadded_box: 1 });
  }
}
const {
  SvelteComponent: jl,
  append: Zl,
  attr: ye,
  detach: Ul,
  init: Ol,
  insert: Hl,
  noop: Te,
  safe_not_equal: Wl,
  svg_element: vt
} = window.__gradio__svelte__internal;
function Gl(l) {
  let e, t;
  return {
    c() {
      e = vt("svg"), t = vt("path"), ye(t, "d", "M23,20a5,5,0,0,0-3.89,1.89L11.8,17.32a4.46,4.46,0,0,0,0-2.64l7.31-4.57A5,5,0,1,0,18,7a4.79,4.79,0,0,0,.2,1.32l-7.31,4.57a5,5,0,1,0,0,6.22l7.31,4.57A4.79,4.79,0,0,0,18,25a5,5,0,1,0,5-5ZM23,4a3,3,0,1,1-3,3A3,3,0,0,1,23,4ZM7,19a3,3,0,1,1,3-3A3,3,0,0,1,7,19Zm16,9a3,3,0,1,1,3-3A3,3,0,0,1,23,28Z"), ye(t, "fill", "currentColor"), ye(e, "id", "icon"), ye(e, "xmlns", "http://www.w3.org/2000/svg"), ye(e, "viewBox", "0 0 32 32");
    },
    m(n, i) {
      Hl(n, e, i), Zl(e, t);
    },
    p: Te,
    i: Te,
    o: Te,
    d(n) {
      n && Ul(e);
    }
  };
}
class Kl extends jl {
  constructor(e) {
    super(), Ol(this, e, null, Gl, Wl, {});
  }
}
const {
  SvelteComponent: Jl,
  append: Ql,
  attr: oe,
  detach: xl,
  init: $l,
  insert: ei,
  noop: Pe,
  safe_not_equal: ti,
  svg_element: kt
} = window.__gradio__svelte__internal;
function ni(l) {
  let e, t;
  return {
    c() {
      e = kt("svg"), t = kt("path"), oe(t, "fill", "currentColor"), oe(t, "d", "M26 24v4H6v-4H4v4a2 2 0 0 0 2 2h20a2 2 0 0 0 2-2v-4zm0-10l-1.41-1.41L17 20.17V2h-2v18.17l-7.59-7.58L6 14l10 10l10-10z"), oe(e, "xmlns", "http://www.w3.org/2000/svg"), oe(e, "width", "100%"), oe(e, "height", "100%"), oe(e, "viewBox", "0 0 32 32");
    },
    m(n, i) {
      ei(n, e, i), Ql(e, t);
    },
    p: Pe,
    i: Pe,
    o: Pe,
    d(n) {
      n && xl(e);
    }
  };
}
class li extends Jl {
  constructor(e) {
    super(), $l(this, e, null, ni, ti, {});
  }
}
const {
  SvelteComponent: ii,
  append: Ne,
  attr: L,
  detach: si,
  init: oi,
  insert: ai,
  noop: Xe,
  safe_not_equal: ri,
  svg_element: Me
} = window.__gradio__svelte__internal;
function fi(l) {
  let e, t, n, i;
  return {
    c() {
      e = Me("svg"), t = Me("rect"), n = Me("circle"), i = Me("polyline"), L(t, "x", "3"), L(t, "y", "3"), L(t, "width", "18"), L(t, "height", "18"), L(t, "rx", "2"), L(t, "ry", "2"), L(n, "cx", "8.5"), L(n, "cy", "8.5"), L(n, "r", "1.5"), L(i, "points", "21 15 16 10 5 21"), L(e, "xmlns", "http://www.w3.org/2000/svg"), L(e, "width", "100%"), L(e, "height", "100%"), L(e, "viewBox", "0 0 24 24"), L(e, "fill", "none"), L(e, "stroke", "currentColor"), L(e, "stroke-width", "1.5"), L(e, "stroke-linecap", "round"), L(e, "stroke-linejoin", "round"), L(e, "class", "feather feather-image");
    },
    m(s, o) {
      ai(s, e, o), Ne(e, t), Ne(e, n), Ne(e, i);
    },
    p: Xe,
    i: Xe,
    o: Xe,
    d(s) {
      s && si(e);
    }
  };
}
let un = class extends ii {
  constructor(e) {
    super(), oi(this, e, null, fi, ri, {});
  }
};
const {
  SvelteComponent: _i,
  create_component: ci,
  destroy_component: ui,
  init: di,
  mount_component: mi,
  safe_not_equal: hi,
  transition_in: gi,
  transition_out: bi
} = window.__gradio__svelte__internal, { createEventDispatcher: wi } = window.__gradio__svelte__internal;
function pi(l) {
  let e, t;
  return e = new cn({
    props: {
      Icon: Kl,
      label: (
        /*i18n*/
        l[2]("common.share")
      ),
      pending: (
        /*pending*/
        l[3]
      )
    }
  }), e.$on(
    "click",
    /*click_handler*/
    l[5]
  ), {
    c() {
      ci(e.$$.fragment);
    },
    m(n, i) {
      mi(e, n, i), t = !0;
    },
    p(n, [i]) {
      const s = {};
      i & /*i18n*/
      4 && (s.label = /*i18n*/
      n[2]("common.share")), i & /*pending*/
      8 && (s.pending = /*pending*/
      n[3]), e.$set(s);
    },
    i(n) {
      t || (gi(e.$$.fragment, n), t = !0);
    },
    o(n) {
      bi(e.$$.fragment, n), t = !1;
    },
    d(n) {
      ui(e, n);
    }
  };
}
function vi(l, e, t) {
  const n = wi();
  let { formatter: i } = e, { value: s } = e, { i18n: o } = e, a = !1;
  const r = async () => {
    try {
      t(3, a = !0);
      const f = await i(s);
      n("share", { description: f });
    } catch (f) {
      console.error(f);
      let _ = f instanceof Ae ? f.message : "Share failed.";
      n("error", _);
    } finally {
      t(3, a = !1);
    }
  };
  return l.$$set = (f) => {
    "formatter" in f && t(0, i = f.formatter), "value" in f && t(1, s = f.value), "i18n" in f && t(2, o = f.i18n);
  }, [i, s, o, a, n, r];
}
class ki extends _i {
  constructor(e) {
    super(), di(this, e, vi, pi, hi, { formatter: 0, value: 1, i18n: 2 });
  }
}
const yi = (l) => {
  let e = l.currentTarget;
  const t = e.getBoundingClientRect(), n = e.naturalWidth / t.width, i = e.naturalHeight / t.height;
  if (n > i) {
    const a = e.naturalHeight / n, r = (t.height - a) / 2;
    var s = Math.round((l.clientX - t.left) * n), o = Math.round((l.clientY - t.top - r) * n);
  } else {
    const a = e.naturalWidth / i, r = (t.width - a) / 2;
    var s = Math.round((l.clientX - t.left - r) * i), o = Math.round((l.clientY - t.top) * i);
  }
  return s < 0 || s >= e.naturalWidth || o < 0 || o >= e.naturalHeight ? null : [s, o];
};
new Intl.Collator(0, { numeric: 1 }).compare;
function dn(l, e, t) {
  if (l == null)
    return null;
  if (Array.isArray(l)) {
    const n = [];
    for (const i of l)
      i == null ? n.push(null) : n.push(dn(i, e, t));
    return n;
  }
  return l.is_stream ? t == null ? new Be({
    ...l,
    url: e + "/stream/" + l.path
  }) : new Be({
    ...l,
    url: "/proxy=" + t + "stream/" + l.path
  }) : new Be({
    ...l,
    url: qi(l.path, e, t)
  });
}
function Ci(l) {
  try {
    const e = new URL(l);
    return e.protocol === "http:" || e.protocol === "https:";
  } catch {
    return !1;
  }
}
function qi(l, e, t) {
  return l == null ? t ? `/proxy=${t}file=` : `${e}/file=` : Ci(l) ? l : t ? `/proxy=${t}file=${l}` : `${e}/file=${l}`;
}
class Be {
  constructor({
    path: e,
    url: t,
    orig_name: n,
    size: i,
    blob: s,
    is_stream: o,
    mime_type: a,
    alt_text: r
  }) {
    this.path = e, this.url = t, this.orig_name = n, this.size = i, this.blob = t ? void 0 : s, this.is_stream = o, this.mime_type = a, this.alt_text = r;
  }
}
class Si {
  constructor({ image: e, blurhash: t, width: n, height: i }) {
    this.image = e ? new Be(e) : void 0, this.blurhash = t, this.width = n, this.height = i;
  }
}
function mn(l, e, t) {
  if (l == null)
    return null;
  if (Array.isArray(l)) {
    const i = [];
    for (const s of l)
      i.push(mn(s, e));
    return i;
  }
  const n = l.image ? dn(l.image, e, null) : null;
  return new Si({
    image: n || void 0,
    blurhash: l.blurhash,
    width: l.width,
    height: l.height
  });
}
const {
  SvelteComponent: Mi,
  binding_callbacks: Ii,
  create_slot: Li,
  detach: zi,
  element: Ai,
  get_all_dirty_from_scope: Bi,
  get_slot_changes: Fi,
  init: Ei,
  insert: Di,
  safe_not_equal: Ri,
  transition_in: Vi,
  transition_out: Ti,
  update_slot_base: Pi
} = window.__gradio__svelte__internal, { onMount: Ni } = window.__gradio__svelte__internal, Xi = (l) => ({
  visible: l & /*visible*/
  4,
  hasBeenVisible: l & /*hasBeenVisible*/
  2
}), yt = (l) => ({
  visible: (
    /*visible*/
    l[2]
  ),
  hasBeenVisible: (
    /*hasBeenVisible*/
    l[1]
  )
});
function Yi(l) {
  let e, t;
  const n = (
    /*#slots*/
    l[5].default
  ), i = Li(
    n,
    l,
    /*$$scope*/
    l[4],
    yt
  );
  return {
    c() {
      e = Ai("div"), i && i.c();
    },
    m(s, o) {
      Di(s, e, o), i && i.m(e, null), l[6](e), t = !0;
    },
    p(s, [o]) {
      i && i.p && (!t || o & /*$$scope, visible, hasBeenVisible*/
      22) && Pi(
        i,
        n,
        s,
        /*$$scope*/
        s[4],
        t ? Fi(
          n,
          /*$$scope*/
          s[4],
          o,
          Xi
        ) : Bi(
          /*$$scope*/
          s[4]
        ),
        yt
      );
    },
    i(s) {
      t || (Vi(i, s), t = !0);
    },
    o(s) {
      Ti(i, s), t = !1;
    },
    d(s) {
      s && zi(e), i && i.d(s), l[6](null);
    }
  };
}
let ji = "0px 0px 200px 0px";
function Zi(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, s = null, o = !1, a = !1, r = null;
  Ni(() => (t(3, r = new IntersectionObserver(
    (_) => {
      t(2, o = _[0].isIntersecting), t(1, a = a || o);
    },
    { rootMargin: ji }
  )), r.observe(s), () => {
    a || r.unobserve(s);
  }));
  function f(_) {
    Ii[_ ? "unshift" : "push"](() => {
      s = _, t(0, s);
    });
  }
  return l.$$set = (_) => {
    "$$scope" in _ && t(4, i = _.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty & /*hasBeenVisible, observer, el*/
    11 && a && r.unobserve(s);
  }, [s, a, o, r, i, n, f];
}
class Ui extends Mi {
  constructor(e) {
    super(), Ei(this, e, Zi, Yi, Ri, {});
  }
}
const Oi = [
  "0",
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
  "#",
  "$",
  "%",
  "*",
  "+",
  ",",
  "-",
  ".",
  ":",
  ";",
  "=",
  "?",
  "@",
  "[",
  "]",
  "^",
  "_",
  "{",
  "|",
  "}",
  "~"
], Ce = (l) => {
  let e = 0;
  for (let t = 0; t < l.length; t++) {
    const n = l[t], i = Oi.indexOf(n);
    e = e * 83 + i;
  }
  return e;
}, Ye = (l) => {
  let e = l / 255;
  return e <= 0.04045 ? e / 12.92 : Math.pow((e + 0.055) / 1.055, 2.4);
}, je = (l) => {
  let e = Math.max(0, Math.min(1, l));
  return e <= 31308e-7 ? Math.round(e * 12.92 * 255 + 0.5) : Math.round((1.055 * Math.pow(e, 1 / 2.4) - 0.055) * 255 + 0.5);
}, Hi = (l) => l < 0 ? -1 : 1, Ze = (l, e) => Hi(l) * Math.pow(Math.abs(l), e);
class Ct extends Error {
  constructor(e) {
    super(e), this.name = "ValidationError", this.message = e;
  }
}
const Wi = (l) => {
  if (!l || l.length < 6)
    throw new Ct("The blurhash string must be at least 6 characters");
  const e = Ce(l[0]), t = Math.floor(e / 9) + 1, n = e % 9 + 1;
  if (l.length !== 4 + 2 * n * t)
    throw new Ct(`blurhash length mismatch: length is ${l.length} but it should be ${4 + 2 * n * t}`);
}, Gi = (l) => {
  const e = l >> 16, t = l >> 8 & 255, n = l & 255;
  return [Ye(e), Ye(t), Ye(n)];
}, Ki = (l, e) => {
  const t = Math.floor(l / 361), n = Math.floor(l / 19) % 19, i = l % 19;
  return [
    Ze((t - 9) / 9, 2) * e,
    Ze((n - 9) / 9, 2) * e,
    Ze((i - 9) / 9, 2) * e
  ];
}, Ji = (l, e, t, n) => {
  Wi(l), n = n | 1;
  const i = Ce(l[0]), s = Math.floor(i / 9) + 1, o = i % 9 + 1, r = (Ce(l[1]) + 1) / 166, f = new Array(o * s);
  for (let u = 0; u < f.length; u++)
    if (u === 0) {
      const d = Ce(l.substring(2, 6));
      f[u] = Gi(d);
    } else {
      const d = Ce(l.substring(4 + u * 2, 6 + u * 2));
      f[u] = Ki(d, r * n);
    }
  const _ = e * 4, c = new Uint8ClampedArray(_ * t);
  for (let u = 0; u < t; u++)
    for (let d = 0; d < e; d++) {
      let g = 0, p = 0, C = 0;
      for (let y = 0; y < s; y++)
        for (let w = 0; w < o; w++) {
          const Z = Math.cos(Math.PI * d * w / e) * Math.cos(Math.PI * u * y / t);
          let V = f[w + y * o];
          g += V[0] * Z, p += V[1] * Z, C += V[2] * Z;
        }
      let I = je(g), S = je(p), m = je(C);
      c[4 * d + 0 + u * _] = I, c[4 * d + 1 + u * _] = S, c[4 * d + 2 + u * _] = m, c[4 * d + 3 + u * _] = 255;
    }
  return c;
}, Qi = Ji, {
  SvelteComponent: xi,
  append: $i,
  attr: Ie,
  binding_callbacks: es,
  detach: ts,
  element: qt,
  init: ns,
  insert: ls,
  noop: St,
  safe_not_equal: is,
  set_style: ae
} = window.__gradio__svelte__internal, { onMount: ss } = window.__gradio__svelte__internal;
function os(l) {
  let e, t;
  return {
    c() {
      e = qt("div"), t = qt("canvas"), Ie(
        t,
        "width",
        /*resolutionX*/
        l[2]
      ), Ie(
        t,
        "height",
        /*resolutionY*/
        l[3]
      ), ae(t, "width", "100%"), ae(t, "height", "100%"), ae(
        e,
        "width",
        /*width*/
        l[0] + "px"
      ), ae(
        e,
        "height",
        /*height*/
        l[1] + "px"
      );
    },
    m(n, i) {
      ls(n, e, i), $i(e, t), l[7](t);
    },
    p(n, [i]) {
      i & /*resolutionX*/
      4 && Ie(
        t,
        "width",
        /*resolutionX*/
        n[2]
      ), i & /*resolutionY*/
      8 && Ie(
        t,
        "height",
        /*resolutionY*/
        n[3]
      ), i & /*width*/
      1 && ae(
        e,
        "width",
        /*width*/
        n[0] + "px"
      ), i & /*height*/
      2 && ae(
        e,
        "height",
        /*height*/
        n[1] + "px"
      );
    },
    i: St,
    o: St,
    d(n) {
      n && ts(e), l[7](null);
    }
  };
}
function as(l, e, t) {
  let { hash: n } = e, { width: i = 100 } = e, { height: s = 100 } = e, { resolutionX: o = 16 } = e, { resolutionY: a = 16 } = e, { punch: r = 1 } = e, f;
  ss(() => {
    if (n && f) {
      const c = Qi(n, o, a, r), u = f.getContext("2d"), d = u.createImageData(o, a);
      d.data.set(c), u.putImageData(d, 0, 0);
    }
  });
  function _(c) {
    es[c ? "unshift" : "push"](() => {
      f = c, t(4, f);
    });
  }
  return l.$$set = (c) => {
    "hash" in c && t(5, n = c.hash), "width" in c && t(0, i = c.width), "height" in c && t(1, s = c.height), "resolutionX" in c && t(2, o = c.resolutionX), "resolutionY" in c && t(3, a = c.resolutionY), "punch" in c && t(6, r = c.punch);
  }, [i, s, o, a, f, n, r, _];
}
class rs extends xi {
  constructor(e) {
    super(), ns(this, e, as, os, is, {
      hash: 5,
      width: 0,
      height: 1,
      resolutionX: 2,
      resolutionY: 3,
      punch: 6
    });
  }
}
const {
  SvelteComponent: fs,
  attr: X,
  binding_callbacks: _s,
  detach: cs,
  element: us,
  init: ds,
  insert: ms,
  noop: Mt,
  safe_not_equal: hs,
  set_style: re,
  src_url_equal: It
} = window.__gradio__svelte__internal, { onMount: gs, createEventDispatcher: bs } = window.__gradio__svelte__internal;
function ws(l) {
  let e, t;
  return {
    c() {
      e = us("img"), It(e.src, t = /*src*/
      l[0]) || X(e, "src", t), X(
        e,
        "alt",
        /*alt*/
        l[1]
      ), X(
        e,
        "width",
        /*width*/
        l[2]
      ), X(
        e,
        "height",
        /*height*/
        l[3]
      ), re(e, "position", "absolute"), re(e, "top", "0"), re(e, "left", "0"), re(e, "opacity", "0"), re(e, "transition", "opacity " + /*fadeDuration*/
      l[4] + "ms"), X(e, "loading", "lazy"), X(e, "decoding", "async");
    },
    m(n, i) {
      ms(n, e, i), l[6](e);
    },
    p(n, [i]) {
      i & /*src*/
      1 && !It(e.src, t = /*src*/
      n[0]) && X(e, "src", t), i & /*alt*/
      2 && X(
        e,
        "alt",
        /*alt*/
        n[1]
      ), i & /*width*/
      4 && X(
        e,
        "width",
        /*width*/
        n[2]
      ), i & /*height*/
      8 && X(
        e,
        "height",
        /*height*/
        n[3]
      ), i & /*fadeDuration*/
      16 && re(e, "transition", "opacity " + /*fadeDuration*/
      n[4] + "ms");
    },
    i: Mt,
    o: Mt,
    d(n) {
      n && cs(e), l[6](null);
    }
  };
}
function ps(l, e, t) {
  const n = bs();
  let { src: i } = e, { alt: s } = e, { width: o } = e, { height: a } = e, { fadeDuration: r = 500 } = e, f;
  gs(() => {
    t(
      5,
      f.onload = () => {
        t(5, f.style.opacity = 1, f), n("imageLoaded", { fadeDuration: r });
      },
      f
    );
  });
  function _(c) {
    _s[c ? "unshift" : "push"](() => {
      f = c, t(5, f);
    });
  }
  return l.$$set = (c) => {
    "src" in c && t(0, i = c.src), "alt" in c && t(1, s = c.alt), "width" in c && t(2, o = c.width), "height" in c && t(3, a = c.height), "fadeDuration" in c && t(4, r = c.fadeDuration);
  }, [i, s, o, a, r, f, _];
}
let vs = class extends fs {
  constructor(e) {
    super(), ds(this, e, ps, ws, hs, {
      src: 0,
      alt: 1,
      width: 2,
      height: 3,
      fadeDuration: 4
    });
  }
};
const {
  SvelteComponent: ks,
  append: ys,
  check_outros: hn,
  create_component: it,
  destroy_component: st,
  detach: ot,
  element: gn,
  empty: Cs,
  group_outros: bn,
  init: qs,
  insert: at,
  mount_component: rt,
  noop: Lt,
  safe_not_equal: Ss,
  set_style: qe,
  space: Ms,
  transition_in: ee,
  transition_out: se
} = window.__gradio__svelte__internal;
function zt(l) {
  let e, t, n, i, s, o;
  const a = [Ls, Is], r = [];
  function f(_, c) {
    return (
      /*isFadeIn*/
      _[6] ? 1 : 0
    );
  }
  return t = f(l), n = r[t] = a[t](l), s = new vs({
    props: {
      src: (
        /*src*/
        l[0]
      ),
      alt: (
        /*alt*/
        l[4]
      ),
      width: (
        /*width*/
        l[2]
      ),
      height: (
        /*height*/
        l[3]
      ),
      fadeDuration: (
        /*fadeDuration*/
        l[5]
      )
    }
  }), s.$on(
    "imageLoaded",
    /*onImageLoaded*/
    l[7]
  ), {
    c() {
      e = gn("div"), n.c(), i = Ms(), it(s.$$.fragment), qe(e, "position", "relative");
    },
    m(_, c) {
      at(_, e, c), r[t].m(e, null), ys(e, i), rt(s, e, null), o = !0;
    },
    p(_, c) {
      let u = t;
      t = f(_), t === u ? r[t].p(_, c) : (bn(), se(r[u], 1, 1, () => {
        r[u] = null;
      }), hn(), n = r[t], n ? n.p(_, c) : (n = r[t] = a[t](_), n.c()), ee(n, 1), n.m(e, i));
      const d = {};
      c & /*src*/
      1 && (d.src = /*src*/
      _[0]), c & /*alt*/
      16 && (d.alt = /*alt*/
      _[4]), c & /*width*/
      4 && (d.width = /*width*/
      _[2]), c & /*height*/
      8 && (d.height = /*height*/
      _[3]), c & /*fadeDuration*/
      32 && (d.fadeDuration = /*fadeDuration*/
      _[5]), s.$set(d);
    },
    i(_) {
      o || (ee(n), ee(s.$$.fragment, _), o = !0);
    },
    o(_) {
      se(n), se(s.$$.fragment, _), o = !1;
    },
    d(_) {
      _ && ot(e), r[t].d(), st(s);
    }
  };
}
function Is(l) {
  let e;
  return {
    c() {
      e = gn("div"), qe(
        e,
        "width",
        /*width*/
        l[2] + "px"
      ), qe(
        e,
        "height",
        /*height*/
        l[3] + "px"
      );
    },
    m(t, n) {
      at(t, e, n);
    },
    p(t, n) {
      n & /*width*/
      4 && qe(
        e,
        "width",
        /*width*/
        t[2] + "px"
      ), n & /*height*/
      8 && qe(
        e,
        "height",
        /*height*/
        t[3] + "px"
      );
    },
    i: Lt,
    o: Lt,
    d(t) {
      t && ot(e);
    }
  };
}
function Ls(l) {
  let e, t;
  return e = new rs({
    props: {
      hash: (
        /*hash*/
        l[1]
      ),
      width: (
        /*width*/
        l[2]
      ),
      height: (
        /*height*/
        l[3]
      )
    }
  }), {
    c() {
      it(e.$$.fragment);
    },
    m(n, i) {
      rt(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i & /*hash*/
      2 && (s.hash = /*hash*/
      n[1]), i & /*width*/
      4 && (s.width = /*width*/
      n[2]), i & /*height*/
      8 && (s.height = /*height*/
      n[3]), e.$set(s);
    },
    i(n) {
      t || (ee(e.$$.fragment, n), t = !0);
    },
    o(n) {
      se(e.$$.fragment, n), t = !1;
    },
    d(n) {
      st(e, n);
    }
  };
}
function zs(l) {
  let e, t, n = (
    /*hasBeenVisible*/
    l[9] && zt(l)
  );
  return {
    c() {
      n && n.c(), e = Cs();
    },
    m(i, s) {
      n && n.m(i, s), at(i, e, s), t = !0;
    },
    p(i, s) {
      /*hasBeenVisible*/
      i[9] ? n ? (n.p(i, s), s & /*hasBeenVisible*/
      512 && ee(n, 1)) : (n = zt(i), n.c(), ee(n, 1), n.m(e.parentNode, e)) : n && (bn(), se(n, 1, 1, () => {
        n = null;
      }), hn());
    },
    i(i) {
      t || (ee(n), t = !0);
    },
    o(i) {
      se(n), t = !1;
    },
    d(i) {
      i && ot(e), n && n.d(i);
    }
  };
}
function As(l) {
  let e, t;
  return e = new Ui({
    props: {
      $$slots: {
        default: [
          zs,
          ({ hasBeenVisible: n }) => ({ 9: n }),
          ({ hasBeenVisible: n }) => n ? 512 : 0
        ]
      },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      it(e.$$.fragment);
    },
    m(n, i) {
      rt(e, n, i), t = !0;
    },
    p(n, [i]) {
      const s = {};
      i & /*$$scope, src, alt, width, height, fadeDuration, hash, isFadeIn, hasBeenVisible*/
      1663 && (s.$$scope = { dirty: i, ctx: n }), e.$set(s);
    },
    i(n) {
      t || (ee(e.$$.fragment, n), t = !0);
    },
    o(n) {
      se(e.$$.fragment, n), t = !1;
    },
    d(n) {
      st(e, n);
    }
  };
}
function Bs(l, e, t) {
  let { src: n = "#" } = e, { hash: i } = e, { width: s } = e, { height: o } = e, { alt: a = "" } = e, { fadeDuration: r = 500 } = e, f = !1;
  function _(u) {
    setTimeout(c, u.detail.fadeDuration + 100);
  }
  function c() {
    t(6, f = !0);
  }
  return l.$$set = (u) => {
    "src" in u && t(0, n = u.src), "hash" in u && t(1, i = u.hash), "width" in u && t(2, s = u.width), "height" in u && t(3, o = u.height), "alt" in u && t(4, a = u.alt), "fadeDuration" in u && t(5, r = u.fadeDuration);
  }, [n, i, s, o, a, r, f, _];
}
class Fs extends ks {
  constructor(e) {
    super(), qs(this, e, Bs, As, Ss, {
      src: 0,
      hash: 1,
      width: 2,
      height: 3,
      alt: 4,
      fadeDuration: 5
    });
  }
}
const {
  SvelteComponent: Es,
  append: At,
  attr: le,
  bubble: Bt,
  check_outros: We,
  create_component: we,
  destroy_component: pe,
  detach: de,
  element: Fe,
  empty: Ds,
  group_outros: Ge,
  init: Rs,
  insert: me,
  listen: Vs,
  mount_component: ve,
  safe_not_equal: Ts,
  space: Ke,
  transition_in: B,
  transition_out: D
} = window.__gradio__svelte__internal, { createEventDispatcher: Ps } = window.__gradio__svelte__internal;
function Ns(l) {
  let e, t, n, i, s, o, a, r, f, _ = (
    /*show_download_button*/
    l[3] && Ft(l)
  ), c = (
    /*show_share_button*/
    l[4] && Et(l)
  );
  return o = new Fs({
    props: {
      src: (
        /*value*/
        l[0].image.url
      ),
      hash: (
        /*value*/
        l[0].blurhash
      ),
      width: (
        /*value*/
        l[0].width
      ),
      height: (
        /*value*/
        l[0].height
      )
    }
  }), {
    c() {
      e = Fe("div"), _ && _.c(), t = Ke(), c && c.c(), n = Ke(), i = Fe("button"), s = Fe("div"), we(o.$$.fragment), le(e, "class", "icon-buttons svelte-fz4vky"), le(s, "class", "image-wrapper svelte-fz4vky"), le(i, "class", "selectable svelte-fz4vky");
    },
    m(u, d) {
      me(u, e, d), _ && _.m(e, null), At(e, t), c && c.m(e, null), me(u, n, d), me(u, i, d), At(i, s), ve(o, s, null), a = !0, r || (f = Vs(
        i,
        "click",
        /*handle_click*/
        l[6]
      ), r = !0);
    },
    p(u, d) {
      /*show_download_button*/
      u[3] ? _ ? (_.p(u, d), d & /*show_download_button*/
      8 && B(_, 1)) : (_ = Ft(u), _.c(), B(_, 1), _.m(e, t)) : _ && (Ge(), D(_, 1, 1, () => {
        _ = null;
      }), We()), /*show_share_button*/
      u[4] ? c ? (c.p(u, d), d & /*show_share_button*/
      16 && B(c, 1)) : (c = Et(u), c.c(), B(c, 1), c.m(e, null)) : c && (Ge(), D(c, 1, 1, () => {
        c = null;
      }), We());
      const g = {};
      d & /*value*/
      1 && (g.src = /*value*/
      u[0].image.url), d & /*value*/
      1 && (g.hash = /*value*/
      u[0].blurhash), d & /*value*/
      1 && (g.width = /*value*/
      u[0].width), d & /*value*/
      1 && (g.height = /*value*/
      u[0].height), o.$set(g);
    },
    i(u) {
      a || (B(_), B(c), B(o.$$.fragment, u), a = !0);
    },
    o(u) {
      D(_), D(c), D(o.$$.fragment, u), a = !1;
    },
    d(u) {
      u && (de(e), de(n), de(i)), _ && _.d(), c && c.d(), pe(o), r = !1, f();
    }
  };
}
function Xs(l) {
  let e, t;
  return e = new Yl({
    props: {
      unpadded_box: !0,
      size: "large",
      $$slots: { default: [Ys] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      we(e.$$.fragment);
    },
    m(n, i) {
      ve(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i & /*$$scope*/
      4096 && (s.$$scope = { dirty: i, ctx: n }), e.$set(s);
    },
    i(n) {
      t || (B(e.$$.fragment, n), t = !0);
    },
    o(n) {
      D(e.$$.fragment, n), t = !1;
    },
    d(n) {
      pe(e, n);
    }
  };
}
function Ft(l) {
  let e, t, n, i;
  return t = new cn({
    props: {
      Icon: li,
      label: (
        /*i18n*/
        l[5]("common.download")
      )
    }
  }), {
    c() {
      e = Fe("a"), we(t.$$.fragment), le(e, "href", n = /*value*/
      l[0].image.url), le(e, "target", window.__is_colab__ ? "_blank" : null), le(e, "download", "image");
    },
    m(s, o) {
      me(s, e, o), ve(t, e, null), i = !0;
    },
    p(s, o) {
      const a = {};
      o & /*i18n*/
      32 && (a.label = /*i18n*/
      s[5]("common.download")), t.$set(a), (!i || o & /*value*/
      1 && n !== (n = /*value*/
      s[0].image.url)) && le(e, "href", n);
    },
    i(s) {
      i || (B(t.$$.fragment, s), i = !0);
    },
    o(s) {
      D(t.$$.fragment, s), i = !1;
    },
    d(s) {
      s && de(e), pe(t);
    }
  };
}
function Et(l) {
  let e, t;
  return e = new ki({
    props: {
      i18n: (
        /*i18n*/
        l[5]
      ),
      formatter: (
        /*func*/
        l[8]
      ),
      value: (
        /*value*/
        l[0]
      )
    }
  }), e.$on(
    "share",
    /*share_handler*/
    l[9]
  ), e.$on(
    "error",
    /*error_handler*/
    l[10]
  ), {
    c() {
      we(e.$$.fragment);
    },
    m(n, i) {
      ve(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i & /*i18n*/
      32 && (s.i18n = /*i18n*/
      n[5]), i & /*value*/
      1 && (s.value = /*value*/
      n[0]), e.$set(s);
    },
    i(n) {
      t || (B(e.$$.fragment, n), t = !0);
    },
    o(n) {
      D(e.$$.fragment, n), t = !1;
    },
    d(n) {
      pe(e, n);
    }
  };
}
function Ys(l) {
  let e, t;
  return e = new un({}), {
    c() {
      we(e.$$.fragment);
    },
    m(n, i) {
      ve(e, n, i), t = !0;
    },
    i(n) {
      t || (B(e.$$.fragment, n), t = !0);
    },
    o(n) {
      D(e.$$.fragment, n), t = !1;
    },
    d(n) {
      pe(e, n);
    }
  };
}
function js(l) {
  let e, t, n, i, s, o;
  e = new fl({
    props: {
      show_label: (
        /*show_label*/
        l[2]
      ),
      Icon: un,
      label: (
        /*label*/
        l[1] || /*i18n*/
        l[5]("image.image")
      )
    }
  });
  const a = [Xs, Ns], r = [];
  function f(_, c) {
    return (
      /*value*/
      _[0] === null || /*value*/
      _[0].image === null || !/*value*/
      _[0].image.url ? 0 : 1
    );
  }
  return n = f(l), i = r[n] = a[n](l), {
    c() {
      we(e.$$.fragment), t = Ke(), i.c(), s = Ds();
    },
    m(_, c) {
      ve(e, _, c), me(_, t, c), r[n].m(_, c), me(_, s, c), o = !0;
    },
    p(_, [c]) {
      const u = {};
      c & /*show_label*/
      4 && (u.show_label = /*show_label*/
      _[2]), c & /*label, i18n*/
      34 && (u.label = /*label*/
      _[1] || /*i18n*/
      _[5]("image.image")), e.$set(u);
      let d = n;
      n = f(_), n === d ? r[n].p(_, c) : (Ge(), D(r[d], 1, 1, () => {
        r[d] = null;
      }), We(), i = r[n], i ? i.p(_, c) : (i = r[n] = a[n](_), i.c()), B(i, 1), i.m(s.parentNode, s));
    },
    i(_) {
      o || (B(e.$$.fragment, _), B(i), o = !0);
    },
    o(_) {
      D(e.$$.fragment, _), D(i), o = !1;
    },
    d(_) {
      _ && (de(t), de(s)), pe(e, _), r[n].d(_);
    }
  };
}
function Zs(l, e, t) {
  let { value: n } = e, { label: i = void 0 } = e, { show_label: s } = e, { show_download_button: o = !0 } = e, { show_share_button: a = !1 } = e, { root: r } = e, { i18n: f } = e;
  const _ = Ps(), c = (p) => {
    let C = yi(p);
    C && _("select", { index: C, value: null });
  }, u = async (p) => p ? `<img src="${await An(p, "base64")}" />` : "";
  function d(p) {
    Bt.call(this, l, p);
  }
  function g(p) {
    Bt.call(this, l, p);
  }
  return l.$$set = (p) => {
    "value" in p && t(0, n = p.value), "label" in p && t(1, i = p.label), "show_label" in p && t(2, s = p.show_label), "show_download_button" in p && t(3, o = p.show_download_button), "show_share_button" in p && t(4, a = p.show_share_button), "root" in p && t(7, r = p.root), "i18n" in p && t(5, f = p.i18n);
  }, l.$$.update = () => {
    l.$$.dirty & /*value, root*/
    129 && t(0, n = mn(n, r));
  }, [
    n,
    i,
    s,
    o,
    a,
    f,
    c,
    r,
    u,
    d,
    g
  ];
}
class Us extends Es {
  constructor(e) {
    super(), Rs(this, e, Zs, js, Ts, {
      value: 0,
      label: 1,
      show_label: 2,
      show_download_button: 3,
      show_share_button: 4,
      root: 7,
      i18n: 5
    });
  }
}
function ce(l) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; l > 1e3 && t < e.length - 1; )
    l /= 1e3, t++;
  let n = e[t];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
function Ee() {
}
function Os(l, e) {
  return l != l ? e == e : l !== e || l && typeof l == "object" || typeof l == "function";
}
const wn = typeof window < "u";
let Dt = wn ? () => window.performance.now() : () => Date.now(), pn = wn ? (l) => requestAnimationFrame(l) : Ee;
const he = /* @__PURE__ */ new Set();
function vn(l) {
  he.forEach((e) => {
    e.c(l) || (he.delete(e), e.f());
  }), he.size !== 0 && pn(vn);
}
function Hs(l) {
  let e;
  return he.size === 0 && pn(vn), {
    promise: new Promise((t) => {
      he.add(e = { c: l, f: t });
    }),
    abort() {
      he.delete(e);
    }
  };
}
const fe = [];
function Ws(l, e = Ee) {
  let t;
  const n = /* @__PURE__ */ new Set();
  function i(a) {
    if (Os(l, a) && (l = a, t)) {
      const r = !fe.length;
      for (const f of n)
        f[1](), fe.push(f, l);
      if (r) {
        for (let f = 0; f < fe.length; f += 2)
          fe[f][0](fe[f + 1]);
        fe.length = 0;
      }
    }
  }
  function s(a) {
    i(a(l));
  }
  function o(a, r = Ee) {
    const f = [a, r];
    return n.add(f), n.size === 1 && (t = e(i, s) || Ee), a(l), () => {
      n.delete(f), n.size === 0 && t && (t(), t = null);
    };
  }
  return { set: i, update: s, subscribe: o };
}
function Rt(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function Je(l, e, t, n) {
  if (typeof t == "number" || Rt(t)) {
    const i = n - t, s = (t - e) / (l.dt || 1 / 60), o = l.opts.stiffness * i, a = l.opts.damping * s, r = (o - a) * l.inv_mass, f = (s + r) * l.dt;
    return Math.abs(f) < l.opts.precision && Math.abs(i) < l.opts.precision ? n : (l.settled = !1, Rt(t) ? new Date(t.getTime() + f) : t + f);
  } else {
    if (Array.isArray(t))
      return t.map(
        (i, s) => Je(l, e[s], t[s], n[s])
      );
    if (typeof t == "object") {
      const i = {};
      for (const s in t)
        i[s] = Je(l, e[s], t[s], n[s]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function Vt(l, e = {}) {
  const t = Ws(l), { stiffness: n = 0.15, damping: i = 0.8, precision: s = 0.01 } = e;
  let o, a, r, f = l, _ = l, c = 1, u = 0, d = !1;
  function g(C, I = {}) {
    _ = C;
    const S = r = {};
    return l == null || I.hard || p.stiffness >= 1 && p.damping >= 1 ? (d = !0, o = Dt(), f = C, t.set(l = _), Promise.resolve()) : (I.soft && (u = 1 / ((I.soft === !0 ? 0.5 : +I.soft) * 60), c = 0), a || (o = Dt(), d = !1, a = Hs((m) => {
      if (d)
        return d = !1, a = null, !1;
      c = Math.min(c + u, 1);
      const y = {
        inv_mass: c,
        opts: p,
        settled: !0,
        dt: (m - o) * 60 / 1e3
      }, w = Je(y, f, l, _);
      return o = m, f = l, t.set(l = w), y.settled && (a = null), !y.settled;
    })), new Promise((m) => {
      a.promise.then(() => {
        S === r && m();
      });
    }));
  }
  const p = {
    set: g,
    update: (C, I) => g(C(_, l), I),
    subscribe: t.subscribe,
    stiffness: n,
    damping: i,
    precision: s
  };
  return p;
}
const {
  SvelteComponent: Gs,
  append: T,
  attr: q,
  component_subscribe: Tt,
  detach: Ks,
  element: Js,
  init: Qs,
  insert: xs,
  noop: Pt,
  safe_not_equal: $s,
  set_style: Le,
  svg_element: P,
  toggle_class: Nt
} = window.__gradio__svelte__internal, { onMount: eo } = window.__gradio__svelte__internal;
function to(l) {
  let e, t, n, i, s, o, a, r, f, _, c, u;
  return {
    c() {
      e = Js("div"), t = P("svg"), n = P("g"), i = P("path"), s = P("path"), o = P("path"), a = P("path"), r = P("g"), f = P("path"), _ = P("path"), c = P("path"), u = P("path"), q(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), q(i, "fill", "#FF7C00"), q(i, "fill-opacity", "0.4"), q(i, "class", "svelte-43sxxs"), q(s, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), q(s, "fill", "#FF7C00"), q(s, "class", "svelte-43sxxs"), q(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), q(o, "fill", "#FF7C00"), q(o, "fill-opacity", "0.4"), q(o, "class", "svelte-43sxxs"), q(a, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), q(a, "fill", "#FF7C00"), q(a, "class", "svelte-43sxxs"), Le(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), q(f, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), q(f, "fill", "#FF7C00"), q(f, "fill-opacity", "0.4"), q(f, "class", "svelte-43sxxs"), q(_, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), q(_, "fill", "#FF7C00"), q(_, "class", "svelte-43sxxs"), q(c, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), q(c, "fill", "#FF7C00"), q(c, "fill-opacity", "0.4"), q(c, "class", "svelte-43sxxs"), q(u, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), q(u, "fill", "#FF7C00"), q(u, "class", "svelte-43sxxs"), Le(r, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), q(t, "viewBox", "-1200 -1200 3000 3000"), q(t, "fill", "none"), q(t, "xmlns", "http://www.w3.org/2000/svg"), q(t, "class", "svelte-43sxxs"), q(e, "class", "svelte-43sxxs"), Nt(
        e,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(d, g) {
      xs(d, e, g), T(e, t), T(t, n), T(n, i), T(n, s), T(n, o), T(n, a), T(t, r), T(r, f), T(r, _), T(r, c), T(r, u);
    },
    p(d, [g]) {
      g & /*$top*/
      2 && Le(n, "transform", "translate(" + /*$top*/
      d[1][0] + "px, " + /*$top*/
      d[1][1] + "px)"), g & /*$bottom*/
      4 && Le(r, "transform", "translate(" + /*$bottom*/
      d[2][0] + "px, " + /*$bottom*/
      d[2][1] + "px)"), g & /*margin*/
      1 && Nt(
        e,
        "margin",
        /*margin*/
        d[0]
      );
    },
    i: Pt,
    o: Pt,
    d(d) {
      d && Ks(e);
    }
  };
}
function no(l, e, t) {
  let n, i, { margin: s = !0 } = e;
  const o = Vt([0, 0]);
  Tt(l, o, (u) => t(1, n = u));
  const a = Vt([0, 0]);
  Tt(l, a, (u) => t(2, i = u));
  let r;
  async function f() {
    await Promise.all([o.set([125, 140]), a.set([-125, -140])]), await Promise.all([o.set([-125, 140]), a.set([125, -140])]), await Promise.all([o.set([-125, 0]), a.set([125, -0])]), await Promise.all([o.set([125, 0]), a.set([-125, 0])]);
  }
  async function _() {
    await f(), r || _();
  }
  async function c() {
    await Promise.all([o.set([125, 0]), a.set([-125, 0])]), _();
  }
  return eo(() => (c(), () => r = !0)), l.$$set = (u) => {
    "margin" in u && t(0, s = u.margin);
  }, [s, n, i, o, a];
}
class lo extends Gs {
  constructor(e) {
    super(), Qs(this, e, no, to, $s, { margin: 0 });
  }
}
const {
  SvelteComponent: io,
  append: ie,
  attr: Y,
  binding_callbacks: Xt,
  check_outros: kn,
  create_component: so,
  create_slot: oo,
  destroy_component: ao,
  destroy_each: yn,
  detach: v,
  element: O,
  empty: ke,
  ensure_array_like: De,
  get_all_dirty_from_scope: ro,
  get_slot_changes: fo,
  group_outros: Cn,
  init: _o,
  insert: k,
  mount_component: co,
  noop: Qe,
  safe_not_equal: uo,
  set_data: R,
  set_style: $,
  space: j,
  text: M,
  toggle_class: E,
  transition_in: ge,
  transition_out: be,
  update_slot_base: mo
} = window.__gradio__svelte__internal, { tick: ho } = window.__gradio__svelte__internal, { onDestroy: go } = window.__gradio__svelte__internal, bo = (l) => ({}), Yt = (l) => ({});
function jt(l, e, t) {
  const n = l.slice();
  return n[38] = e[t], n[40] = t, n;
}
function Zt(l, e, t) {
  const n = l.slice();
  return n[38] = e[t], n;
}
function wo(l) {
  let e, t = (
    /*i18n*/
    l[1]("common.error") + ""
  ), n, i, s;
  const o = (
    /*#slots*/
    l[29].error
  ), a = oo(
    o,
    l,
    /*$$scope*/
    l[28],
    Yt
  );
  return {
    c() {
      e = O("span"), n = M(t), i = j(), a && a.c(), Y(e, "class", "error svelte-14miwb5");
    },
    m(r, f) {
      k(r, e, f), ie(e, n), k(r, i, f), a && a.m(r, f), s = !0;
    },
    p(r, f) {
      (!s || f[0] & /*i18n*/
      2) && t !== (t = /*i18n*/
      r[1]("common.error") + "") && R(n, t), a && a.p && (!s || f[0] & /*$$scope*/
      268435456) && mo(
        a,
        o,
        r,
        /*$$scope*/
        r[28],
        s ? fo(
          o,
          /*$$scope*/
          r[28],
          f,
          bo
        ) : ro(
          /*$$scope*/
          r[28]
        ),
        Yt
      );
    },
    i(r) {
      s || (ge(a, r), s = !0);
    },
    o(r) {
      be(a, r), s = !1;
    },
    d(r) {
      r && (v(e), v(i)), a && a.d(r);
    }
  };
}
function po(l) {
  let e, t, n, i, s, o, a, r, f, _ = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && Ut(l)
  );
  function c(m, y) {
    if (
      /*progress*/
      m[7]
    )
      return yo;
    if (
      /*queue_position*/
      m[2] !== null && /*queue_size*/
      m[3] !== void 0 && /*queue_position*/
      m[2] >= 0
    )
      return ko;
    if (
      /*queue_position*/
      m[2] === 0
    )
      return vo;
  }
  let u = c(l), d = u && u(l), g = (
    /*timer*/
    l[5] && Wt(l)
  );
  const p = [Mo, So], C = [];
  function I(m, y) {
    return (
      /*last_progress_level*/
      m[15] != null ? 0 : (
        /*show_progress*/
        m[6] === "full" ? 1 : -1
      )
    );
  }
  ~(s = I(l)) && (o = C[s] = p[s](l));
  let S = !/*timer*/
  l[5] && en(l);
  return {
    c() {
      _ && _.c(), e = j(), t = O("div"), d && d.c(), n = j(), g && g.c(), i = j(), o && o.c(), a = j(), S && S.c(), r = ke(), Y(t, "class", "progress-text svelte-14miwb5"), E(
        t,
        "meta-text-center",
        /*variant*/
        l[8] === "center"
      ), E(
        t,
        "meta-text",
        /*variant*/
        l[8] === "default"
      );
    },
    m(m, y) {
      _ && _.m(m, y), k(m, e, y), k(m, t, y), d && d.m(t, null), ie(t, n), g && g.m(t, null), k(m, i, y), ~s && C[s].m(m, y), k(m, a, y), S && S.m(m, y), k(m, r, y), f = !0;
    },
    p(m, y) {
      /*variant*/
      m[8] === "default" && /*show_eta_bar*/
      m[18] && /*show_progress*/
      m[6] === "full" ? _ ? _.p(m, y) : (_ = Ut(m), _.c(), _.m(e.parentNode, e)) : _ && (_.d(1), _ = null), u === (u = c(m)) && d ? d.p(m, y) : (d && d.d(1), d = u && u(m), d && (d.c(), d.m(t, n))), /*timer*/
      m[5] ? g ? g.p(m, y) : (g = Wt(m), g.c(), g.m(t, null)) : g && (g.d(1), g = null), (!f || y[0] & /*variant*/
      256) && E(
        t,
        "meta-text-center",
        /*variant*/
        m[8] === "center"
      ), (!f || y[0] & /*variant*/
      256) && E(
        t,
        "meta-text",
        /*variant*/
        m[8] === "default"
      );
      let w = s;
      s = I(m), s === w ? ~s && C[s].p(m, y) : (o && (Cn(), be(C[w], 1, 1, () => {
        C[w] = null;
      }), kn()), ~s ? (o = C[s], o ? o.p(m, y) : (o = C[s] = p[s](m), o.c()), ge(o, 1), o.m(a.parentNode, a)) : o = null), /*timer*/
      m[5] ? S && (S.d(1), S = null) : S ? S.p(m, y) : (S = en(m), S.c(), S.m(r.parentNode, r));
    },
    i(m) {
      f || (ge(o), f = !0);
    },
    o(m) {
      be(o), f = !1;
    },
    d(m) {
      m && (v(e), v(t), v(i), v(a), v(r)), _ && _.d(m), d && d.d(), g && g.d(), ~s && C[s].d(m), S && S.d(m);
    }
  };
}
function Ut(l) {
  let e, t = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = O("div"), Y(e, "class", "eta-bar svelte-14miwb5"), $(e, "transform", t);
    },
    m(n, i) {
      k(n, e, i);
    },
    p(n, i) {
      i[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && $(e, "transform", t);
    },
    d(n) {
      n && v(e);
    }
  };
}
function vo(l) {
  let e;
  return {
    c() {
      e = M("processing |");
    },
    m(t, n) {
      k(t, e, n);
    },
    p: Qe,
    d(t) {
      t && v(e);
    }
  };
}
function ko(l) {
  let e, t = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, i, s, o;
  return {
    c() {
      e = M("queue: "), n = M(t), i = M("/"), s = M(
        /*queue_size*/
        l[3]
      ), o = M(" |");
    },
    m(a, r) {
      k(a, e, r), k(a, n, r), k(a, i, r), k(a, s, r), k(a, o, r);
    },
    p(a, r) {
      r[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      a[2] + 1 + "") && R(n, t), r[0] & /*queue_size*/
      8 && R(
        s,
        /*queue_size*/
        a[3]
      );
    },
    d(a) {
      a && (v(e), v(n), v(i), v(s), v(o));
    }
  };
}
function yo(l) {
  let e, t = De(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = Ht(Zt(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = ke();
    },
    m(i, s) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, s);
      k(i, e, s);
    },
    p(i, s) {
      if (s[0] & /*progress*/
      128) {
        t = De(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const a = Zt(i, t, o);
          n[o] ? n[o].p(a, s) : (n[o] = Ht(a), n[o].c(), n[o].m(e.parentNode, e));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && v(e), yn(n, i);
    }
  };
}
function Ot(l) {
  let e, t = (
    /*p*/
    l[38].unit + ""
  ), n, i, s = " ", o;
  function a(_, c) {
    return (
      /*p*/
      _[38].length != null ? qo : Co
    );
  }
  let r = a(l), f = r(l);
  return {
    c() {
      f.c(), e = j(), n = M(t), i = M(" | "), o = M(s);
    },
    m(_, c) {
      f.m(_, c), k(_, e, c), k(_, n, c), k(_, i, c), k(_, o, c);
    },
    p(_, c) {
      r === (r = a(_)) && f ? f.p(_, c) : (f.d(1), f = r(_), f && (f.c(), f.m(e.parentNode, e))), c[0] & /*progress*/
      128 && t !== (t = /*p*/
      _[38].unit + "") && R(n, t);
    },
    d(_) {
      _ && (v(e), v(n), v(i), v(o)), f.d(_);
    }
  };
}
function Co(l) {
  let e = ce(
    /*p*/
    l[38].index || 0
  ) + "", t;
  return {
    c() {
      t = M(e);
    },
    m(n, i) {
      k(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = ce(
        /*p*/
        n[38].index || 0
      ) + "") && R(t, e);
    },
    d(n) {
      n && v(t);
    }
  };
}
function qo(l) {
  let e = ce(
    /*p*/
    l[38].index || 0
  ) + "", t, n, i = ce(
    /*p*/
    l[38].length
  ) + "", s;
  return {
    c() {
      t = M(e), n = M("/"), s = M(i);
    },
    m(o, a) {
      k(o, t, a), k(o, n, a), k(o, s, a);
    },
    p(o, a) {
      a[0] & /*progress*/
      128 && e !== (e = ce(
        /*p*/
        o[38].index || 0
      ) + "") && R(t, e), a[0] & /*progress*/
      128 && i !== (i = ce(
        /*p*/
        o[38].length
      ) + "") && R(s, i);
    },
    d(o) {
      o && (v(t), v(n), v(s));
    }
  };
}
function Ht(l) {
  let e, t = (
    /*p*/
    l[38].index != null && Ot(l)
  );
  return {
    c() {
      t && t.c(), e = ke();
    },
    m(n, i) {
      t && t.m(n, i), k(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[38].index != null ? t ? t.p(n, i) : (t = Ot(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && v(e), t && t.d(n);
    }
  };
}
function Wt(l) {
  let e, t = (
    /*eta*/
    l[0] ? `/${/*formatted_eta*/
    l[19]}` : ""
  ), n, i;
  return {
    c() {
      e = M(
        /*formatted_timer*/
        l[20]
      ), n = M(t), i = M("s");
    },
    m(s, o) {
      k(s, e, o), k(s, n, o), k(s, i, o);
    },
    p(s, o) {
      o[0] & /*formatted_timer*/
      1048576 && R(
        e,
        /*formatted_timer*/
        s[20]
      ), o[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      s[0] ? `/${/*formatted_eta*/
      s[19]}` : "") && R(n, t);
    },
    d(s) {
      s && (v(e), v(n), v(i));
    }
  };
}
function So(l) {
  let e, t;
  return e = new lo({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      so(e.$$.fragment);
    },
    m(n, i) {
      co(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i[0] & /*variant*/
      256 && (s.margin = /*variant*/
      n[8] === "default"), e.$set(s);
    },
    i(n) {
      t || (ge(e.$$.fragment, n), t = !0);
    },
    o(n) {
      be(e.$$.fragment, n), t = !1;
    },
    d(n) {
      ao(e, n);
    }
  };
}
function Mo(l) {
  let e, t, n, i, s, o = `${/*last_progress_level*/
  l[15] * 100}%`, a = (
    /*progress*/
    l[7] != null && Gt(l)
  );
  return {
    c() {
      e = O("div"), t = O("div"), a && a.c(), n = j(), i = O("div"), s = O("div"), Y(t, "class", "progress-level-inner svelte-14miwb5"), Y(s, "class", "progress-bar svelte-14miwb5"), $(s, "width", o), Y(i, "class", "progress-bar-wrap svelte-14miwb5"), Y(e, "class", "progress-level svelte-14miwb5");
    },
    m(r, f) {
      k(r, e, f), ie(e, t), a && a.m(t, null), ie(e, n), ie(e, i), ie(i, s), l[30](s);
    },
    p(r, f) {
      /*progress*/
      r[7] != null ? a ? a.p(r, f) : (a = Gt(r), a.c(), a.m(t, null)) : a && (a.d(1), a = null), f[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      r[15] * 100}%`) && $(s, "width", o);
    },
    i: Qe,
    o: Qe,
    d(r) {
      r && v(e), a && a.d(), l[30](null);
    }
  };
}
function Gt(l) {
  let e, t = De(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = $t(jt(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = ke();
    },
    m(i, s) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, s);
      k(i, e, s);
    },
    p(i, s) {
      if (s[0] & /*progress_level, progress*/
      16512) {
        t = De(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const a = jt(i, t, o);
          n[o] ? n[o].p(a, s) : (n[o] = $t(a), n[o].c(), n[o].m(e.parentNode, e));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && v(e), yn(n, i);
    }
  };
}
function Kt(l) {
  let e, t, n, i, s = (
    /*i*/
    l[40] !== 0 && Io()
  ), o = (
    /*p*/
    l[38].desc != null && Jt(l)
  ), a = (
    /*p*/
    l[38].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[40]
    ] != null && Qt()
  ), r = (
    /*progress_level*/
    l[14] != null && xt(l)
  );
  return {
    c() {
      s && s.c(), e = j(), o && o.c(), t = j(), a && a.c(), n = j(), r && r.c(), i = ke();
    },
    m(f, _) {
      s && s.m(f, _), k(f, e, _), o && o.m(f, _), k(f, t, _), a && a.m(f, _), k(f, n, _), r && r.m(f, _), k(f, i, _);
    },
    p(f, _) {
      /*p*/
      f[38].desc != null ? o ? o.p(f, _) : (o = Jt(f), o.c(), o.m(t.parentNode, t)) : o && (o.d(1), o = null), /*p*/
      f[38].desc != null && /*progress_level*/
      f[14] && /*progress_level*/
      f[14][
        /*i*/
        f[40]
      ] != null ? a || (a = Qt(), a.c(), a.m(n.parentNode, n)) : a && (a.d(1), a = null), /*progress_level*/
      f[14] != null ? r ? r.p(f, _) : (r = xt(f), r.c(), r.m(i.parentNode, i)) : r && (r.d(1), r = null);
    },
    d(f) {
      f && (v(e), v(t), v(n), v(i)), s && s.d(f), o && o.d(f), a && a.d(f), r && r.d(f);
    }
  };
}
function Io(l) {
  let e;
  return {
    c() {
      e = M(" /");
    },
    m(t, n) {
      k(t, e, n);
    },
    d(t) {
      t && v(e);
    }
  };
}
function Jt(l) {
  let e = (
    /*p*/
    l[38].desc + ""
  ), t;
  return {
    c() {
      t = M(e);
    },
    m(n, i) {
      k(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = /*p*/
      n[38].desc + "") && R(t, e);
    },
    d(n) {
      n && v(t);
    }
  };
}
function Qt(l) {
  let e;
  return {
    c() {
      e = M("-");
    },
    m(t, n) {
      k(t, e, n);
    },
    d(t) {
      t && v(e);
    }
  };
}
function xt(l) {
  let e = (100 * /*progress_level*/
  (l[14][
    /*i*/
    l[40]
  ] || 0)).toFixed(1) + "", t, n;
  return {
    c() {
      t = M(e), n = M("%");
    },
    m(i, s) {
      k(i, t, s), k(i, n, s);
    },
    p(i, s) {
      s[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[40]
      ] || 0)).toFixed(1) + "") && R(t, e);
    },
    d(i) {
      i && (v(t), v(n));
    }
  };
}
function $t(l) {
  let e, t = (
    /*p*/
    (l[38].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[40]
    ] != null) && Kt(l)
  );
  return {
    c() {
      t && t.c(), e = ke();
    },
    m(n, i) {
      t && t.m(n, i), k(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[38].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[40]
      ] != null ? t ? t.p(n, i) : (t = Kt(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && v(e), t && t.d(n);
    }
  };
}
function en(l) {
  let e, t;
  return {
    c() {
      e = O("p"), t = M(
        /*loading_text*/
        l[9]
      ), Y(e, "class", "loading svelte-14miwb5");
    },
    m(n, i) {
      k(n, e, i), ie(e, t);
    },
    p(n, i) {
      i[0] & /*loading_text*/
      512 && R(
        t,
        /*loading_text*/
        n[9]
      );
    },
    d(n) {
      n && v(e);
    }
  };
}
function Lo(l) {
  let e, t, n, i, s;
  const o = [po, wo], a = [];
  function r(f, _) {
    return (
      /*status*/
      f[4] === "pending" ? 0 : (
        /*status*/
        f[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = r(l)) && (n = a[t] = o[t](l)), {
    c() {
      e = O("div"), n && n.c(), Y(e, "class", i = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-14miwb5"), E(e, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), E(
        e,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), E(
        e,
        "generating",
        /*status*/
        l[4] === "generating"
      ), E(
        e,
        "border",
        /*border*/
        l[12]
      ), $(
        e,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), $(
        e,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(f, _) {
      k(f, e, _), ~t && a[t].m(e, null), l[31](e), s = !0;
    },
    p(f, _) {
      let c = t;
      t = r(f), t === c ? ~t && a[t].p(f, _) : (n && (Cn(), be(a[c], 1, 1, () => {
        a[c] = null;
      }), kn()), ~t ? (n = a[t], n ? n.p(f, _) : (n = a[t] = o[t](f), n.c()), ge(n, 1), n.m(e, null)) : n = null), (!s || _[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      f[8] + " " + /*show_progress*/
      f[6] + " svelte-14miwb5")) && Y(e, "class", i), (!s || _[0] & /*variant, show_progress, status, show_progress*/
      336) && E(e, "hide", !/*status*/
      f[4] || /*status*/
      f[4] === "complete" || /*show_progress*/
      f[6] === "hidden"), (!s || _[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && E(
        e,
        "translucent",
        /*variant*/
        f[8] === "center" && /*status*/
        (f[4] === "pending" || /*status*/
        f[4] === "error") || /*translucent*/
        f[11] || /*show_progress*/
        f[6] === "minimal"
      ), (!s || _[0] & /*variant, show_progress, status*/
      336) && E(
        e,
        "generating",
        /*status*/
        f[4] === "generating"
      ), (!s || _[0] & /*variant, show_progress, border*/
      4416) && E(
        e,
        "border",
        /*border*/
        f[12]
      ), _[0] & /*absolute*/
      1024 && $(
        e,
        "position",
        /*absolute*/
        f[10] ? "absolute" : "static"
      ), _[0] & /*absolute*/
      1024 && $(
        e,
        "padding",
        /*absolute*/
        f[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(f) {
      s || (ge(n), s = !0);
    },
    o(f) {
      be(n), s = !1;
    },
    d(f) {
      f && v(e), ~t && a[t].d(), l[31](null);
    }
  };
}
let ze = [], Ue = !1;
async function zo(l, e = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && e !== !0)) {
    if (ze.push(l), !Ue)
      Ue = !0;
    else
      return;
    await ho(), requestAnimationFrame(() => {
      let t = [0, 0];
      for (let n = 0; n < ze.length; n++) {
        const s = ze[n].getBoundingClientRect();
        (n === 0 || s.top + window.scrollY <= t[0]) && (t[0] = s.top + window.scrollY, t[1] = n);
      }
      window.scrollTo({ top: t[0] - 20, behavior: "smooth" }), Ue = !1, ze = [];
    });
  }
}
function Ao(l, e, t) {
  let n, { $$slots: i = {}, $$scope: s } = e, { i18n: o } = e, { eta: a = null } = e, { queue: r = !1 } = e, { queue_position: f } = e, { queue_size: _ } = e, { status: c } = e, { scroll_to_output: u = !1 } = e, { timer: d = !0 } = e, { show_progress: g = "full" } = e, { message: p = null } = e, { progress: C = null } = e, { variant: I = "default" } = e, { loading_text: S = "Loading..." } = e, { absolute: m = !0 } = e, { translucent: y = !1 } = e, { border: w = !1 } = e, { autoscroll: Z } = e, V, h = !1, H = 0, A = 0, W = null, U = 0, N = null, te, G = null, ct = !0;
  const Sn = () => {
    t(25, H = performance.now()), t(26, A = 0), h = !0, ut();
  };
  function ut() {
    requestAnimationFrame(() => {
      t(26, A = (performance.now() - H) / 1e3), h && ut();
    });
  }
  function dt() {
    t(26, A = 0), h && (h = !1);
  }
  go(() => {
    h && dt();
  });
  let mt = null;
  function Mn(b) {
    Xt[b ? "unshift" : "push"](() => {
      G = b, t(16, G), t(7, C), t(14, N), t(15, te);
    });
  }
  function In(b) {
    Xt[b ? "unshift" : "push"](() => {
      V = b, t(13, V);
    });
  }
  return l.$$set = (b) => {
    "i18n" in b && t(1, o = b.i18n), "eta" in b && t(0, a = b.eta), "queue" in b && t(21, r = b.queue), "queue_position" in b && t(2, f = b.queue_position), "queue_size" in b && t(3, _ = b.queue_size), "status" in b && t(4, c = b.status), "scroll_to_output" in b && t(22, u = b.scroll_to_output), "timer" in b && t(5, d = b.timer), "show_progress" in b && t(6, g = b.show_progress), "message" in b && t(23, p = b.message), "progress" in b && t(7, C = b.progress), "variant" in b && t(8, I = b.variant), "loading_text" in b && t(9, S = b.loading_text), "absolute" in b && t(10, m = b.absolute), "translucent" in b && t(11, y = b.translucent), "border" in b && t(12, w = b.border), "autoscroll" in b && t(24, Z = b.autoscroll), "$$scope" in b && t(28, s = b.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, queue, timer_start*/
    169869313 && (a === null ? t(0, a = W) : r && t(0, a = (performance.now() - H) / 1e3 + a), a != null && (t(19, mt = a.toFixed(1)), t(27, W = a))), l.$$.dirty[0] & /*eta, timer_diff*/
    67108865 && t(17, U = a === null || a <= 0 || !A ? null : Math.min(A / a, 1)), l.$$.dirty[0] & /*progress*/
    128 && C != null && t(18, ct = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (C != null ? t(14, N = C.map((b) => {
      if (b.index != null && b.length != null)
        return b.index / b.length;
      if (b.progress != null)
        return b.progress;
    })) : t(14, N = null), N ? (t(15, te = N[N.length - 1]), G && (te === 0 ? t(16, G.style.transition = "0", G) : t(16, G.style.transition = "150ms", G))) : t(15, te = void 0)), l.$$.dirty[0] & /*status*/
    16 && (c === "pending" ? Sn() : dt()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && V && u && (c === "pending" || c === "complete") && zo(V, Z), l.$$.dirty[0] & /*status, message*/
    8388624, l.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, n = A.toFixed(1));
  }, [
    a,
    o,
    f,
    _,
    c,
    d,
    g,
    C,
    I,
    S,
    m,
    y,
    w,
    V,
    N,
    te,
    G,
    U,
    ct,
    mt,
    n,
    r,
    u,
    p,
    Z,
    H,
    A,
    W,
    s,
    i,
    Mn,
    In
  ];
}
class Bo extends io {
  constructor(e) {
    super(), _o(
      this,
      e,
      Ao,
      Lo,
      uo,
      {
        i18n: 1,
        eta: 0,
        queue: 21,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 22,
        timer: 5,
        show_progress: 6,
        message: 23,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 24
      },
      null,
      [-1, -1]
    );
  }
}
const { setContext: La, getContext: Fo } = window.__gradio__svelte__internal, Eo = "WORKER_PROXY_CONTEXT_KEY";
function Do() {
  return Fo(Eo);
}
function Ro(l) {
  return l.host === window.location.host || l.host === "localhost:7860" || l.host === "127.0.0.1:7860" || // Ref: https://github.com/gradio-app/gradio/blob/v3.32.0/js/app/src/Index.svelte#L194
  l.host === "lite.local";
}
async function tn(l) {
  if (l == null)
    return l;
  const e = new URL(l);
  if (!Ro(e) || e.protocol !== "http:" && e.protocol !== "https:")
    return l;
  const t = Do();
  if (t == null)
    return l;
  const n = e.pathname;
  return t.httpRequest({
    method: "GET",
    path: n,
    headers: {},
    query_string: ""
  }).then((i) => {
    if (i.status !== 200)
      throw new Error(`Failed to get file ${n} from the Wasm worker.`);
    const s = new Blob([i.body], {
      type: i.headers["Content-Type"]
    });
    return URL.createObjectURL(s);
  });
}
const {
  SvelteComponent: Vo,
  append: To,
  assign: xe,
  compute_rest_props: nn,
  detach: ft,
  element: qn,
  empty: Po,
  exclude_internal_props: No,
  get_spread_update: Xo,
  handle_promise: ln,
  init: Yo,
  insert: _t,
  noop: ue,
  safe_not_equal: jo,
  set_attributes: sn,
  set_data: Zo,
  set_style: Uo,
  src_url_equal: Oo,
  text: Ho,
  toggle_class: on,
  update_await_block_branch: Wo
} = window.__gradio__svelte__internal;
function Go(l) {
  let e, t = (
    /*error*/
    l[3].message + ""
  ), n;
  return {
    c() {
      e = qn("p"), n = Ho(t), Uo(e, "color", "red");
    },
    m(i, s) {
      _t(i, e, s), To(e, n);
    },
    p(i, s) {
      s & /*src*/
      1 && t !== (t = /*error*/
      i[3].message + "") && Zo(n, t);
    },
    d(i) {
      i && ft(e);
    }
  };
}
function Ko(l) {
  let e, t, n = [
    {
      src: t = /*resolved_src*/
      l[2]
    },
    /*$$restProps*/
    l[1]
  ], i = {};
  for (let s = 0; s < n.length; s += 1)
    i = xe(i, n[s]);
  return {
    c() {
      e = qn("img"), sn(e, i), on(e, "svelte-1k8xp4f", !0);
    },
    m(s, o) {
      _t(s, e, o);
    },
    p(s, o) {
      sn(e, i = Xo(n, [
        o & /*src*/
        1 && !Oo(e.src, t = /*resolved_src*/
        s[2]) && { src: t },
        o & /*$$restProps*/
        2 && /*$$restProps*/
        s[1]
      ])), on(e, "svelte-1k8xp4f", !0);
    },
    d(s) {
      s && ft(e);
    }
  };
}
function Jo(l) {
  return { c: ue, m: ue, p: ue, d: ue };
}
function Qo(l) {
  let e, t, n = {
    ctx: l,
    current: null,
    token: null,
    hasCatch: !0,
    pending: Jo,
    then: Ko,
    catch: Go,
    value: 2,
    error: 3
  };
  return ln(t = tn(
    /*src*/
    l[0]
  ), n), {
    c() {
      e = Po(), n.block.c();
    },
    m(i, s) {
      _t(i, e, s), n.block.m(i, n.anchor = s), n.mount = () => e.parentNode, n.anchor = e;
    },
    p(i, [s]) {
      l = i, n.ctx = l, s & /*src*/
      1 && t !== (t = tn(
        /*src*/
        l[0]
      )) && ln(t, n) || Wo(n, l, s);
    },
    i: ue,
    o: ue,
    d(i) {
      i && ft(e), n.block.d(i), n.token = null, n = null;
    }
  };
}
function xo(l, e, t) {
  const n = ["src"];
  let i = nn(e, n), { src: s = void 0 } = e;
  return l.$$set = (o) => {
    e = xe(xe({}, e), No(o)), t(1, i = nn(e, n)), "src" in o && t(0, s = o.src);
  }, [s, i];
}
class $o extends Vo {
  constructor(e) {
    super(), Yo(this, e, xo, Qo, jo, { src: 0 });
  }
}
const {
  SvelteComponent: ea,
  attr: ta,
  create_component: na,
  destroy_component: la,
  detach: ia,
  element: sa,
  init: oa,
  insert: aa,
  mount_component: ra,
  safe_not_equal: fa,
  toggle_class: _e,
  transition_in: _a,
  transition_out: ca
} = window.__gradio__svelte__internal;
function ua(l) {
  let e, t, n;
  return t = new $o({
    props: {
      src: (
        /*samples_dir*/
        l[1] + /*value*/
        l[0]
      ),
      alt: ""
    }
  }), {
    c() {
      e = sa("div"), na(t.$$.fragment), ta(e, "class", "container svelte-1iqucjz"), _e(
        e,
        "table",
        /*type*/
        l[2] === "table"
      ), _e(
        e,
        "gallery",
        /*type*/
        l[2] === "gallery"
      ), _e(
        e,
        "selected",
        /*selected*/
        l[3]
      );
    },
    m(i, s) {
      aa(i, e, s), ra(t, e, null), n = !0;
    },
    p(i, [s]) {
      const o = {};
      s & /*samples_dir, value*/
      3 && (o.src = /*samples_dir*/
      i[1] + /*value*/
      i[0]), t.$set(o), (!n || s & /*type*/
      4) && _e(
        e,
        "table",
        /*type*/
        i[2] === "table"
      ), (!n || s & /*type*/
      4) && _e(
        e,
        "gallery",
        /*type*/
        i[2] === "gallery"
      ), (!n || s & /*selected*/
      8) && _e(
        e,
        "selected",
        /*selected*/
        i[3]
      );
    },
    i(i) {
      n || (_a(t.$$.fragment, i), n = !0);
    },
    o(i) {
      ca(t.$$.fragment, i), n = !1;
    },
    d(i) {
      i && ia(e), la(t);
    }
  };
}
function da(l, e, t) {
  let { value: n } = e, { samples_dir: i } = e, { type: s } = e, { selected: o = !1 } = e;
  return l.$$set = (a) => {
    "value" in a && t(0, n = a.value), "samples_dir" in a && t(1, i = a.samples_dir), "type" in a && t(2, s = a.type), "selected" in a && t(3, o = a.selected);
  }, [n, i, s, o];
}
class za extends ea {
  constructor(e) {
    super(), oa(this, e, da, ua, fa, {
      value: 0,
      samples_dir: 1,
      type: 2,
      selected: 3
    });
  }
}
const {
  SvelteComponent: ma,
  assign: ha,
  create_component: $e,
  destroy_component: et,
  detach: ga,
  flush: z,
  get_spread_object: ba,
  get_spread_update: wa,
  init: pa,
  insert: va,
  mount_component: tt,
  safe_not_equal: ka,
  space: ya,
  transition_in: nt,
  transition_out: lt
} = window.__gradio__svelte__internal;
function Ca(l) {
  let e, t, n, i;
  const s = [
    {
      autoscroll: (
        /*gradio*/
        l[15].autoscroll
      )
    },
    { i18n: (
      /*gradio*/
      l[15].i18n
    ) },
    /*loading_status*/
    l[13]
  ];
  let o = {};
  for (let a = 0; a < s.length; a += 1)
    o = ha(o, s[a]);
  return e = new Bo({ props: o }), n = new Us({
    props: {
      root: (
        /*root*/
        l[7]
      ),
      value: (
        /*value*/
        l[0]
      ),
      label: (
        /*label*/
        l[4]
      ),
      show_label: (
        /*show_label*/
        l[5]
      ),
      show_download_button: (
        /*show_download_button*/
        l[6]
      ),
      show_share_button: (
        /*show_share_button*/
        l[14]
      ),
      i18n: (
        /*gradio*/
        l[15].i18n
      )
    }
  }), n.$on(
    "select",
    /*select_handler*/
    l[17]
  ), n.$on(
    "share",
    /*share_handler*/
    l[18]
  ), n.$on(
    "error",
    /*error_handler*/
    l[19]
  ), {
    c() {
      $e(e.$$.fragment), t = ya(), $e(n.$$.fragment);
    },
    m(a, r) {
      tt(e, a, r), va(a, t, r), tt(n, a, r), i = !0;
    },
    p(a, r) {
      const f = r & /*gradio, loading_status*/
      40960 ? wa(s, [
        r & /*gradio*/
        32768 && {
          autoscroll: (
            /*gradio*/
            a[15].autoscroll
          )
        },
        r & /*gradio*/
        32768 && { i18n: (
          /*gradio*/
          a[15].i18n
        ) },
        r & /*loading_status*/
        8192 && ba(
          /*loading_status*/
          a[13]
        )
      ]) : {};
      e.$set(f);
      const _ = {};
      r & /*root*/
      128 && (_.root = /*root*/
      a[7]), r & /*value*/
      1 && (_.value = /*value*/
      a[0]), r & /*label*/
      16 && (_.label = /*label*/
      a[4]), r & /*show_label*/
      32 && (_.show_label = /*show_label*/
      a[5]), r & /*show_download_button*/
      64 && (_.show_download_button = /*show_download_button*/
      a[6]), r & /*show_share_button*/
      16384 && (_.show_share_button = /*show_share_button*/
      a[14]), r & /*gradio*/
      32768 && (_.i18n = /*gradio*/
      a[15].i18n), n.$set(_);
    },
    i(a) {
      i || (nt(e.$$.fragment, a), nt(n.$$.fragment, a), i = !0);
    },
    o(a) {
      lt(e.$$.fragment, a), lt(n.$$.fragment, a), i = !1;
    },
    d(a) {
      a && ga(t), et(e, a), et(n, a);
    }
  };
}
function qa(l) {
  let e, t;
  return e = new Wn({
    props: {
      visible: (
        /*visible*/
        l[3]
      ),
      variant: "solid",
      border_mode: (
        /*dragging*/
        l[16] ? "focus" : "base"
      ),
      padding: !1,
      elem_id: (
        /*elem_id*/
        l[1]
      ),
      elem_classes: (
        /*elem_classes*/
        l[2]
      ),
      height: (
        /*height*/
        l[8] || void 0
      ),
      width: (
        /*width*/
        l[9]
      ),
      allow_overflow: !1,
      container: (
        /*container*/
        l[10]
      ),
      scale: (
        /*scale*/
        l[11]
      ),
      min_width: (
        /*min_width*/
        l[12]
      ),
      $$slots: { default: [Ca] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      $e(e.$$.fragment);
    },
    m(n, i) {
      tt(e, n, i), t = !0;
    },
    p(n, [i]) {
      const s = {};
      i & /*visible*/
      8 && (s.visible = /*visible*/
      n[3]), i & /*elem_id*/
      2 && (s.elem_id = /*elem_id*/
      n[1]), i & /*elem_classes*/
      4 && (s.elem_classes = /*elem_classes*/
      n[2]), i & /*height*/
      256 && (s.height = /*height*/
      n[8] || void 0), i & /*width*/
      512 && (s.width = /*width*/
      n[9]), i & /*container*/
      1024 && (s.container = /*container*/
      n[10]), i & /*scale*/
      2048 && (s.scale = /*scale*/
      n[11]), i & /*min_width*/
      4096 && (s.min_width = /*min_width*/
      n[12]), i & /*$$scope, root, value, label, show_label, show_download_button, show_share_button, gradio, loading_status*/
      2154737 && (s.$$scope = { dirty: i, ctx: n }), e.$set(s);
    },
    i(n) {
      t || (nt(e.$$.fragment, n), t = !0);
    },
    o(n) {
      lt(e.$$.fragment, n), t = !1;
    },
    d(n) {
      et(e, n);
    }
  };
}
function Sa(l, e, t) {
  function n(h) {
    let H, A = h[0], W = 1;
    for (; W < h.length; ) {
      const U = h[W], N = h[W + 1];
      if (W += 2, (U === "optionalAccess" || U === "optionalCall") && A == null)
        return;
      U === "access" || U === "optionalAccess" ? (H = A, A = N(A)) : (U === "call" || U === "optionalCall") && (A = N((...te) => A.call(H, ...te)), H = void 0);
    }
    return A;
  }
  let { elem_id: i = "" } = e, { elem_classes: s = [] } = e, { visible: o = !0 } = e, { value: a = null } = e, { label: r } = e, { show_label: f } = e, { show_download_button: _ } = e, { root: c } = e, { height: u } = e, { width: d } = e, { container: g = !0 } = e, { scale: p = null } = e, { min_width: C = void 0 } = e, { loading_status: I } = e, { show_share_button: S = !1 } = e, { gradio: m } = e, y;
  const w = ({ detail: h }) => m.dispatch("select", h), Z = ({ detail: h }) => m.dispatch("share", h), V = ({ detail: h }) => m.dispatch("error", h);
  return l.$$set = (h) => {
    "elem_id" in h && t(1, i = h.elem_id), "elem_classes" in h && t(2, s = h.elem_classes), "visible" in h && t(3, o = h.visible), "value" in h && t(0, a = h.value), "label" in h && t(4, r = h.label), "show_label" in h && t(5, f = h.show_label), "show_download_button" in h && t(6, _ = h.show_download_button), "root" in h && t(7, c = h.root), "height" in h && t(8, u = h.height), "width" in h && t(9, d = h.width), "container" in h && t(10, g = h.container), "scale" in h && t(11, p = h.scale), "min_width" in h && t(12, C = h.min_width), "loading_status" in h && t(13, I = h.loading_status), "show_share_button" in h && t(14, S = h.show_share_button), "gradio" in h && t(15, m = h.gradio);
  }, l.$$.update = () => {
    l.$$.dirty & /*value*/
    1 && t(0, a = a || null), l.$$.dirty & /*value*/
    1 && console.log(a), l.$$.dirty & /*value, gradio*/
    32769 && n([a, "optionalAccess", (h) => h.image, "optionalAccess", (h) => h.url]) && m.dispatch("change");
  }, [
    a,
    i,
    s,
    o,
    r,
    f,
    _,
    c,
    u,
    d,
    g,
    p,
    C,
    I,
    S,
    m,
    y,
    w,
    Z,
    V
  ];
}
class Aa extends ma {
  constructor(e) {
    super(), pa(this, e, Sa, qa, ka, {
      elem_id: 1,
      elem_classes: 2,
      visible: 3,
      value: 0,
      label: 4,
      show_label: 5,
      show_download_button: 6,
      root: 7,
      height: 8,
      width: 9,
      container: 10,
      scale: 11,
      min_width: 12,
      loading_status: 13,
      show_share_button: 14,
      gradio: 15
    });
  }
  get elem_id() {
    return this.$$.ctx[1];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), z();
  }
  get elem_classes() {
    return this.$$.ctx[2];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), z();
  }
  get visible() {
    return this.$$.ctx[3];
  }
  set visible(e) {
    this.$$set({ visible: e }), z();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(e) {
    this.$$set({ value: e }), z();
  }
  get label() {
    return this.$$.ctx[4];
  }
  set label(e) {
    this.$$set({ label: e }), z();
  }
  get show_label() {
    return this.$$.ctx[5];
  }
  set show_label(e) {
    this.$$set({ show_label: e }), z();
  }
  get show_download_button() {
    return this.$$.ctx[6];
  }
  set show_download_button(e) {
    this.$$set({ show_download_button: e }), z();
  }
  get root() {
    return this.$$.ctx[7];
  }
  set root(e) {
    this.$$set({ root: e }), z();
  }
  get height() {
    return this.$$.ctx[8];
  }
  set height(e) {
    this.$$set({ height: e }), z();
  }
  get width() {
    return this.$$.ctx[9];
  }
  set width(e) {
    this.$$set({ width: e }), z();
  }
  get container() {
    return this.$$.ctx[10];
  }
  set container(e) {
    this.$$set({ container: e }), z();
  }
  get scale() {
    return this.$$.ctx[11];
  }
  set scale(e) {
    this.$$set({ scale: e }), z();
  }
  get min_width() {
    return this.$$.ctx[12];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), z();
  }
  get loading_status() {
    return this.$$.ctx[13];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), z();
  }
  get show_share_button() {
    return this.$$.ctx[14];
  }
  set show_share_button(e) {
    this.$$set({ show_share_button: e }), z();
  }
  get gradio() {
    return this.$$.ctx[15];
  }
  set gradio(e) {
    this.$$set({ gradio: e }), z();
  }
}
export {
  za as BaseExample,
  Us as BaseStaticImage,
  Aa as default
};
