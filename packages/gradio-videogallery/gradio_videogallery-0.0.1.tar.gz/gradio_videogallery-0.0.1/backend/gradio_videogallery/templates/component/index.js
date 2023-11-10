const {
  SvelteComponent: Pr,
  assign: Ir,
  create_slot: kr,
  detach: Lr,
  element: Nr,
  get_all_dirty_from_scope: Or,
  get_slot_changes: Mr,
  get_spread_update: Rr,
  init: Dr,
  insert: Ur,
  safe_not_equal: Gr,
  set_dynamic_element_data: Tn,
  set_style: X,
  toggle_class: de,
  transition_in: Oi,
  transition_out: Mi,
  update_slot_base: Fr
} = window.__gradio__svelte__internal;
function xr(e) {
  let t, n, i;
  const r = (
    /*#slots*/
    e[17].default
  ), l = kr(
    r,
    e,
    /*$$scope*/
    e[16],
    null
  );
  let o = [
    { "data-testid": (
      /*test_id*/
      e[7]
    ) },
    { id: (
      /*elem_id*/
      e[2]
    ) },
    {
      class: n = "block " + /*elem_classes*/
      e[3].join(" ") + " svelte-1t38q2d"
    }
  ], a = {};
  for (let s = 0; s < o.length; s += 1)
    a = Ir(a, o[s]);
  return {
    c() {
      t = Nr(
        /*tag*/
        e[14]
      ), l && l.c(), Tn(
        /*tag*/
        e[14]
      )(t, a), de(
        t,
        "hidden",
        /*visible*/
        e[10] === !1
      ), de(
        t,
        "padded",
        /*padding*/
        e[6]
      ), de(
        t,
        "border_focus",
        /*border_mode*/
        e[5] === "focus"
      ), de(t, "hide-container", !/*explicit_call*/
      e[8] && !/*container*/
      e[9]), X(t, "height", typeof /*height*/
      e[0] == "number" ? (
        /*height*/
        e[0] + "px"
      ) : void 0), X(t, "width", typeof /*width*/
      e[1] == "number" ? `calc(min(${/*width*/
      e[1]}px, 100%))` : void 0), X(
        t,
        "border-style",
        /*variant*/
        e[4]
      ), X(
        t,
        "overflow",
        /*allow_overflow*/
        e[11] ? "visible" : "hidden"
      ), X(
        t,
        "flex-grow",
        /*scale*/
        e[12]
      ), X(t, "min-width", `calc(min(${/*min_width*/
      e[13]}px, 100%))`), X(t, "border-width", "var(--block-border-width)");
    },
    m(s, u) {
      Ur(s, t, u), l && l.m(t, null), i = !0;
    },
    p(s, u) {
      l && l.p && (!i || u & /*$$scope*/
      65536) && Fr(
        l,
        r,
        s,
        /*$$scope*/
        s[16],
        i ? Mr(
          r,
          /*$$scope*/
          s[16],
          u,
          null
        ) : Or(
          /*$$scope*/
          s[16]
        ),
        null
      ), Tn(
        /*tag*/
        s[14]
      )(t, a = Rr(o, [
        (!i || u & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          s[7]
        ) },
        (!i || u & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          s[2]
        ) },
        (!i || u & /*elem_classes*/
        8 && n !== (n = "block " + /*elem_classes*/
        s[3].join(" ") + " svelte-1t38q2d")) && { class: n }
      ])), de(
        t,
        "hidden",
        /*visible*/
        s[10] === !1
      ), de(
        t,
        "padded",
        /*padding*/
        s[6]
      ), de(
        t,
        "border_focus",
        /*border_mode*/
        s[5] === "focus"
      ), de(t, "hide-container", !/*explicit_call*/
      s[8] && !/*container*/
      s[9]), u & /*height*/
      1 && X(t, "height", typeof /*height*/
      s[0] == "number" ? (
        /*height*/
        s[0] + "px"
      ) : void 0), u & /*width*/
      2 && X(t, "width", typeof /*width*/
      s[1] == "number" ? `calc(min(${/*width*/
      s[1]}px, 100%))` : void 0), u & /*variant*/
      16 && X(
        t,
        "border-style",
        /*variant*/
        s[4]
      ), u & /*allow_overflow*/
      2048 && X(
        t,
        "overflow",
        /*allow_overflow*/
        s[11] ? "visible" : "hidden"
      ), u & /*scale*/
      4096 && X(
        t,
        "flex-grow",
        /*scale*/
        s[12]
      ), u & /*min_width*/
      8192 && X(t, "min-width", `calc(min(${/*min_width*/
      s[13]}px, 100%))`);
    },
    i(s) {
      i || (Oi(l, s), i = !0);
    },
    o(s) {
      Mi(l, s), i = !1;
    },
    d(s) {
      s && Lr(t), l && l.d(s);
    }
  };
}
function jr(e) {
  let t, n = (
    /*tag*/
    e[14] && xr(e)
  );
  return {
    c() {
      n && n.c();
    },
    m(i, r) {
      n && n.m(i, r), t = !0;
    },
    p(i, [r]) {
      /*tag*/
      i[14] && n.p(i, r);
    },
    i(i) {
      t || (Oi(n, i), t = !0);
    },
    o(i) {
      Mi(n, i), t = !1;
    },
    d(i) {
      n && n.d(i);
    }
  };
}
function Vr(e, t, n) {
  let { $$slots: i = {}, $$scope: r } = t, { height: l = void 0 } = t, { width: o = void 0 } = t, { elem_id: a = "" } = t, { elem_classes: s = [] } = t, { variant: u = "solid" } = t, { border_mode: f = "base" } = t, { padding: c = !0 } = t, { type: h = "normal" } = t, { test_id: _ = void 0 } = t, { explicit_call: b = !1 } = t, { container: T = !0 } = t, { visible: y = !0 } = t, { allow_overflow: C = !0 } = t, { scale: E = null } = t, { min_width: m = 0 } = t, g = h === "fieldset" ? "fieldset" : "div";
  return e.$$set = (p) => {
    "height" in p && n(0, l = p.height), "width" in p && n(1, o = p.width), "elem_id" in p && n(2, a = p.elem_id), "elem_classes" in p && n(3, s = p.elem_classes), "variant" in p && n(4, u = p.variant), "border_mode" in p && n(5, f = p.border_mode), "padding" in p && n(6, c = p.padding), "type" in p && n(15, h = p.type), "test_id" in p && n(7, _ = p.test_id), "explicit_call" in p && n(8, b = p.explicit_call), "container" in p && n(9, T = p.container), "visible" in p && n(10, y = p.visible), "allow_overflow" in p && n(11, C = p.allow_overflow), "scale" in p && n(12, E = p.scale), "min_width" in p && n(13, m = p.min_width), "$$scope" in p && n(16, r = p.$$scope);
  }, [
    l,
    o,
    a,
    s,
    u,
    f,
    c,
    _,
    b,
    T,
    y,
    C,
    E,
    m,
    g,
    h,
    r,
    i
  ];
}
class zr extends Pr {
  constructor(t) {
    super(), Dr(this, t, Vr, jr, Gr, {
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
  SvelteComponent: qr,
  append: It,
  attr: at,
  create_component: Xr,
  destroy_component: Zr,
  detach: Wr,
  element: An,
  init: Qr,
  insert: Jr,
  mount_component: Yr,
  safe_not_equal: Kr,
  set_data: $r,
  space: el,
  text: tl,
  toggle_class: be,
  transition_in: nl,
  transition_out: il
} = window.__gradio__svelte__internal;
function rl(e) {
  let t, n, i, r, l, o;
  return i = new /*Icon*/
  e[1]({}), {
    c() {
      t = An("label"), n = An("span"), Xr(i.$$.fragment), r = el(), l = tl(
        /*label*/
        e[0]
      ), at(n, "class", "svelte-9gxdi0"), at(t, "for", ""), at(t, "data-testid", "block-label"), at(t, "class", "svelte-9gxdi0"), be(t, "hide", !/*show_label*/
      e[2]), be(t, "sr-only", !/*show_label*/
      e[2]), be(
        t,
        "float",
        /*float*/
        e[4]
      ), be(
        t,
        "hide-label",
        /*disable*/
        e[3]
      );
    },
    m(a, s) {
      Jr(a, t, s), It(t, n), Yr(i, n, null), It(t, r), It(t, l), o = !0;
    },
    p(a, [s]) {
      (!o || s & /*label*/
      1) && $r(
        l,
        /*label*/
        a[0]
      ), (!o || s & /*show_label*/
      4) && be(t, "hide", !/*show_label*/
      a[2]), (!o || s & /*show_label*/
      4) && be(t, "sr-only", !/*show_label*/
      a[2]), (!o || s & /*float*/
      16) && be(
        t,
        "float",
        /*float*/
        a[4]
      ), (!o || s & /*disable*/
      8) && be(
        t,
        "hide-label",
        /*disable*/
        a[3]
      );
    },
    i(a) {
      o || (nl(i.$$.fragment, a), o = !0);
    },
    o(a) {
      il(i.$$.fragment, a), o = !1;
    },
    d(a) {
      a && Wr(t), Zr(i);
    }
  };
}
function ll(e, t, n) {
  let { label: i = null } = t, { Icon: r } = t, { show_label: l = !0 } = t, { disable: o = !1 } = t, { float: a = !0 } = t;
  return e.$$set = (s) => {
    "label" in s && n(0, i = s.label), "Icon" in s && n(1, r = s.Icon), "show_label" in s && n(2, l = s.show_label), "disable" in s && n(3, o = s.disable), "float" in s && n(4, a = s.float);
  }, [i, r, l, o, a];
}
class ol extends qr {
  constructor(t) {
    super(), Qr(this, t, ll, rl, Kr, {
      label: 0,
      Icon: 1,
      show_label: 2,
      disable: 3,
      float: 4
    });
  }
}
const {
  SvelteComponent: sl,
  append: Qt,
  attr: Se,
  bubble: al,
  create_component: ul,
  destroy_component: fl,
  detach: Ri,
  element: Jt,
  init: cl,
  insert: Di,
  listen: hl,
  mount_component: _l,
  safe_not_equal: ml,
  set_data: dl,
  space: bl,
  text: gl,
  toggle_class: ge,
  transition_in: pl,
  transition_out: vl
} = window.__gradio__svelte__internal;
function Hn(e) {
  let t, n;
  return {
    c() {
      t = Jt("span"), n = gl(
        /*label*/
        e[1]
      ), Se(t, "class", "svelte-xtz2g8");
    },
    m(i, r) {
      Di(i, t, r), Qt(t, n);
    },
    p(i, r) {
      r & /*label*/
      2 && dl(
        n,
        /*label*/
        i[1]
      );
    },
    d(i) {
      i && Ri(t);
    }
  };
}
function wl(e) {
  let t, n, i, r, l, o, a, s = (
    /*show_label*/
    e[2] && Hn(e)
  );
  return r = new /*Icon*/
  e[0]({}), {
    c() {
      t = Jt("button"), s && s.c(), n = bl(), i = Jt("div"), ul(r.$$.fragment), Se(i, "class", "svelte-xtz2g8"), ge(
        i,
        "small",
        /*size*/
        e[4] === "small"
      ), ge(
        i,
        "large",
        /*size*/
        e[4] === "large"
      ), Se(
        t,
        "aria-label",
        /*label*/
        e[1]
      ), Se(
        t,
        "title",
        /*label*/
        e[1]
      ), Se(t, "class", "svelte-xtz2g8"), ge(
        t,
        "pending",
        /*pending*/
        e[3]
      ), ge(
        t,
        "padded",
        /*padded*/
        e[5]
      );
    },
    m(u, f) {
      Di(u, t, f), s && s.m(t, null), Qt(t, n), Qt(t, i), _l(r, i, null), l = !0, o || (a = hl(
        t,
        "click",
        /*click_handler*/
        e[6]
      ), o = !0);
    },
    p(u, [f]) {
      /*show_label*/
      u[2] ? s ? s.p(u, f) : (s = Hn(u), s.c(), s.m(t, n)) : s && (s.d(1), s = null), (!l || f & /*size*/
      16) && ge(
        i,
        "small",
        /*size*/
        u[4] === "small"
      ), (!l || f & /*size*/
      16) && ge(
        i,
        "large",
        /*size*/
        u[4] === "large"
      ), (!l || f & /*label*/
      2) && Se(
        t,
        "aria-label",
        /*label*/
        u[1]
      ), (!l || f & /*label*/
      2) && Se(
        t,
        "title",
        /*label*/
        u[1]
      ), (!l || f & /*pending*/
      8) && ge(
        t,
        "pending",
        /*pending*/
        u[3]
      ), (!l || f & /*padded*/
      32) && ge(
        t,
        "padded",
        /*padded*/
        u[5]
      );
    },
    i(u) {
      l || (pl(r.$$.fragment, u), l = !0);
    },
    o(u) {
      vl(r.$$.fragment, u), l = !1;
    },
    d(u) {
      u && Ri(t), s && s.d(), fl(r), o = !1, a();
    }
  };
}
function yl(e, t, n) {
  let { Icon: i } = t, { label: r = "" } = t, { show_label: l = !1 } = t, { pending: o = !1 } = t, { size: a = "small" } = t, { padded: s = !0 } = t;
  function u(f) {
    al.call(this, e, f);
  }
  return e.$$set = (f) => {
    "Icon" in f && n(0, i = f.Icon), "label" in f && n(1, r = f.label), "show_label" in f && n(2, l = f.show_label), "pending" in f && n(3, o = f.pending), "size" in f && n(4, a = f.size), "padded" in f && n(5, s = f.padded);
  }, [i, r, l, o, a, s, u];
}
class et extends sl {
  constructor(t) {
    super(), cl(this, t, yl, wl, ml, {
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
  SvelteComponent: El,
  append: Sl,
  attr: kt,
  binding_callbacks: Tl,
  create_slot: Al,
  detach: Hl,
  element: Bn,
  get_all_dirty_from_scope: Bl,
  get_slot_changes: Cl,
  init: Pl,
  insert: Il,
  safe_not_equal: kl,
  toggle_class: pe,
  transition_in: Ll,
  transition_out: Nl,
  update_slot_base: Ol
} = window.__gradio__svelte__internal;
function Ml(e) {
  let t, n, i;
  const r = (
    /*#slots*/
    e[5].default
  ), l = Al(
    r,
    e,
    /*$$scope*/
    e[4],
    null
  );
  return {
    c() {
      t = Bn("div"), n = Bn("div"), l && l.c(), kt(n, "class", "icon svelte-3w3rth"), kt(t, "class", "empty svelte-3w3rth"), kt(t, "aria-label", "Empty value"), pe(
        t,
        "small",
        /*size*/
        e[0] === "small"
      ), pe(
        t,
        "large",
        /*size*/
        e[0] === "large"
      ), pe(
        t,
        "unpadded_box",
        /*unpadded_box*/
        e[1]
      ), pe(
        t,
        "small_parent",
        /*parent_height*/
        e[3]
      );
    },
    m(o, a) {
      Il(o, t, a), Sl(t, n), l && l.m(n, null), e[6](t), i = !0;
    },
    p(o, [a]) {
      l && l.p && (!i || a & /*$$scope*/
      16) && Ol(
        l,
        r,
        o,
        /*$$scope*/
        o[4],
        i ? Cl(
          r,
          /*$$scope*/
          o[4],
          a,
          null
        ) : Bl(
          /*$$scope*/
          o[4]
        ),
        null
      ), (!i || a & /*size*/
      1) && pe(
        t,
        "small",
        /*size*/
        o[0] === "small"
      ), (!i || a & /*size*/
      1) && pe(
        t,
        "large",
        /*size*/
        o[0] === "large"
      ), (!i || a & /*unpadded_box*/
      2) && pe(
        t,
        "unpadded_box",
        /*unpadded_box*/
        o[1]
      ), (!i || a & /*parent_height*/
      8) && pe(
        t,
        "small_parent",
        /*parent_height*/
        o[3]
      );
    },
    i(o) {
      i || (Ll(l, o), i = !0);
    },
    o(o) {
      Nl(l, o), i = !1;
    },
    d(o) {
      o && Hl(t), l && l.d(o), e[6](null);
    }
  };
}
function Rl(e) {
  let t, n = e[0], i = 1;
  for (; i < e.length; ) {
    const r = e[i], l = e[i + 1];
    if (i += 2, (r === "optionalAccess" || r === "optionalCall") && n == null)
      return;
    r === "access" || r === "optionalAccess" ? (t = n, n = l(n)) : (r === "call" || r === "optionalCall") && (n = l((...o) => n.call(t, ...o)), t = void 0);
  }
  return n;
}
function Dl(e, t, n) {
  let i, { $$slots: r = {}, $$scope: l } = t, { size: o = "small" } = t, { unpadded_box: a = !1 } = t, s;
  function u(c) {
    if (!c)
      return !1;
    const { height: h } = c.getBoundingClientRect(), { height: _ } = Rl([
      c,
      "access",
      (b) => b.parentElement,
      "optionalAccess",
      (b) => b.getBoundingClientRect,
      "call",
      (b) => b()
    ]) || { height: h };
    return h > _ + 2;
  }
  function f(c) {
    Tl[c ? "unshift" : "push"](() => {
      s = c, n(2, s);
    });
  }
  return e.$$set = (c) => {
    "size" in c && n(0, o = c.size), "unpadded_box" in c && n(1, a = c.unpadded_box), "$$scope" in c && n(4, l = c.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty & /*el*/
    4 && n(3, i = u(s));
  }, [o, a, s, i, l, r, f];
}
class Ul extends El {
  constructor(t) {
    super(), Pl(this, t, Dl, Ml, kl, { size: 0, unpadded_box: 1 });
  }
}
const {
  SvelteComponent: Gl,
  append: Lt,
  attr: te,
  detach: Fl,
  init: xl,
  insert: jl,
  noop: Nt,
  safe_not_equal: Vl,
  set_style: oe,
  svg_element: ut
} = window.__gradio__svelte__internal;
function zl(e) {
  let t, n, i, r;
  return {
    c() {
      t = ut("svg"), n = ut("g"), i = ut("path"), r = ut("path"), te(i, "d", "M18,6L6.087,17.913"), oe(i, "fill", "none"), oe(i, "fill-rule", "nonzero"), oe(i, "stroke-width", "2px"), te(n, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), te(r, "d", "M4.364,4.364L19.636,19.636"), oe(r, "fill", "none"), oe(r, "fill-rule", "nonzero"), oe(r, "stroke-width", "2px"), te(t, "width", "100%"), te(t, "height", "100%"), te(t, "viewBox", "0 0 24 24"), te(t, "version", "1.1"), te(t, "xmlns", "http://www.w3.org/2000/svg"), te(t, "xmlns:xlink", "http://www.w3.org/1999/xlink"), te(t, "xml:space", "preserve"), te(t, "stroke", "currentColor"), oe(t, "fill-rule", "evenodd"), oe(t, "clip-rule", "evenodd"), oe(t, "stroke-linecap", "round"), oe(t, "stroke-linejoin", "round");
    },
    m(l, o) {
      jl(l, t, o), Lt(t, n), Lt(n, i), Lt(t, r);
    },
    p: Nt,
    i: Nt,
    o: Nt,
    d(l) {
      l && Fl(t);
    }
  };
}
class ql extends Gl {
  constructor(t) {
    super(), xl(this, t, null, zl, Vl, {});
  }
}
const {
  SvelteComponent: Xl,
  append: Zl,
  attr: Xe,
  detach: Wl,
  init: Ql,
  insert: Jl,
  noop: Ot,
  safe_not_equal: Yl,
  svg_element: Cn
} = window.__gradio__svelte__internal;
function Kl(e) {
  let t, n;
  return {
    c() {
      t = Cn("svg"), n = Cn("path"), Xe(n, "d", "M23,20a5,5,0,0,0-3.89,1.89L11.8,17.32a4.46,4.46,0,0,0,0-2.64l7.31-4.57A5,5,0,1,0,18,7a4.79,4.79,0,0,0,.2,1.32l-7.31,4.57a5,5,0,1,0,0,6.22l7.31,4.57A4.79,4.79,0,0,0,18,25a5,5,0,1,0,5-5ZM23,4a3,3,0,1,1-3,3A3,3,0,0,1,23,4ZM7,19a3,3,0,1,1,3-3A3,3,0,0,1,7,19Zm16,9a3,3,0,1,1,3-3A3,3,0,0,1,23,28Z"), Xe(n, "fill", "currentColor"), Xe(t, "id", "icon"), Xe(t, "xmlns", "http://www.w3.org/2000/svg"), Xe(t, "viewBox", "0 0 32 32");
    },
    m(i, r) {
      Jl(i, t, r), Zl(t, n);
    },
    p: Ot,
    i: Ot,
    o: Ot,
    d(i) {
      i && Wl(t);
    }
  };
}
class $l extends Xl {
  constructor(t) {
    super(), Ql(this, t, null, Kl, Yl, {});
  }
}
const {
  SvelteComponent: eo,
  append: to,
  attr: Ce,
  detach: no,
  init: io,
  insert: ro,
  noop: Mt,
  safe_not_equal: lo,
  svg_element: Pn
} = window.__gradio__svelte__internal;
function oo(e) {
  let t, n;
  return {
    c() {
      t = Pn("svg"), n = Pn("path"), Ce(n, "fill", "currentColor"), Ce(n, "d", "M26 24v4H6v-4H4v4a2 2 0 0 0 2 2h20a2 2 0 0 0 2-2v-4zm0-10l-1.41-1.41L17 20.17V2h-2v18.17l-7.59-7.58L6 14l10 10l10-10z"), Ce(t, "xmlns", "http://www.w3.org/2000/svg"), Ce(t, "width", "100%"), Ce(t, "height", "100%"), Ce(t, "viewBox", "0 0 32 32");
    },
    m(i, r) {
      ro(i, t, r), to(t, n);
    },
    p: Mt,
    i: Mt,
    o: Mt,
    d(i) {
      i && no(t);
    }
  };
}
class so extends eo {
  constructor(t) {
    super(), io(this, t, null, oo, lo, {});
  }
}
const {
  SvelteComponent: ao,
  append: uo,
  attr: ne,
  detach: fo,
  init: co,
  insert: ho,
  noop: Rt,
  safe_not_equal: _o,
  svg_element: In
} = window.__gradio__svelte__internal;
function mo(e) {
  let t, n;
  return {
    c() {
      t = In("svg"), n = In("path"), ne(n, "d", "M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"), ne(t, "xmlns", "http://www.w3.org/2000/svg"), ne(t, "width", "100%"), ne(t, "height", "100%"), ne(t, "viewBox", "0 0 24 24"), ne(t, "fill", "none"), ne(t, "stroke", "currentColor"), ne(t, "stroke-width", "1.5"), ne(t, "stroke-linecap", "round"), ne(t, "stroke-linejoin", "round"), ne(t, "class", "feather feather-edit-2");
    },
    m(i, r) {
      ho(i, t, r), uo(t, n);
    },
    p: Rt,
    i: Rt,
    o: Rt,
    d(i) {
      i && fo(t);
    }
  };
}
class bo extends ao {
  constructor(t) {
    super(), co(this, t, null, mo, _o, {});
  }
}
const {
  SvelteComponent: go,
  append: Dt,
  attr: R,
  detach: po,
  init: vo,
  insert: wo,
  noop: Ut,
  safe_not_equal: yo,
  svg_element: ft
} = window.__gradio__svelte__internal;
function Eo(e) {
  let t, n, i, r;
  return {
    c() {
      t = ft("svg"), n = ft("rect"), i = ft("circle"), r = ft("polyline"), R(n, "x", "3"), R(n, "y", "3"), R(n, "width", "18"), R(n, "height", "18"), R(n, "rx", "2"), R(n, "ry", "2"), R(i, "cx", "8.5"), R(i, "cy", "8.5"), R(i, "r", "1.5"), R(r, "points", "21 15 16 10 5 21"), R(t, "xmlns", "http://www.w3.org/2000/svg"), R(t, "width", "100%"), R(t, "height", "100%"), R(t, "viewBox", "0 0 24 24"), R(t, "fill", "none"), R(t, "stroke", "currentColor"), R(t, "stroke-width", "1.5"), R(t, "stroke-linecap", "round"), R(t, "stroke-linejoin", "round"), R(t, "class", "feather feather-image");
    },
    m(l, o) {
      wo(l, t, o), Dt(t, n), Dt(t, i), Dt(t, r);
    },
    p: Ut,
    i: Ut,
    o: Ut,
    d(l) {
      l && po(t);
    }
  };
}
class Ui extends go {
  constructor(t) {
    super(), vo(this, t, null, Eo, yo, {});
  }
}
const {
  SvelteComponent: So,
  append: kn,
  attr: Q,
  detach: To,
  init: Ao,
  insert: Ho,
  noop: Gt,
  safe_not_equal: Bo,
  svg_element: Ft
} = window.__gradio__svelte__internal;
function Co(e) {
  let t, n, i;
  return {
    c() {
      t = Ft("svg"), n = Ft("polyline"), i = Ft("path"), Q(n, "points", "1 4 1 10 7 10"), Q(i, "d", "M3.51 15a9 9 0 1 0 2.13-9.36L1 10"), Q(t, "xmlns", "http://www.w3.org/2000/svg"), Q(t, "width", "100%"), Q(t, "height", "100%"), Q(t, "viewBox", "0 0 24 24"), Q(t, "fill", "none"), Q(t, "stroke", "currentColor"), Q(t, "stroke-width", "2"), Q(t, "stroke-linecap", "round"), Q(t, "stroke-linejoin", "round"), Q(t, "class", "feather feather-rotate-ccw");
    },
    m(r, l) {
      Ho(r, t, l), kn(t, n), kn(t, i);
    },
    p: Gt,
    i: Gt,
    o: Gt,
    d(r) {
      r && To(t);
    }
  };
}
class Po extends So {
  constructor(t) {
    super(), Ao(this, t, null, Co, Bo, {});
  }
}
const Io = [
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
], Ln = {
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
Io.reduce(
  (e, { color: t, primary: n, secondary: i }) => ({
    ...e,
    [t]: {
      primary: Ln[t][n],
      secondary: Ln[t][i]
    }
  }),
  {}
);
function ko(e) {
  let t, n = e[0], i = 1;
  for (; i < e.length; ) {
    const r = e[i], l = e[i + 1];
    if (i += 2, (r === "optionalAccess" || r === "optionalCall") && n == null)
      return;
    r === "access" || r === "optionalAccess" ? (t = n, n = l(n)) : (r === "call" || r === "optionalCall") && (n = l((...o) => n.call(t, ...o)), t = void 0);
  }
  return n;
}
class mt extends Error {
  constructor(t) {
    super(t), this.name = "ShareError";
  }
}
async function Lo(e, t) {
  if (window.__gradio_space__ == null)
    throw new mt("Must be on Spaces to share.");
  let n, i, r;
  if (t === "url") {
    const s = await fetch(e);
    n = await s.blob(), i = s.headers.get("content-type") || "", r = s.headers.get("content-disposition") || "";
  } else
    n = No(e), i = e.split(";")[0].split(":")[1], r = "file" + i.split("/")[1];
  const l = new File([n], r, { type: i }), o = await fetch("https://huggingface.co/uploads", {
    method: "POST",
    body: l,
    headers: {
      "Content-Type": l.type,
      "X-Requested-With": "XMLHttpRequest"
    }
  });
  if (!o.ok) {
    if (ko([o, "access", (s) => s.headers, "access", (s) => s.get, "call", (s) => s("content-type"), "optionalAccess", (s) => s.includes, "call", (s) => s("application/json")])) {
      const s = await o.json();
      throw new mt(`Upload failed: ${s.error}`);
    }
    throw new mt("Upload failed.");
  }
  return await o.text();
}
function No(e) {
  for (var t = e.split(","), n = t[0].match(/:(.*?);/)[1], i = atob(t[1]), r = i.length, l = new Uint8Array(r); r--; )
    l[r] = i.charCodeAt(r);
  return new Blob([l], { type: n });
}
const {
  SvelteComponent: Oo,
  create_component: Mo,
  destroy_component: Ro,
  init: Do,
  mount_component: Uo,
  safe_not_equal: Go,
  transition_in: Fo,
  transition_out: xo
} = window.__gradio__svelte__internal, { createEventDispatcher: jo } = window.__gradio__svelte__internal;
function Vo(e) {
  let t, n;
  return t = new et({
    props: {
      Icon: $l,
      label: (
        /*i18n*/
        e[2]("common.share")
      ),
      pending: (
        /*pending*/
        e[3]
      )
    }
  }), t.$on(
    "click",
    /*click_handler*/
    e[5]
  ), {
    c() {
      Mo(t.$$.fragment);
    },
    m(i, r) {
      Uo(t, i, r), n = !0;
    },
    p(i, [r]) {
      const l = {};
      r & /*i18n*/
      4 && (l.label = /*i18n*/
      i[2]("common.share")), r & /*pending*/
      8 && (l.pending = /*pending*/
      i[3]), t.$set(l);
    },
    i(i) {
      n || (Fo(t.$$.fragment, i), n = !0);
    },
    o(i) {
      xo(t.$$.fragment, i), n = !1;
    },
    d(i) {
      Ro(t, i);
    }
  };
}
function zo(e, t, n) {
  const i = jo();
  let { formatter: r } = t, { value: l } = t, { i18n: o } = t, a = !1;
  const s = async () => {
    try {
      n(3, a = !0);
      const u = await r(l);
      i("share", { description: u });
    } catch (u) {
      console.error(u);
      let f = u instanceof mt ? u.message : "Share failed.";
      i("error", f);
    } finally {
      n(3, a = !1);
    }
  };
  return e.$$set = (u) => {
    "formatter" in u && n(0, r = u.formatter), "value" in u && n(1, l = u.value), "i18n" in u && n(2, o = u.i18n);
  }, [r, l, o, a, i, s];
}
class qo extends Oo {
  constructor(t) {
    super(), Do(this, t, zo, Vo, Go, { formatter: 0, value: 1, i18n: 2 });
  }
}
new Intl.Collator(0, { numeric: 1 }).compare;
function Gi(e, t, n) {
  if (e == null)
    return null;
  if (Array.isArray(e)) {
    const i = [];
    for (const r of e)
      r == null ? i.push(null) : i.push(Gi(r, t, n));
    return i;
  }
  return e.is_stream ? n == null ? new xt({
    ...e,
    url: t + "/stream/" + e.path
  }) : new xt({
    ...e,
    url: "/proxy=" + n + "stream/" + e.path
  }) : new xt({
    ...e,
    url: Zo(e.path, t, n)
  });
}
function Xo(e) {
  try {
    const t = new URL(e);
    return t.protocol === "http:" || t.protocol === "https:";
  } catch {
    return !1;
  }
}
function Zo(e, t, n) {
  return e == null ? n ? `/proxy=${n}file=` : `${t}/file=` : Xo(e) ? e : n ? `/proxy=${n}file=${e}` : `${t}/file=${e}`;
}
class xt {
  constructor({
    path: t,
    url: n,
    orig_name: i,
    size: r,
    blob: l,
    is_stream: o,
    mime_type: a,
    alt_text: s
  }) {
    this.path = t, this.url = n, this.orig_name = i, this.size = r, this.blob = n ? void 0 : l, this.is_stream = o, this.mime_type = a, this.alt_text = s;
  }
}
function He() {
}
function Wo(e) {
  return e();
}
function Qo(e) {
  e.forEach(Wo);
}
function Jo(e) {
  return typeof e == "function";
}
function Yo(e, t) {
  return e != e ? t == t : e !== t || e && typeof e == "object" || typeof e == "function";
}
function Ko(e, ...t) {
  if (e == null) {
    for (const i of t)
      i(void 0);
    return He;
  }
  const n = e.subscribe(...t);
  return n.unsubscribe ? () => n.unsubscribe() : n;
}
const Fi = typeof window < "u";
let Nn = Fi ? () => window.performance.now() : () => Date.now(), xi = Fi ? (e) => requestAnimationFrame(e) : He;
const ke = /* @__PURE__ */ new Set();
function ji(e) {
  ke.forEach((t) => {
    t.c(e) || (ke.delete(t), t.f());
  }), ke.size !== 0 && xi(ji);
}
function $o(e) {
  let t;
  return ke.size === 0 && xi(ji), {
    promise: new Promise((n) => {
      ke.add(t = { c: e, f: n });
    }),
    abort() {
      ke.delete(t);
    }
  };
}
const Pe = [];
function es(e, t) {
  return {
    subscribe: tt(e, t).subscribe
  };
}
function tt(e, t = He) {
  let n;
  const i = /* @__PURE__ */ new Set();
  function r(a) {
    if (Yo(e, a) && (e = a, n)) {
      const s = !Pe.length;
      for (const u of i)
        u[1](), Pe.push(u, e);
      if (s) {
        for (let u = 0; u < Pe.length; u += 2)
          Pe[u][0](Pe[u + 1]);
        Pe.length = 0;
      }
    }
  }
  function l(a) {
    r(a(e));
  }
  function o(a, s = He) {
    const u = [a, s];
    return i.add(u), i.size === 1 && (n = t(r, l) || He), a(e), () => {
      i.delete(u), i.size === 0 && n && (n(), n = null);
    };
  }
  return { set: r, update: l, subscribe: o };
}
function Ue(e, t, n) {
  const i = !Array.isArray(e), r = i ? [e] : e;
  if (!r.every(Boolean))
    throw new Error("derived() expects stores as input, got a falsy value");
  const l = t.length < 2;
  return es(n, (o, a) => {
    let s = !1;
    const u = [];
    let f = 0, c = He;
    const h = () => {
      if (f)
        return;
      c();
      const b = t(i ? u[0] : u, o, a);
      l ? o(b) : c = Jo(b) ? b : He;
    }, _ = r.map(
      (b, T) => Ko(
        b,
        (y) => {
          u[T] = y, f &= ~(1 << T), s && h();
        },
        () => {
          f |= 1 << T;
        }
      )
    );
    return s = !0, h(), function() {
      Qo(_), c(), s = !1;
    };
  });
}
function On(e) {
  return Object.prototype.toString.call(e) === "[object Date]";
}
function Yt(e, t, n, i) {
  if (typeof n == "number" || On(n)) {
    const r = i - n, l = (n - t) / (e.dt || 1 / 60), o = e.opts.stiffness * r, a = e.opts.damping * l, s = (o - a) * e.inv_mass, u = (l + s) * e.dt;
    return Math.abs(u) < e.opts.precision && Math.abs(r) < e.opts.precision ? i : (e.settled = !1, On(n) ? new Date(n.getTime() + u) : n + u);
  } else {
    if (Array.isArray(n))
      return n.map(
        (r, l) => Yt(e, t[l], n[l], i[l])
      );
    if (typeof n == "object") {
      const r = {};
      for (const l in n)
        r[l] = Yt(e, t[l], n[l], i[l]);
      return r;
    } else
      throw new Error(`Cannot spring ${typeof n} values`);
  }
}
function Mn(e, t = {}) {
  const n = tt(e), { stiffness: i = 0.15, damping: r = 0.8, precision: l = 0.01 } = t;
  let o, a, s, u = e, f = e, c = 1, h = 0, _ = !1;
  function b(y, C = {}) {
    f = y;
    const E = s = {};
    return e == null || C.hard || T.stiffness >= 1 && T.damping >= 1 ? (_ = !0, o = Nn(), u = y, n.set(e = f), Promise.resolve()) : (C.soft && (h = 1 / ((C.soft === !0 ? 0.5 : +C.soft) * 60), c = 0), a || (o = Nn(), _ = !1, a = $o((m) => {
      if (_)
        return _ = !1, a = null, !1;
      c = Math.min(c + h, 1);
      const g = {
        inv_mass: c,
        opts: T,
        settled: !0,
        dt: (m - o) * 60 / 1e3
      }, p = Yt(g, u, e, f);
      return o = m, u = e, n.set(e = p), g.settled && (a = null), !g.settled;
    })), new Promise((m) => {
      a.promise.then(() => {
        E === s && m();
      });
    }));
  }
  const T = {
    set: b,
    update: (y, C) => b(y(f, e), C),
    subscribe: n.subscribe,
    stiffness: i,
    damping: r,
    precision: l
  };
  return T;
}
function ts(e) {
  return e && e.__esModule && Object.prototype.hasOwnProperty.call(e, "default") ? e.default : e;
}
var ns = function(t) {
  return is(t) && !rs(t);
};
function is(e) {
  return !!e && typeof e == "object";
}
function rs(e) {
  var t = Object.prototype.toString.call(e);
  return t === "[object RegExp]" || t === "[object Date]" || ss(e);
}
var ls = typeof Symbol == "function" && Symbol.for, os = ls ? Symbol.for("react.element") : 60103;
function ss(e) {
  return e.$$typeof === os;
}
function as(e) {
  return Array.isArray(e) ? [] : {};
}
function Je(e, t) {
  return t.clone !== !1 && t.isMergeableObject(e) ? Le(as(e), e, t) : e;
}
function us(e, t, n) {
  return e.concat(t).map(function(i) {
    return Je(i, n);
  });
}
function fs(e, t) {
  if (!t.customMerge)
    return Le;
  var n = t.customMerge(e);
  return typeof n == "function" ? n : Le;
}
function cs(e) {
  return Object.getOwnPropertySymbols ? Object.getOwnPropertySymbols(e).filter(function(t) {
    return Object.propertyIsEnumerable.call(e, t);
  }) : [];
}
function Rn(e) {
  return Object.keys(e).concat(cs(e));
}
function Vi(e, t) {
  try {
    return t in e;
  } catch {
    return !1;
  }
}
function hs(e, t) {
  return Vi(e, t) && !(Object.hasOwnProperty.call(e, t) && Object.propertyIsEnumerable.call(e, t));
}
function _s(e, t, n) {
  var i = {};
  return n.isMergeableObject(e) && Rn(e).forEach(function(r) {
    i[r] = Je(e[r], n);
  }), Rn(t).forEach(function(r) {
    hs(e, r) || (Vi(e, r) && n.isMergeableObject(t[r]) ? i[r] = fs(r, n)(e[r], t[r], n) : i[r] = Je(t[r], n));
  }), i;
}
function Le(e, t, n) {
  n = n || {}, n.arrayMerge = n.arrayMerge || us, n.isMergeableObject = n.isMergeableObject || ns, n.cloneUnlessOtherwiseSpecified = Je;
  var i = Array.isArray(t), r = Array.isArray(e), l = i === r;
  return l ? i ? n.arrayMerge(e, t, n) : _s(e, t, n) : Je(t, n);
}
Le.all = function(t, n) {
  if (!Array.isArray(t))
    throw new Error("first argument should be an array");
  return t.reduce(function(i, r) {
    return Le(i, r, n);
  }, {});
};
var ms = Le, ds = ms;
const bs = /* @__PURE__ */ ts(ds);
var Kt = function(e, t) {
  return Kt = Object.setPrototypeOf || { __proto__: [] } instanceof Array && function(n, i) {
    n.__proto__ = i;
  } || function(n, i) {
    for (var r in i)
      Object.prototype.hasOwnProperty.call(i, r) && (n[r] = i[r]);
  }, Kt(e, t);
};
function yt(e, t) {
  if (typeof t != "function" && t !== null)
    throw new TypeError("Class extends value " + String(t) + " is not a constructor or null");
  Kt(e, t);
  function n() {
    this.constructor = e;
  }
  e.prototype = t === null ? Object.create(t) : (n.prototype = t.prototype, new n());
}
var k = function() {
  return k = Object.assign || function(t) {
    for (var n, i = 1, r = arguments.length; i < r; i++) {
      n = arguments[i];
      for (var l in n)
        Object.prototype.hasOwnProperty.call(n, l) && (t[l] = n[l]);
    }
    return t;
  }, k.apply(this, arguments);
};
function jt(e, t, n) {
  if (n || arguments.length === 2)
    for (var i = 0, r = t.length, l; i < r; i++)
      (l || !(i in t)) && (l || (l = Array.prototype.slice.call(t, 0, i)), l[i] = t[i]);
  return e.concat(l || Array.prototype.slice.call(t));
}
var B;
(function(e) {
  e[e.EXPECT_ARGUMENT_CLOSING_BRACE = 1] = "EXPECT_ARGUMENT_CLOSING_BRACE", e[e.EMPTY_ARGUMENT = 2] = "EMPTY_ARGUMENT", e[e.MALFORMED_ARGUMENT = 3] = "MALFORMED_ARGUMENT", e[e.EXPECT_ARGUMENT_TYPE = 4] = "EXPECT_ARGUMENT_TYPE", e[e.INVALID_ARGUMENT_TYPE = 5] = "INVALID_ARGUMENT_TYPE", e[e.EXPECT_ARGUMENT_STYLE = 6] = "EXPECT_ARGUMENT_STYLE", e[e.INVALID_NUMBER_SKELETON = 7] = "INVALID_NUMBER_SKELETON", e[e.INVALID_DATE_TIME_SKELETON = 8] = "INVALID_DATE_TIME_SKELETON", e[e.EXPECT_NUMBER_SKELETON = 9] = "EXPECT_NUMBER_SKELETON", e[e.EXPECT_DATE_TIME_SKELETON = 10] = "EXPECT_DATE_TIME_SKELETON", e[e.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE = 11] = "UNCLOSED_QUOTE_IN_ARGUMENT_STYLE", e[e.EXPECT_SELECT_ARGUMENT_OPTIONS = 12] = "EXPECT_SELECT_ARGUMENT_OPTIONS", e[e.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE = 13] = "EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE = 14] = "INVALID_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR = 15] = "EXPECT_SELECT_ARGUMENT_SELECTOR", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR = 16] = "EXPECT_PLURAL_ARGUMENT_SELECTOR", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT = 17] = "EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT = 18] = "EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT", e[e.INVALID_PLURAL_ARGUMENT_SELECTOR = 19] = "INVALID_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_PLURAL_ARGUMENT_SELECTOR = 20] = "DUPLICATE_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_SELECT_ARGUMENT_SELECTOR = 21] = "DUPLICATE_SELECT_ARGUMENT_SELECTOR", e[e.MISSING_OTHER_CLAUSE = 22] = "MISSING_OTHER_CLAUSE", e[e.INVALID_TAG = 23] = "INVALID_TAG", e[e.INVALID_TAG_NAME = 25] = "INVALID_TAG_NAME", e[e.UNMATCHED_CLOSING_TAG = 26] = "UNMATCHED_CLOSING_TAG", e[e.UNCLOSED_TAG = 27] = "UNCLOSED_TAG";
})(B || (B = {}));
var O;
(function(e) {
  e[e.literal = 0] = "literal", e[e.argument = 1] = "argument", e[e.number = 2] = "number", e[e.date = 3] = "date", e[e.time = 4] = "time", e[e.select = 5] = "select", e[e.plural = 6] = "plural", e[e.pound = 7] = "pound", e[e.tag = 8] = "tag";
})(O || (O = {}));
var Ne;
(function(e) {
  e[e.number = 0] = "number", e[e.dateTime = 1] = "dateTime";
})(Ne || (Ne = {}));
function Dn(e) {
  return e.type === O.literal;
}
function gs(e) {
  return e.type === O.argument;
}
function zi(e) {
  return e.type === O.number;
}
function qi(e) {
  return e.type === O.date;
}
function Xi(e) {
  return e.type === O.time;
}
function Zi(e) {
  return e.type === O.select;
}
function Wi(e) {
  return e.type === O.plural;
}
function ps(e) {
  return e.type === O.pound;
}
function Qi(e) {
  return e.type === O.tag;
}
function Ji(e) {
  return !!(e && typeof e == "object" && e.type === Ne.number);
}
function $t(e) {
  return !!(e && typeof e == "object" && e.type === Ne.dateTime);
}
var Yi = /[ \xA0\u1680\u2000-\u200A\u202F\u205F\u3000]/, vs = /(?:[Eec]{1,6}|G{1,5}|[Qq]{1,5}|(?:[yYur]+|U{1,5})|[ML]{1,5}|d{1,2}|D{1,3}|F{1}|[abB]{1,5}|[hkHK]{1,2}|w{1,2}|W{1}|m{1,2}|s{1,2}|[zZOvVxX]{1,4})(?=([^']*'[^']*')*[^']*$)/g;
function ws(e) {
  var t = {};
  return e.replace(vs, function(n) {
    var i = n.length;
    switch (n[0]) {
      case "G":
        t.era = i === 4 ? "long" : i === 5 ? "narrow" : "short";
        break;
      case "y":
        t.year = i === 2 ? "2-digit" : "numeric";
        break;
      case "Y":
      case "u":
      case "U":
      case "r":
        throw new RangeError("`Y/u/U/r` (year) patterns are not supported, use `y` instead");
      case "q":
      case "Q":
        throw new RangeError("`q/Q` (quarter) patterns are not supported");
      case "M":
      case "L":
        t.month = ["numeric", "2-digit", "short", "long", "narrow"][i - 1];
        break;
      case "w":
      case "W":
        throw new RangeError("`w/W` (week) patterns are not supported");
      case "d":
        t.day = ["numeric", "2-digit"][i - 1];
        break;
      case "D":
      case "F":
      case "g":
        throw new RangeError("`D/F/g` (day) patterns are not supported, use `d` instead");
      case "E":
        t.weekday = i === 4 ? "short" : i === 5 ? "narrow" : "short";
        break;
      case "e":
        if (i < 4)
          throw new RangeError("`e..eee` (weekday) patterns are not supported");
        t.weekday = ["short", "long", "narrow", "short"][i - 4];
        break;
      case "c":
        if (i < 4)
          throw new RangeError("`c..ccc` (weekday) patterns are not supported");
        t.weekday = ["short", "long", "narrow", "short"][i - 4];
        break;
      case "a":
        t.hour12 = !0;
        break;
      case "b":
      case "B":
        throw new RangeError("`b/B` (period) patterns are not supported, use `a` instead");
      case "h":
        t.hourCycle = "h12", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "H":
        t.hourCycle = "h23", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "K":
        t.hourCycle = "h11", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "k":
        t.hourCycle = "h24", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "j":
      case "J":
      case "C":
        throw new RangeError("`j/J/C` (hour) patterns are not supported, use `h/H/K/k` instead");
      case "m":
        t.minute = ["numeric", "2-digit"][i - 1];
        break;
      case "s":
        t.second = ["numeric", "2-digit"][i - 1];
        break;
      case "S":
      case "A":
        throw new RangeError("`S/A` (second) patterns are not supported, use `s` instead");
      case "z":
        t.timeZoneName = i < 4 ? "short" : "long";
        break;
      case "Z":
      case "O":
      case "v":
      case "V":
      case "X":
      case "x":
        throw new RangeError("`Z/O/v/V/X/x` (timeZone) patterns are not supported, use `z` instead");
    }
    return "";
  }), t;
}
var ys = /[\t-\r \x85\u200E\u200F\u2028\u2029]/i;
function Es(e) {
  if (e.length === 0)
    throw new Error("Number skeleton cannot be empty");
  for (var t = e.split(ys).filter(function(h) {
    return h.length > 0;
  }), n = [], i = 0, r = t; i < r.length; i++) {
    var l = r[i], o = l.split("/");
    if (o.length === 0)
      throw new Error("Invalid number skeleton");
    for (var a = o[0], s = o.slice(1), u = 0, f = s; u < f.length; u++) {
      var c = f[u];
      if (c.length === 0)
        throw new Error("Invalid number skeleton");
    }
    n.push({ stem: a, options: s });
  }
  return n;
}
function Ss(e) {
  return e.replace(/^(.*?)-/, "");
}
var Un = /^\.(?:(0+)(\*)?|(#+)|(0+)(#+))$/g, Ki = /^(@+)?(\+|#+)?[rs]?$/g, Ts = /(\*)(0+)|(#+)(0+)|(0+)/g, $i = /^(0+)$/;
function Gn(e) {
  var t = {};
  return e[e.length - 1] === "r" ? t.roundingPriority = "morePrecision" : e[e.length - 1] === "s" && (t.roundingPriority = "lessPrecision"), e.replace(Ki, function(n, i, r) {
    return typeof r != "string" ? (t.minimumSignificantDigits = i.length, t.maximumSignificantDigits = i.length) : r === "+" ? t.minimumSignificantDigits = i.length : i[0] === "#" ? t.maximumSignificantDigits = i.length : (t.minimumSignificantDigits = i.length, t.maximumSignificantDigits = i.length + (typeof r == "string" ? r.length : 0)), "";
  }), t;
}
function er(e) {
  switch (e) {
    case "sign-auto":
      return {
        signDisplay: "auto"
      };
    case "sign-accounting":
    case "()":
      return {
        currencySign: "accounting"
      };
    case "sign-always":
    case "+!":
      return {
        signDisplay: "always"
      };
    case "sign-accounting-always":
    case "()!":
      return {
        signDisplay: "always",
        currencySign: "accounting"
      };
    case "sign-except-zero":
    case "+?":
      return {
        signDisplay: "exceptZero"
      };
    case "sign-accounting-except-zero":
    case "()?":
      return {
        signDisplay: "exceptZero",
        currencySign: "accounting"
      };
    case "sign-never":
    case "+_":
      return {
        signDisplay: "never"
      };
  }
}
function As(e) {
  var t;
  if (e[0] === "E" && e[1] === "E" ? (t = {
    notation: "engineering"
  }, e = e.slice(2)) : e[0] === "E" && (t = {
    notation: "scientific"
  }, e = e.slice(1)), t) {
    var n = e.slice(0, 2);
    if (n === "+!" ? (t.signDisplay = "always", e = e.slice(2)) : n === "+?" && (t.signDisplay = "exceptZero", e = e.slice(2)), !$i.test(e))
      throw new Error("Malformed concise eng/scientific notation");
    t.minimumIntegerDigits = e.length;
  }
  return t;
}
function Fn(e) {
  var t = {}, n = er(e);
  return n || t;
}
function Hs(e) {
  for (var t = {}, n = 0, i = e; n < i.length; n++) {
    var r = i[n];
    switch (r.stem) {
      case "percent":
      case "%":
        t.style = "percent";
        continue;
      case "%x100":
        t.style = "percent", t.scale = 100;
        continue;
      case "currency":
        t.style = "currency", t.currency = r.options[0];
        continue;
      case "group-off":
      case ",_":
        t.useGrouping = !1;
        continue;
      case "precision-integer":
      case ".":
        t.maximumFractionDigits = 0;
        continue;
      case "measure-unit":
      case "unit":
        t.style = "unit", t.unit = Ss(r.options[0]);
        continue;
      case "compact-short":
      case "K":
        t.notation = "compact", t.compactDisplay = "short";
        continue;
      case "compact-long":
      case "KK":
        t.notation = "compact", t.compactDisplay = "long";
        continue;
      case "scientific":
        t = k(k(k({}, t), { notation: "scientific" }), r.options.reduce(function(s, u) {
          return k(k({}, s), Fn(u));
        }, {}));
        continue;
      case "engineering":
        t = k(k(k({}, t), { notation: "engineering" }), r.options.reduce(function(s, u) {
          return k(k({}, s), Fn(u));
        }, {}));
        continue;
      case "notation-simple":
        t.notation = "standard";
        continue;
      case "unit-width-narrow":
        t.currencyDisplay = "narrowSymbol", t.unitDisplay = "narrow";
        continue;
      case "unit-width-short":
        t.currencyDisplay = "code", t.unitDisplay = "short";
        continue;
      case "unit-width-full-name":
        t.currencyDisplay = "name", t.unitDisplay = "long";
        continue;
      case "unit-width-iso-code":
        t.currencyDisplay = "symbol";
        continue;
      case "scale":
        t.scale = parseFloat(r.options[0]);
        continue;
      case "integer-width":
        if (r.options.length > 1)
          throw new RangeError("integer-width stems only accept a single optional option");
        r.options[0].replace(Ts, function(s, u, f, c, h, _) {
          if (u)
            t.minimumIntegerDigits = f.length;
          else {
            if (c && h)
              throw new Error("We currently do not support maximum integer digits");
            if (_)
              throw new Error("We currently do not support exact integer digits");
          }
          return "";
        });
        continue;
    }
    if ($i.test(r.stem)) {
      t.minimumIntegerDigits = r.stem.length;
      continue;
    }
    if (Un.test(r.stem)) {
      if (r.options.length > 1)
        throw new RangeError("Fraction-precision stems only accept a single optional option");
      r.stem.replace(Un, function(s, u, f, c, h, _) {
        return f === "*" ? t.minimumFractionDigits = u.length : c && c[0] === "#" ? t.maximumFractionDigits = c.length : h && _ ? (t.minimumFractionDigits = h.length, t.maximumFractionDigits = h.length + _.length) : (t.minimumFractionDigits = u.length, t.maximumFractionDigits = u.length), "";
      });
      var l = r.options[0];
      l === "w" ? t = k(k({}, t), { trailingZeroDisplay: "stripIfInteger" }) : l && (t = k(k({}, t), Gn(l)));
      continue;
    }
    if (Ki.test(r.stem)) {
      t = k(k({}, t), Gn(r.stem));
      continue;
    }
    var o = er(r.stem);
    o && (t = k(k({}, t), o));
    var a = As(r.stem);
    a && (t = k(k({}, t), a));
  }
  return t;
}
var ct = {
  AX: [
    "H"
  ],
  BQ: [
    "H"
  ],
  CP: [
    "H"
  ],
  CZ: [
    "H"
  ],
  DK: [
    "H"
  ],
  FI: [
    "H"
  ],
  ID: [
    "H"
  ],
  IS: [
    "H"
  ],
  ML: [
    "H"
  ],
  NE: [
    "H"
  ],
  RU: [
    "H"
  ],
  SE: [
    "H"
  ],
  SJ: [
    "H"
  ],
  SK: [
    "H"
  ],
  AS: [
    "h",
    "H"
  ],
  BT: [
    "h",
    "H"
  ],
  DJ: [
    "h",
    "H"
  ],
  ER: [
    "h",
    "H"
  ],
  GH: [
    "h",
    "H"
  ],
  IN: [
    "h",
    "H"
  ],
  LS: [
    "h",
    "H"
  ],
  PG: [
    "h",
    "H"
  ],
  PW: [
    "h",
    "H"
  ],
  SO: [
    "h",
    "H"
  ],
  TO: [
    "h",
    "H"
  ],
  VU: [
    "h",
    "H"
  ],
  WS: [
    "h",
    "H"
  ],
  "001": [
    "H",
    "h"
  ],
  AL: [
    "h",
    "H",
    "hB"
  ],
  TD: [
    "h",
    "H",
    "hB"
  ],
  "ca-ES": [
    "H",
    "h",
    "hB"
  ],
  CF: [
    "H",
    "h",
    "hB"
  ],
  CM: [
    "H",
    "h",
    "hB"
  ],
  "fr-CA": [
    "H",
    "h",
    "hB"
  ],
  "gl-ES": [
    "H",
    "h",
    "hB"
  ],
  "it-CH": [
    "H",
    "h",
    "hB"
  ],
  "it-IT": [
    "H",
    "h",
    "hB"
  ],
  LU: [
    "H",
    "h",
    "hB"
  ],
  NP: [
    "H",
    "h",
    "hB"
  ],
  PF: [
    "H",
    "h",
    "hB"
  ],
  SC: [
    "H",
    "h",
    "hB"
  ],
  SM: [
    "H",
    "h",
    "hB"
  ],
  SN: [
    "H",
    "h",
    "hB"
  ],
  TF: [
    "H",
    "h",
    "hB"
  ],
  VA: [
    "H",
    "h",
    "hB"
  ],
  CY: [
    "h",
    "H",
    "hb",
    "hB"
  ],
  GR: [
    "h",
    "H",
    "hb",
    "hB"
  ],
  CO: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  DO: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  KP: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  KR: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  NA: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  PA: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  PR: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  VE: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  AC: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  AI: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  BW: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  BZ: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  CC: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  CK: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  CX: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  DG: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  FK: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  GB: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  GG: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  GI: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  IE: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  IM: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  IO: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  JE: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  LT: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  MK: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  MN: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  MS: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NF: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NG: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NR: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NU: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  PN: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  SH: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  SX: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  TA: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  ZA: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  "af-ZA": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  AR: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  CL: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  CR: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  CU: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  EA: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-BO": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-BR": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-EC": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-ES": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-GQ": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-PE": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  GT: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  HN: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  IC: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  KG: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  KM: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  LK: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  MA: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  MX: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  NI: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  PY: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  SV: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  UY: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  JP: [
    "H",
    "h",
    "K"
  ],
  AD: [
    "H",
    "hB"
  ],
  AM: [
    "H",
    "hB"
  ],
  AO: [
    "H",
    "hB"
  ],
  AT: [
    "H",
    "hB"
  ],
  AW: [
    "H",
    "hB"
  ],
  BE: [
    "H",
    "hB"
  ],
  BF: [
    "H",
    "hB"
  ],
  BJ: [
    "H",
    "hB"
  ],
  BL: [
    "H",
    "hB"
  ],
  BR: [
    "H",
    "hB"
  ],
  CG: [
    "H",
    "hB"
  ],
  CI: [
    "H",
    "hB"
  ],
  CV: [
    "H",
    "hB"
  ],
  DE: [
    "H",
    "hB"
  ],
  EE: [
    "H",
    "hB"
  ],
  FR: [
    "H",
    "hB"
  ],
  GA: [
    "H",
    "hB"
  ],
  GF: [
    "H",
    "hB"
  ],
  GN: [
    "H",
    "hB"
  ],
  GP: [
    "H",
    "hB"
  ],
  GW: [
    "H",
    "hB"
  ],
  HR: [
    "H",
    "hB"
  ],
  IL: [
    "H",
    "hB"
  ],
  IT: [
    "H",
    "hB"
  ],
  KZ: [
    "H",
    "hB"
  ],
  MC: [
    "H",
    "hB"
  ],
  MD: [
    "H",
    "hB"
  ],
  MF: [
    "H",
    "hB"
  ],
  MQ: [
    "H",
    "hB"
  ],
  MZ: [
    "H",
    "hB"
  ],
  NC: [
    "H",
    "hB"
  ],
  NL: [
    "H",
    "hB"
  ],
  PM: [
    "H",
    "hB"
  ],
  PT: [
    "H",
    "hB"
  ],
  RE: [
    "H",
    "hB"
  ],
  RO: [
    "H",
    "hB"
  ],
  SI: [
    "H",
    "hB"
  ],
  SR: [
    "H",
    "hB"
  ],
  ST: [
    "H",
    "hB"
  ],
  TG: [
    "H",
    "hB"
  ],
  TR: [
    "H",
    "hB"
  ],
  WF: [
    "H",
    "hB"
  ],
  YT: [
    "H",
    "hB"
  ],
  BD: [
    "h",
    "hB",
    "H"
  ],
  PK: [
    "h",
    "hB",
    "H"
  ],
  AZ: [
    "H",
    "hB",
    "h"
  ],
  BA: [
    "H",
    "hB",
    "h"
  ],
  BG: [
    "H",
    "hB",
    "h"
  ],
  CH: [
    "H",
    "hB",
    "h"
  ],
  GE: [
    "H",
    "hB",
    "h"
  ],
  LI: [
    "H",
    "hB",
    "h"
  ],
  ME: [
    "H",
    "hB",
    "h"
  ],
  RS: [
    "H",
    "hB",
    "h"
  ],
  UA: [
    "H",
    "hB",
    "h"
  ],
  UZ: [
    "H",
    "hB",
    "h"
  ],
  XK: [
    "H",
    "hB",
    "h"
  ],
  AG: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  AU: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BB: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BS: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  CA: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  DM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  "en-001": [
    "h",
    "hb",
    "H",
    "hB"
  ],
  FJ: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  FM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GD: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GU: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GY: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  JM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  KI: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  KN: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  KY: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  LC: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  LR: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  MH: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  MP: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  MW: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  NZ: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SB: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SG: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SL: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SS: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SZ: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  TC: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  TT: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  UM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  US: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  VC: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  VG: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  VI: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  ZM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BO: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  EC: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  ES: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  GQ: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  PE: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  AE: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  "ar-001": [
    "h",
    "hB",
    "hb",
    "H"
  ],
  BH: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  DZ: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  EG: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  EH: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  HK: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  IQ: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  JO: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  KW: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  LB: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  LY: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  MO: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  MR: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  OM: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  PH: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  PS: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  QA: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  SA: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  SD: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  SY: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  TN: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  YE: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  AF: [
    "H",
    "hb",
    "hB",
    "h"
  ],
  LA: [
    "H",
    "hb",
    "hB",
    "h"
  ],
  CN: [
    "H",
    "hB",
    "hb",
    "h"
  ],
  LV: [
    "H",
    "hB",
    "hb",
    "h"
  ],
  TL: [
    "H",
    "hB",
    "hb",
    "h"
  ],
  "zu-ZA": [
    "H",
    "hB",
    "hb",
    "h"
  ],
  CD: [
    "hB",
    "H"
  ],
  IR: [
    "hB",
    "H"
  ],
  "hi-IN": [
    "hB",
    "h",
    "H"
  ],
  "kn-IN": [
    "hB",
    "h",
    "H"
  ],
  "ml-IN": [
    "hB",
    "h",
    "H"
  ],
  "te-IN": [
    "hB",
    "h",
    "H"
  ],
  KH: [
    "hB",
    "h",
    "H",
    "hb"
  ],
  "ta-IN": [
    "hB",
    "h",
    "hb",
    "H"
  ],
  BN: [
    "hb",
    "hB",
    "h",
    "H"
  ],
  MY: [
    "hb",
    "hB",
    "h",
    "H"
  ],
  ET: [
    "hB",
    "hb",
    "h",
    "H"
  ],
  "gu-IN": [
    "hB",
    "hb",
    "h",
    "H"
  ],
  "mr-IN": [
    "hB",
    "hb",
    "h",
    "H"
  ],
  "pa-IN": [
    "hB",
    "hb",
    "h",
    "H"
  ],
  TW: [
    "hB",
    "hb",
    "h",
    "H"
  ],
  KE: [
    "hB",
    "hb",
    "H",
    "h"
  ],
  MM: [
    "hB",
    "hb",
    "H",
    "h"
  ],
  TZ: [
    "hB",
    "hb",
    "H",
    "h"
  ],
  UG: [
    "hB",
    "hb",
    "H",
    "h"
  ]
};
function Bs(e, t) {
  for (var n = "", i = 0; i < e.length; i++) {
    var r = e.charAt(i);
    if (r === "j") {
      for (var l = 0; i + 1 < e.length && e.charAt(i + 1) === r; )
        l++, i++;
      var o = 1 + (l & 1), a = l < 2 ? 1 : 3 + (l >> 1), s = "a", u = Cs(t);
      for ((u == "H" || u == "k") && (a = 0); a-- > 0; )
        n += s;
      for (; o-- > 0; )
        n = u + n;
    } else
      r === "J" ? n += "H" : n += r;
  }
  return n;
}
function Cs(e) {
  var t = e.hourCycle;
  if (t === void 0 && // @ts-ignore hourCycle(s) is not identified yet
  e.hourCycles && // @ts-ignore
  e.hourCycles.length && (t = e.hourCycles[0]), t)
    switch (t) {
      case "h24":
        return "k";
      case "h23":
        return "H";
      case "h12":
        return "h";
      case "h11":
        return "K";
      default:
        throw new Error("Invalid hourCycle");
    }
  var n = e.language, i;
  n !== "root" && (i = e.maximize().region);
  var r = ct[i || ""] || ct[n || ""] || ct["".concat(n, "-001")] || ct["001"];
  return r[0];
}
var Vt, Ps = new RegExp("^".concat(Yi.source, "*")), Is = new RegExp("".concat(Yi.source, "*$"));
function P(e, t) {
  return { start: e, end: t };
}
var ks = !!String.prototype.startsWith, Ls = !!String.fromCodePoint, Ns = !!Object.fromEntries, Os = !!String.prototype.codePointAt, Ms = !!String.prototype.trimStart, Rs = !!String.prototype.trimEnd, Ds = !!Number.isSafeInteger, Us = Ds ? Number.isSafeInteger : function(e) {
  return typeof e == "number" && isFinite(e) && Math.floor(e) === e && Math.abs(e) <= 9007199254740991;
}, en = !0;
try {
  var Gs = nr("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  en = ((Vt = Gs.exec("a")) === null || Vt === void 0 ? void 0 : Vt[0]) === "a";
} catch {
  en = !1;
}
var xn = ks ? (
  // Native
  function(t, n, i) {
    return t.startsWith(n, i);
  }
) : (
  // For IE11
  function(t, n, i) {
    return t.slice(i, i + n.length) === n;
  }
), tn = Ls ? String.fromCodePoint : (
  // IE11
  function() {
    for (var t = [], n = 0; n < arguments.length; n++)
      t[n] = arguments[n];
    for (var i = "", r = t.length, l = 0, o; r > l; ) {
      if (o = t[l++], o > 1114111)
        throw RangeError(o + " is not a valid code point");
      i += o < 65536 ? String.fromCharCode(o) : String.fromCharCode(((o -= 65536) >> 10) + 55296, o % 1024 + 56320);
    }
    return i;
  }
), jn = (
  // native
  Ns ? Object.fromEntries : (
    // Ponyfill
    function(t) {
      for (var n = {}, i = 0, r = t; i < r.length; i++) {
        var l = r[i], o = l[0], a = l[1];
        n[o] = a;
      }
      return n;
    }
  )
), tr = Os ? (
  // Native
  function(t, n) {
    return t.codePointAt(n);
  }
) : (
  // IE 11
  function(t, n) {
    var i = t.length;
    if (!(n < 0 || n >= i)) {
      var r = t.charCodeAt(n), l;
      return r < 55296 || r > 56319 || n + 1 === i || (l = t.charCodeAt(n + 1)) < 56320 || l > 57343 ? r : (r - 55296 << 10) + (l - 56320) + 65536;
    }
  }
), Fs = Ms ? (
  // Native
  function(t) {
    return t.trimStart();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Ps, "");
  }
), xs = Rs ? (
  // Native
  function(t) {
    return t.trimEnd();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Is, "");
  }
);
function nr(e, t) {
  return new RegExp(e, t);
}
var nn;
if (en) {
  var Vn = nr("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  nn = function(t, n) {
    var i;
    Vn.lastIndex = n;
    var r = Vn.exec(t);
    return (i = r[1]) !== null && i !== void 0 ? i : "";
  };
} else
  nn = function(t, n) {
    for (var i = []; ; ) {
      var r = tr(t, n);
      if (r === void 0 || ir(r) || qs(r))
        break;
      i.push(r), n += r >= 65536 ? 2 : 1;
    }
    return tn.apply(void 0, i);
  };
var js = (
  /** @class */
  function() {
    function e(t, n) {
      n === void 0 && (n = {}), this.message = t, this.position = { offset: 0, line: 1, column: 1 }, this.ignoreTag = !!n.ignoreTag, this.locale = n.locale, this.requiresOtherClause = !!n.requiresOtherClause, this.shouldParseSkeletons = !!n.shouldParseSkeletons;
    }
    return e.prototype.parse = function() {
      if (this.offset() !== 0)
        throw Error("parser can only be used once");
      return this.parseMessage(0, "", !1);
    }, e.prototype.parseMessage = function(t, n, i) {
      for (var r = []; !this.isEOF(); ) {
        var l = this.char();
        if (l === 123) {
          var o = this.parseArgument(t, i);
          if (o.err)
            return o;
          r.push(o.val);
        } else {
          if (l === 125 && t > 0)
            break;
          if (l === 35 && (n === "plural" || n === "selectordinal")) {
            var a = this.clonePosition();
            this.bump(), r.push({
              type: O.pound,
              location: P(a, this.clonePosition())
            });
          } else if (l === 60 && !this.ignoreTag && this.peek() === 47) {
            if (i)
              break;
            return this.error(B.UNMATCHED_CLOSING_TAG, P(this.clonePosition(), this.clonePosition()));
          } else if (l === 60 && !this.ignoreTag && rn(this.peek() || 0)) {
            var o = this.parseTag(t, n);
            if (o.err)
              return o;
            r.push(o.val);
          } else {
            var o = this.parseLiteral(t, n);
            if (o.err)
              return o;
            r.push(o.val);
          }
        }
      }
      return { val: r, err: null };
    }, e.prototype.parseTag = function(t, n) {
      var i = this.clonePosition();
      this.bump();
      var r = this.parseTagName();
      if (this.bumpSpace(), this.bumpIf("/>"))
        return {
          val: {
            type: O.literal,
            value: "<".concat(r, "/>"),
            location: P(i, this.clonePosition())
          },
          err: null
        };
      if (this.bumpIf(">")) {
        var l = this.parseMessage(t + 1, n, !0);
        if (l.err)
          return l;
        var o = l.val, a = this.clonePosition();
        if (this.bumpIf("</")) {
          if (this.isEOF() || !rn(this.char()))
            return this.error(B.INVALID_TAG, P(a, this.clonePosition()));
          var s = this.clonePosition(), u = this.parseTagName();
          return r !== u ? this.error(B.UNMATCHED_CLOSING_TAG, P(s, this.clonePosition())) : (this.bumpSpace(), this.bumpIf(">") ? {
            val: {
              type: O.tag,
              value: r,
              children: o,
              location: P(i, this.clonePosition())
            },
            err: null
          } : this.error(B.INVALID_TAG, P(a, this.clonePosition())));
        } else
          return this.error(B.UNCLOSED_TAG, P(i, this.clonePosition()));
      } else
        return this.error(B.INVALID_TAG, P(i, this.clonePosition()));
    }, e.prototype.parseTagName = function() {
      var t = this.offset();
      for (this.bump(); !this.isEOF() && zs(this.char()); )
        this.bump();
      return this.message.slice(t, this.offset());
    }, e.prototype.parseLiteral = function(t, n) {
      for (var i = this.clonePosition(), r = ""; ; ) {
        var l = this.tryParseQuote(n);
        if (l) {
          r += l;
          continue;
        }
        var o = this.tryParseUnquoted(t, n);
        if (o) {
          r += o;
          continue;
        }
        var a = this.tryParseLeftAngleBracket();
        if (a) {
          r += a;
          continue;
        }
        break;
      }
      var s = P(i, this.clonePosition());
      return {
        val: { type: O.literal, value: r, location: s },
        err: null
      };
    }, e.prototype.tryParseLeftAngleBracket = function() {
      return !this.isEOF() && this.char() === 60 && (this.ignoreTag || // If at the opening tag or closing tag position, bail.
      !Vs(this.peek() || 0)) ? (this.bump(), "<") : null;
    }, e.prototype.tryParseQuote = function(t) {
      if (this.isEOF() || this.char() !== 39)
        return null;
      switch (this.peek()) {
        case 39:
          return this.bump(), this.bump(), "'";
        case 123:
        case 60:
        case 62:
        case 125:
          break;
        case 35:
          if (t === "plural" || t === "selectordinal")
            break;
          return null;
        default:
          return null;
      }
      this.bump();
      var n = [this.char()];
      for (this.bump(); !this.isEOF(); ) {
        var i = this.char();
        if (i === 39)
          if (this.peek() === 39)
            n.push(39), this.bump();
          else {
            this.bump();
            break;
          }
        else
          n.push(i);
        this.bump();
      }
      return tn.apply(void 0, n);
    }, e.prototype.tryParseUnquoted = function(t, n) {
      if (this.isEOF())
        return null;
      var i = this.char();
      return i === 60 || i === 123 || i === 35 && (n === "plural" || n === "selectordinal") || i === 125 && t > 0 ? null : (this.bump(), tn(i));
    }, e.prototype.parseArgument = function(t, n) {
      var i = this.clonePosition();
      if (this.bump(), this.bumpSpace(), this.isEOF())
        return this.error(B.EXPECT_ARGUMENT_CLOSING_BRACE, P(i, this.clonePosition()));
      if (this.char() === 125)
        return this.bump(), this.error(B.EMPTY_ARGUMENT, P(i, this.clonePosition()));
      var r = this.parseIdentifierIfPossible().value;
      if (!r)
        return this.error(B.MALFORMED_ARGUMENT, P(i, this.clonePosition()));
      if (this.bumpSpace(), this.isEOF())
        return this.error(B.EXPECT_ARGUMENT_CLOSING_BRACE, P(i, this.clonePosition()));
      switch (this.char()) {
        case 125:
          return this.bump(), {
            val: {
              type: O.argument,
              // value does not include the opening and closing braces.
              value: r,
              location: P(i, this.clonePosition())
            },
            err: null
          };
        case 44:
          return this.bump(), this.bumpSpace(), this.isEOF() ? this.error(B.EXPECT_ARGUMENT_CLOSING_BRACE, P(i, this.clonePosition())) : this.parseArgumentOptions(t, n, r, i);
        default:
          return this.error(B.MALFORMED_ARGUMENT, P(i, this.clonePosition()));
      }
    }, e.prototype.parseIdentifierIfPossible = function() {
      var t = this.clonePosition(), n = this.offset(), i = nn(this.message, n), r = n + i.length;
      this.bumpTo(r);
      var l = this.clonePosition(), o = P(t, l);
      return { value: i, location: o };
    }, e.prototype.parseArgumentOptions = function(t, n, i, r) {
      var l, o = this.clonePosition(), a = this.parseIdentifierIfPossible().value, s = this.clonePosition();
      switch (a) {
        case "":
          return this.error(B.EXPECT_ARGUMENT_TYPE, P(o, s));
        case "number":
        case "date":
        case "time": {
          this.bumpSpace();
          var u = null;
          if (this.bumpIf(",")) {
            this.bumpSpace();
            var f = this.clonePosition(), c = this.parseSimpleArgStyleIfPossible();
            if (c.err)
              return c;
            var h = xs(c.val);
            if (h.length === 0)
              return this.error(B.EXPECT_ARGUMENT_STYLE, P(this.clonePosition(), this.clonePosition()));
            var _ = P(f, this.clonePosition());
            u = { style: h, styleLocation: _ };
          }
          var b = this.tryParseArgumentClose(r);
          if (b.err)
            return b;
          var T = P(r, this.clonePosition());
          if (u && xn(u == null ? void 0 : u.style, "::", 0)) {
            var y = Fs(u.style.slice(2));
            if (a === "number") {
              var c = this.parseNumberSkeletonFromString(y, u.styleLocation);
              return c.err ? c : {
                val: { type: O.number, value: i, location: T, style: c.val },
                err: null
              };
            } else {
              if (y.length === 0)
                return this.error(B.EXPECT_DATE_TIME_SKELETON, T);
              var C = y;
              this.locale && (C = Bs(y, this.locale));
              var h = {
                type: Ne.dateTime,
                pattern: C,
                location: u.styleLocation,
                parsedOptions: this.shouldParseSkeletons ? ws(C) : {}
              }, E = a === "date" ? O.date : O.time;
              return {
                val: { type: E, value: i, location: T, style: h },
                err: null
              };
            }
          }
          return {
            val: {
              type: a === "number" ? O.number : a === "date" ? O.date : O.time,
              value: i,
              location: T,
              style: (l = u == null ? void 0 : u.style) !== null && l !== void 0 ? l : null
            },
            err: null
          };
        }
        case "plural":
        case "selectordinal":
        case "select": {
          var m = this.clonePosition();
          if (this.bumpSpace(), !this.bumpIf(","))
            return this.error(B.EXPECT_SELECT_ARGUMENT_OPTIONS, P(m, k({}, m)));
          this.bumpSpace();
          var g = this.parseIdentifierIfPossible(), p = 0;
          if (a !== "select" && g.value === "offset") {
            if (!this.bumpIf(":"))
              return this.error(B.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, P(this.clonePosition(), this.clonePosition()));
            this.bumpSpace();
            var c = this.tryParseDecimalInteger(B.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, B.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE);
            if (c.err)
              return c;
            this.bumpSpace(), g = this.parseIdentifierIfPossible(), p = c.val;
          }
          var N = this.tryParsePluralOrSelectOptions(t, a, n, g);
          if (N.err)
            return N;
          var b = this.tryParseArgumentClose(r);
          if (b.err)
            return b;
          var G = P(r, this.clonePosition());
          return a === "select" ? {
            val: {
              type: O.select,
              value: i,
              options: jn(N.val),
              location: G
            },
            err: null
          } : {
            val: {
              type: O.plural,
              value: i,
              options: jn(N.val),
              offset: p,
              pluralType: a === "plural" ? "cardinal" : "ordinal",
              location: G
            },
            err: null
          };
        }
        default:
          return this.error(B.INVALID_ARGUMENT_TYPE, P(o, s));
      }
    }, e.prototype.tryParseArgumentClose = function(t) {
      return this.isEOF() || this.char() !== 125 ? this.error(B.EXPECT_ARGUMENT_CLOSING_BRACE, P(t, this.clonePosition())) : (this.bump(), { val: !0, err: null });
    }, e.prototype.parseSimpleArgStyleIfPossible = function() {
      for (var t = 0, n = this.clonePosition(); !this.isEOF(); ) {
        var i = this.char();
        switch (i) {
          case 39: {
            this.bump();
            var r = this.clonePosition();
            if (!this.bumpUntil("'"))
              return this.error(B.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE, P(r, this.clonePosition()));
            this.bump();
            break;
          }
          case 123: {
            t += 1, this.bump();
            break;
          }
          case 125: {
            if (t > 0)
              t -= 1;
            else
              return {
                val: this.message.slice(n.offset, this.offset()),
                err: null
              };
            break;
          }
          default:
            this.bump();
            break;
        }
      }
      return {
        val: this.message.slice(n.offset, this.offset()),
        err: null
      };
    }, e.prototype.parseNumberSkeletonFromString = function(t, n) {
      var i = [];
      try {
        i = Es(t);
      } catch {
        return this.error(B.INVALID_NUMBER_SKELETON, n);
      }
      return {
        val: {
          type: Ne.number,
          tokens: i,
          location: n,
          parsedOptions: this.shouldParseSkeletons ? Hs(i) : {}
        },
        err: null
      };
    }, e.prototype.tryParsePluralOrSelectOptions = function(t, n, i, r) {
      for (var l, o = !1, a = [], s = /* @__PURE__ */ new Set(), u = r.value, f = r.location; ; ) {
        if (u.length === 0) {
          var c = this.clonePosition();
          if (n !== "select" && this.bumpIf("=")) {
            var h = this.tryParseDecimalInteger(B.EXPECT_PLURAL_ARGUMENT_SELECTOR, B.INVALID_PLURAL_ARGUMENT_SELECTOR);
            if (h.err)
              return h;
            f = P(c, this.clonePosition()), u = this.message.slice(c.offset, this.offset());
          } else
            break;
        }
        if (s.has(u))
          return this.error(n === "select" ? B.DUPLICATE_SELECT_ARGUMENT_SELECTOR : B.DUPLICATE_PLURAL_ARGUMENT_SELECTOR, f);
        u === "other" && (o = !0), this.bumpSpace();
        var _ = this.clonePosition();
        if (!this.bumpIf("{"))
          return this.error(n === "select" ? B.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT : B.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT, P(this.clonePosition(), this.clonePosition()));
        var b = this.parseMessage(t + 1, n, i);
        if (b.err)
          return b;
        var T = this.tryParseArgumentClose(_);
        if (T.err)
          return T;
        a.push([
          u,
          {
            value: b.val,
            location: P(_, this.clonePosition())
          }
        ]), s.add(u), this.bumpSpace(), l = this.parseIdentifierIfPossible(), u = l.value, f = l.location;
      }
      return a.length === 0 ? this.error(n === "select" ? B.EXPECT_SELECT_ARGUMENT_SELECTOR : B.EXPECT_PLURAL_ARGUMENT_SELECTOR, P(this.clonePosition(), this.clonePosition())) : this.requiresOtherClause && !o ? this.error(B.MISSING_OTHER_CLAUSE, P(this.clonePosition(), this.clonePosition())) : { val: a, err: null };
    }, e.prototype.tryParseDecimalInteger = function(t, n) {
      var i = 1, r = this.clonePosition();
      this.bumpIf("+") || this.bumpIf("-") && (i = -1);
      for (var l = !1, o = 0; !this.isEOF(); ) {
        var a = this.char();
        if (a >= 48 && a <= 57)
          l = !0, o = o * 10 + (a - 48), this.bump();
        else
          break;
      }
      var s = P(r, this.clonePosition());
      return l ? (o *= i, Us(o) ? { val: o, err: null } : this.error(n, s)) : this.error(t, s);
    }, e.prototype.offset = function() {
      return this.position.offset;
    }, e.prototype.isEOF = function() {
      return this.offset() === this.message.length;
    }, e.prototype.clonePosition = function() {
      return {
        offset: this.position.offset,
        line: this.position.line,
        column: this.position.column
      };
    }, e.prototype.char = function() {
      var t = this.position.offset;
      if (t >= this.message.length)
        throw Error("out of bound");
      var n = tr(this.message, t);
      if (n === void 0)
        throw Error("Offset ".concat(t, " is at invalid UTF-16 code unit boundary"));
      return n;
    }, e.prototype.error = function(t, n) {
      return {
        val: null,
        err: {
          kind: t,
          message: this.message,
          location: n
        }
      };
    }, e.prototype.bump = function() {
      if (!this.isEOF()) {
        var t = this.char();
        t === 10 ? (this.position.line += 1, this.position.column = 1, this.position.offset += 1) : (this.position.column += 1, this.position.offset += t < 65536 ? 1 : 2);
      }
    }, e.prototype.bumpIf = function(t) {
      if (xn(this.message, t, this.offset())) {
        for (var n = 0; n < t.length; n++)
          this.bump();
        return !0;
      }
      return !1;
    }, e.prototype.bumpUntil = function(t) {
      var n = this.offset(), i = this.message.indexOf(t, n);
      return i >= 0 ? (this.bumpTo(i), !0) : (this.bumpTo(this.message.length), !1);
    }, e.prototype.bumpTo = function(t) {
      if (this.offset() > t)
        throw Error("targetOffset ".concat(t, " must be greater than or equal to the current offset ").concat(this.offset()));
      for (t = Math.min(t, this.message.length); ; ) {
        var n = this.offset();
        if (n === t)
          break;
        if (n > t)
          throw Error("targetOffset ".concat(t, " is at invalid UTF-16 code unit boundary"));
        if (this.bump(), this.isEOF())
          break;
      }
    }, e.prototype.bumpSpace = function() {
      for (; !this.isEOF() && ir(this.char()); )
        this.bump();
    }, e.prototype.peek = function() {
      if (this.isEOF())
        return null;
      var t = this.char(), n = this.offset(), i = this.message.charCodeAt(n + (t >= 65536 ? 2 : 1));
      return i ?? null;
    }, e;
  }()
);
function rn(e) {
  return e >= 97 && e <= 122 || e >= 65 && e <= 90;
}
function Vs(e) {
  return rn(e) || e === 47;
}
function zs(e) {
  return e === 45 || e === 46 || e >= 48 && e <= 57 || e === 95 || e >= 97 && e <= 122 || e >= 65 && e <= 90 || e == 183 || e >= 192 && e <= 214 || e >= 216 && e <= 246 || e >= 248 && e <= 893 || e >= 895 && e <= 8191 || e >= 8204 && e <= 8205 || e >= 8255 && e <= 8256 || e >= 8304 && e <= 8591 || e >= 11264 && e <= 12271 || e >= 12289 && e <= 55295 || e >= 63744 && e <= 64975 || e >= 65008 && e <= 65533 || e >= 65536 && e <= 983039;
}
function ir(e) {
  return e >= 9 && e <= 13 || e === 32 || e === 133 || e >= 8206 && e <= 8207 || e === 8232 || e === 8233;
}
function qs(e) {
  return e >= 33 && e <= 35 || e === 36 || e >= 37 && e <= 39 || e === 40 || e === 41 || e === 42 || e === 43 || e === 44 || e === 45 || e >= 46 && e <= 47 || e >= 58 && e <= 59 || e >= 60 && e <= 62 || e >= 63 && e <= 64 || e === 91 || e === 92 || e === 93 || e === 94 || e === 96 || e === 123 || e === 124 || e === 125 || e === 126 || e === 161 || e >= 162 && e <= 165 || e === 166 || e === 167 || e === 169 || e === 171 || e === 172 || e === 174 || e === 176 || e === 177 || e === 182 || e === 187 || e === 191 || e === 215 || e === 247 || e >= 8208 && e <= 8213 || e >= 8214 && e <= 8215 || e === 8216 || e === 8217 || e === 8218 || e >= 8219 && e <= 8220 || e === 8221 || e === 8222 || e === 8223 || e >= 8224 && e <= 8231 || e >= 8240 && e <= 8248 || e === 8249 || e === 8250 || e >= 8251 && e <= 8254 || e >= 8257 && e <= 8259 || e === 8260 || e === 8261 || e === 8262 || e >= 8263 && e <= 8273 || e === 8274 || e === 8275 || e >= 8277 && e <= 8286 || e >= 8592 && e <= 8596 || e >= 8597 && e <= 8601 || e >= 8602 && e <= 8603 || e >= 8604 && e <= 8607 || e === 8608 || e >= 8609 && e <= 8610 || e === 8611 || e >= 8612 && e <= 8613 || e === 8614 || e >= 8615 && e <= 8621 || e === 8622 || e >= 8623 && e <= 8653 || e >= 8654 && e <= 8655 || e >= 8656 && e <= 8657 || e === 8658 || e === 8659 || e === 8660 || e >= 8661 && e <= 8691 || e >= 8692 && e <= 8959 || e >= 8960 && e <= 8967 || e === 8968 || e === 8969 || e === 8970 || e === 8971 || e >= 8972 && e <= 8991 || e >= 8992 && e <= 8993 || e >= 8994 && e <= 9e3 || e === 9001 || e === 9002 || e >= 9003 && e <= 9083 || e === 9084 || e >= 9085 && e <= 9114 || e >= 9115 && e <= 9139 || e >= 9140 && e <= 9179 || e >= 9180 && e <= 9185 || e >= 9186 && e <= 9254 || e >= 9255 && e <= 9279 || e >= 9280 && e <= 9290 || e >= 9291 && e <= 9311 || e >= 9472 && e <= 9654 || e === 9655 || e >= 9656 && e <= 9664 || e === 9665 || e >= 9666 && e <= 9719 || e >= 9720 && e <= 9727 || e >= 9728 && e <= 9838 || e === 9839 || e >= 9840 && e <= 10087 || e === 10088 || e === 10089 || e === 10090 || e === 10091 || e === 10092 || e === 10093 || e === 10094 || e === 10095 || e === 10096 || e === 10097 || e === 10098 || e === 10099 || e === 10100 || e === 10101 || e >= 10132 && e <= 10175 || e >= 10176 && e <= 10180 || e === 10181 || e === 10182 || e >= 10183 && e <= 10213 || e === 10214 || e === 10215 || e === 10216 || e === 10217 || e === 10218 || e === 10219 || e === 10220 || e === 10221 || e === 10222 || e === 10223 || e >= 10224 && e <= 10239 || e >= 10240 && e <= 10495 || e >= 10496 && e <= 10626 || e === 10627 || e === 10628 || e === 10629 || e === 10630 || e === 10631 || e === 10632 || e === 10633 || e === 10634 || e === 10635 || e === 10636 || e === 10637 || e === 10638 || e === 10639 || e === 10640 || e === 10641 || e === 10642 || e === 10643 || e === 10644 || e === 10645 || e === 10646 || e === 10647 || e === 10648 || e >= 10649 && e <= 10711 || e === 10712 || e === 10713 || e === 10714 || e === 10715 || e >= 10716 && e <= 10747 || e === 10748 || e === 10749 || e >= 10750 && e <= 11007 || e >= 11008 && e <= 11055 || e >= 11056 && e <= 11076 || e >= 11077 && e <= 11078 || e >= 11079 && e <= 11084 || e >= 11085 && e <= 11123 || e >= 11124 && e <= 11125 || e >= 11126 && e <= 11157 || e === 11158 || e >= 11159 && e <= 11263 || e >= 11776 && e <= 11777 || e === 11778 || e === 11779 || e === 11780 || e === 11781 || e >= 11782 && e <= 11784 || e === 11785 || e === 11786 || e === 11787 || e === 11788 || e === 11789 || e >= 11790 && e <= 11798 || e === 11799 || e >= 11800 && e <= 11801 || e === 11802 || e === 11803 || e === 11804 || e === 11805 || e >= 11806 && e <= 11807 || e === 11808 || e === 11809 || e === 11810 || e === 11811 || e === 11812 || e === 11813 || e === 11814 || e === 11815 || e === 11816 || e === 11817 || e >= 11818 && e <= 11822 || e === 11823 || e >= 11824 && e <= 11833 || e >= 11834 && e <= 11835 || e >= 11836 && e <= 11839 || e === 11840 || e === 11841 || e === 11842 || e >= 11843 && e <= 11855 || e >= 11856 && e <= 11857 || e === 11858 || e >= 11859 && e <= 11903 || e >= 12289 && e <= 12291 || e === 12296 || e === 12297 || e === 12298 || e === 12299 || e === 12300 || e === 12301 || e === 12302 || e === 12303 || e === 12304 || e === 12305 || e >= 12306 && e <= 12307 || e === 12308 || e === 12309 || e === 12310 || e === 12311 || e === 12312 || e === 12313 || e === 12314 || e === 12315 || e === 12316 || e === 12317 || e >= 12318 && e <= 12319 || e === 12320 || e === 12336 || e === 64830 || e === 64831 || e >= 65093 && e <= 65094;
}
function ln(e) {
  e.forEach(function(t) {
    if (delete t.location, Zi(t) || Wi(t))
      for (var n in t.options)
        delete t.options[n].location, ln(t.options[n].value);
    else
      zi(t) && Ji(t.style) || (qi(t) || Xi(t)) && $t(t.style) ? delete t.style.location : Qi(t) && ln(t.children);
  });
}
function Xs(e, t) {
  t === void 0 && (t = {}), t = k({ shouldParseSkeletons: !0, requiresOtherClause: !0 }, t);
  var n = new js(e, t).parse();
  if (n.err) {
    var i = SyntaxError(B[n.err.kind]);
    throw i.location = n.err.location, i.originalMessage = n.err.message, i;
  }
  return t != null && t.captureLocation || ln(n.val), n.val;
}
function zt(e, t) {
  var n = t && t.cache ? t.cache : Ks, i = t && t.serializer ? t.serializer : Ys, r = t && t.strategy ? t.strategy : Ws;
  return r(e, {
    cache: n,
    serializer: i
  });
}
function Zs(e) {
  return e == null || typeof e == "number" || typeof e == "boolean";
}
function rr(e, t, n, i) {
  var r = Zs(i) ? i : n(i), l = t.get(r);
  return typeof l > "u" && (l = e.call(this, i), t.set(r, l)), l;
}
function lr(e, t, n) {
  var i = Array.prototype.slice.call(arguments, 3), r = n(i), l = t.get(r);
  return typeof l > "u" && (l = e.apply(this, i), t.set(r, l)), l;
}
function dn(e, t, n, i, r) {
  return n.bind(t, e, i, r);
}
function Ws(e, t) {
  var n = e.length === 1 ? rr : lr;
  return dn(e, this, n, t.cache.create(), t.serializer);
}
function Qs(e, t) {
  return dn(e, this, lr, t.cache.create(), t.serializer);
}
function Js(e, t) {
  return dn(e, this, rr, t.cache.create(), t.serializer);
}
var Ys = function() {
  return JSON.stringify(arguments);
};
function bn() {
  this.cache = /* @__PURE__ */ Object.create(null);
}
bn.prototype.get = function(e) {
  return this.cache[e];
};
bn.prototype.set = function(e, t) {
  this.cache[e] = t;
};
var Ks = {
  create: function() {
    return new bn();
  }
}, qt = {
  variadic: Qs,
  monadic: Js
}, Oe;
(function(e) {
  e.MISSING_VALUE = "MISSING_VALUE", e.INVALID_VALUE = "INVALID_VALUE", e.MISSING_INTL_API = "MISSING_INTL_API";
})(Oe || (Oe = {}));
var Et = (
  /** @class */
  function(e) {
    yt(t, e);
    function t(n, i, r) {
      var l = e.call(this, n) || this;
      return l.code = i, l.originalMessage = r, l;
    }
    return t.prototype.toString = function() {
      return "[formatjs Error: ".concat(this.code, "] ").concat(this.message);
    }, t;
  }(Error)
), zn = (
  /** @class */
  function(e) {
    yt(t, e);
    function t(n, i, r, l) {
      return e.call(this, 'Invalid values for "'.concat(n, '": "').concat(i, '". Options are "').concat(Object.keys(r).join('", "'), '"'), Oe.INVALID_VALUE, l) || this;
    }
    return t;
  }(Et)
), $s = (
  /** @class */
  function(e) {
    yt(t, e);
    function t(n, i, r) {
      return e.call(this, 'Value for "'.concat(n, '" must be of type ').concat(i), Oe.INVALID_VALUE, r) || this;
    }
    return t;
  }(Et)
), ea = (
  /** @class */
  function(e) {
    yt(t, e);
    function t(n, i) {
      return e.call(this, 'The intl string context variable "'.concat(n, '" was not provided to the string "').concat(i, '"'), Oe.MISSING_VALUE, i) || this;
    }
    return t;
  }(Et)
), j;
(function(e) {
  e[e.literal = 0] = "literal", e[e.object = 1] = "object";
})(j || (j = {}));
function ta(e) {
  return e.length < 2 ? e : e.reduce(function(t, n) {
    var i = t[t.length - 1];
    return !i || i.type !== j.literal || n.type !== j.literal ? t.push(n) : i.value += n.value, t;
  }, []);
}
function na(e) {
  return typeof e == "function";
}
function dt(e, t, n, i, r, l, o) {
  if (e.length === 1 && Dn(e[0]))
    return [
      {
        type: j.literal,
        value: e[0].value
      }
    ];
  for (var a = [], s = 0, u = e; s < u.length; s++) {
    var f = u[s];
    if (Dn(f)) {
      a.push({
        type: j.literal,
        value: f.value
      });
      continue;
    }
    if (ps(f)) {
      typeof l == "number" && a.push({
        type: j.literal,
        value: n.getNumberFormat(t).format(l)
      });
      continue;
    }
    var c = f.value;
    if (!(r && c in r))
      throw new ea(c, o);
    var h = r[c];
    if (gs(f)) {
      (!h || typeof h == "string" || typeof h == "number") && (h = typeof h == "string" || typeof h == "number" ? String(h) : ""), a.push({
        type: typeof h == "string" ? j.literal : j.object,
        value: h
      });
      continue;
    }
    if (qi(f)) {
      var _ = typeof f.style == "string" ? i.date[f.style] : $t(f.style) ? f.style.parsedOptions : void 0;
      a.push({
        type: j.literal,
        value: n.getDateTimeFormat(t, _).format(h)
      });
      continue;
    }
    if (Xi(f)) {
      var _ = typeof f.style == "string" ? i.time[f.style] : $t(f.style) ? f.style.parsedOptions : i.time.medium;
      a.push({
        type: j.literal,
        value: n.getDateTimeFormat(t, _).format(h)
      });
      continue;
    }
    if (zi(f)) {
      var _ = typeof f.style == "string" ? i.number[f.style] : Ji(f.style) ? f.style.parsedOptions : void 0;
      _ && _.scale && (h = h * (_.scale || 1)), a.push({
        type: j.literal,
        value: n.getNumberFormat(t, _).format(h)
      });
      continue;
    }
    if (Qi(f)) {
      var b = f.children, T = f.value, y = r[T];
      if (!na(y))
        throw new $s(T, "function", o);
      var C = dt(b, t, n, i, r, l), E = y(C.map(function(p) {
        return p.value;
      }));
      Array.isArray(E) || (E = [E]), a.push.apply(a, E.map(function(p) {
        return {
          type: typeof p == "string" ? j.literal : j.object,
          value: p
        };
      }));
    }
    if (Zi(f)) {
      var m = f.options[h] || f.options.other;
      if (!m)
        throw new zn(f.value, h, Object.keys(f.options), o);
      a.push.apply(a, dt(m.value, t, n, i, r));
      continue;
    }
    if (Wi(f)) {
      var m = f.options["=".concat(h)];
      if (!m) {
        if (!Intl.PluralRules)
          throw new Et(`Intl.PluralRules is not available in this environment.
Try polyfilling it using "@formatjs/intl-pluralrules"
`, Oe.MISSING_INTL_API, o);
        var g = n.getPluralRules(t, { type: f.pluralType }).select(h - (f.offset || 0));
        m = f.options[g] || f.options.other;
      }
      if (!m)
        throw new zn(f.value, h, Object.keys(f.options), o);
      a.push.apply(a, dt(m.value, t, n, i, r, h - (f.offset || 0)));
      continue;
    }
  }
  return ta(a);
}
function ia(e, t) {
  return t ? k(k(k({}, e || {}), t || {}), Object.keys(e).reduce(function(n, i) {
    return n[i] = k(k({}, e[i]), t[i] || {}), n;
  }, {})) : e;
}
function ra(e, t) {
  return t ? Object.keys(e).reduce(function(n, i) {
    return n[i] = ia(e[i], t[i]), n;
  }, k({}, e)) : e;
}
function Xt(e) {
  return {
    create: function() {
      return {
        get: function(t) {
          return e[t];
        },
        set: function(t, n) {
          e[t] = n;
        }
      };
    }
  };
}
function la(e) {
  return e === void 0 && (e = {
    number: {},
    dateTime: {},
    pluralRules: {}
  }), {
    getNumberFormat: zt(function() {
      for (var t, n = [], i = 0; i < arguments.length; i++)
        n[i] = arguments[i];
      return new ((t = Intl.NumberFormat).bind.apply(t, jt([void 0], n, !1)))();
    }, {
      cache: Xt(e.number),
      strategy: qt.variadic
    }),
    getDateTimeFormat: zt(function() {
      for (var t, n = [], i = 0; i < arguments.length; i++)
        n[i] = arguments[i];
      return new ((t = Intl.DateTimeFormat).bind.apply(t, jt([void 0], n, !1)))();
    }, {
      cache: Xt(e.dateTime),
      strategy: qt.variadic
    }),
    getPluralRules: zt(function() {
      for (var t, n = [], i = 0; i < arguments.length; i++)
        n[i] = arguments[i];
      return new ((t = Intl.PluralRules).bind.apply(t, jt([void 0], n, !1)))();
    }, {
      cache: Xt(e.pluralRules),
      strategy: qt.variadic
    })
  };
}
var oa = (
  /** @class */
  function() {
    function e(t, n, i, r) {
      var l = this;
      if (n === void 0 && (n = e.defaultLocale), this.formatterCache = {
        number: {},
        dateTime: {},
        pluralRules: {}
      }, this.format = function(o) {
        var a = l.formatToParts(o);
        if (a.length === 1)
          return a[0].value;
        var s = a.reduce(function(u, f) {
          return !u.length || f.type !== j.literal || typeof u[u.length - 1] != "string" ? u.push(f.value) : u[u.length - 1] += f.value, u;
        }, []);
        return s.length <= 1 ? s[0] || "" : s;
      }, this.formatToParts = function(o) {
        return dt(l.ast, l.locales, l.formatters, l.formats, o, void 0, l.message);
      }, this.resolvedOptions = function() {
        return {
          locale: l.resolvedLocale.toString()
        };
      }, this.getAst = function() {
        return l.ast;
      }, this.locales = n, this.resolvedLocale = e.resolveLocale(n), typeof t == "string") {
        if (this.message = t, !e.__parse)
          throw new TypeError("IntlMessageFormat.__parse must be set to process `message` of type `string`");
        this.ast = e.__parse(t, {
          ignoreTag: r == null ? void 0 : r.ignoreTag,
          locale: this.resolvedLocale
        });
      } else
        this.ast = t;
      if (!Array.isArray(this.ast))
        throw new TypeError("A message must be provided as a String or AST.");
      this.formats = ra(e.formats, i), this.formatters = r && r.formatters || la(this.formatterCache);
    }
    return Object.defineProperty(e, "defaultLocale", {
      get: function() {
        return e.memoizedDefaultLocale || (e.memoizedDefaultLocale = new Intl.NumberFormat().resolvedOptions().locale), e.memoizedDefaultLocale;
      },
      enumerable: !1,
      configurable: !0
    }), e.memoizedDefaultLocale = null, e.resolveLocale = function(t) {
      var n = Intl.NumberFormat.supportedLocalesOf(t);
      return n.length > 0 ? new Intl.Locale(n[0]) : new Intl.Locale(typeof t == "string" ? t : t[0]);
    }, e.__parse = Xs, e.formats = {
      number: {
        integer: {
          maximumFractionDigits: 0
        },
        currency: {
          style: "currency"
        },
        percent: {
          style: "percent"
        }
      },
      date: {
        short: {
          month: "numeric",
          day: "numeric",
          year: "2-digit"
        },
        medium: {
          month: "short",
          day: "numeric",
          year: "numeric"
        },
        long: {
          month: "long",
          day: "numeric",
          year: "numeric"
        },
        full: {
          weekday: "long",
          month: "long",
          day: "numeric",
          year: "numeric"
        }
      },
      time: {
        short: {
          hour: "numeric",
          minute: "numeric"
        },
        medium: {
          hour: "numeric",
          minute: "numeric",
          second: "numeric"
        },
        long: {
          hour: "numeric",
          minute: "numeric",
          second: "numeric",
          timeZoneName: "short"
        },
        full: {
          hour: "numeric",
          minute: "numeric",
          second: "numeric",
          timeZoneName: "short"
        }
      }
    }, e;
  }()
);
function sa(e, t) {
  if (t == null)
    return;
  if (t in e)
    return e[t];
  const n = t.split(".");
  let i = e;
  for (let r = 0; r < n.length; r++)
    if (typeof i == "object") {
      if (r > 0) {
        const l = n.slice(r, n.length).join(".");
        if (l in i) {
          i = i[l];
          break;
        }
      }
      i = i[n[r]];
    } else
      i = void 0;
  return i;
}
const we = {}, aa = (e, t, n) => n && (t in we || (we[t] = {}), e in we[t] || (we[t][e] = n), n), or = (e, t) => {
  if (t == null)
    return;
  if (t in we && e in we[t])
    return we[t][e];
  const n = St(t);
  for (let i = 0; i < n.length; i++) {
    const r = n[i], l = fa(r, e);
    if (l)
      return aa(e, t, l);
  }
};
let gn;
const nt = tt({});
function ua(e) {
  return gn[e] || null;
}
function sr(e) {
  return e in gn;
}
function fa(e, t) {
  if (!sr(e))
    return null;
  const n = ua(e);
  return sa(n, t);
}
function ca(e) {
  if (e == null)
    return;
  const t = St(e);
  for (let n = 0; n < t.length; n++) {
    const i = t[n];
    if (sr(i))
      return i;
  }
}
function ha(e, ...t) {
  delete we[e], nt.update((n) => (n[e] = bs.all([n[e] || {}, ...t]), n));
}
Ue(
  [nt],
  ([e]) => Object.keys(e)
);
nt.subscribe((e) => gn = e);
const bt = {};
function _a(e, t) {
  bt[e].delete(t), bt[e].size === 0 && delete bt[e];
}
function ar(e) {
  return bt[e];
}
function ma(e) {
  return St(e).map((t) => {
    const n = ar(t);
    return [t, n ? [...n] : []];
  }).filter(([, t]) => t.length > 0);
}
function on(e) {
  return e == null ? !1 : St(e).some(
    (t) => {
      var n;
      return (n = ar(t)) == null ? void 0 : n.size;
    }
  );
}
function da(e, t) {
  return Promise.all(
    t.map((i) => (_a(e, i), i().then((r) => r.default || r)))
  ).then((i) => ha(e, ...i));
}
const Ze = {};
function ur(e) {
  if (!on(e))
    return e in Ze ? Ze[e] : Promise.resolve();
  const t = ma(e);
  return Ze[e] = Promise.all(
    t.map(
      ([n, i]) => da(n, i)
    )
  ).then(() => {
    if (on(e))
      return ur(e);
    delete Ze[e];
  }), Ze[e];
}
const ba = {
  number: {
    scientific: { notation: "scientific" },
    engineering: { notation: "engineering" },
    compactLong: { notation: "compact", compactDisplay: "long" },
    compactShort: { notation: "compact", compactDisplay: "short" }
  },
  date: {
    short: { month: "numeric", day: "numeric", year: "2-digit" },
    medium: { month: "short", day: "numeric", year: "numeric" },
    long: { month: "long", day: "numeric", year: "numeric" },
    full: { weekday: "long", month: "long", day: "numeric", year: "numeric" }
  },
  time: {
    short: { hour: "numeric", minute: "numeric" },
    medium: { hour: "numeric", minute: "numeric", second: "numeric" },
    long: {
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
      timeZoneName: "short"
    },
    full: {
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
      timeZoneName: "short"
    }
  }
}, ga = {
  fallbackLocale: null,
  loadingDelay: 200,
  formats: ba,
  warnOnMissingMessages: !0,
  handleMissingMessage: void 0,
  ignoreTag: !0
}, pa = ga;
function Me() {
  return pa;
}
const Zt = tt(!1);
var va = Object.defineProperty, wa = Object.defineProperties, ya = Object.getOwnPropertyDescriptors, qn = Object.getOwnPropertySymbols, Ea = Object.prototype.hasOwnProperty, Sa = Object.prototype.propertyIsEnumerable, Xn = (e, t, n) => t in e ? va(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, Ta = (e, t) => {
  for (var n in t || (t = {}))
    Ea.call(t, n) && Xn(e, n, t[n]);
  if (qn)
    for (var n of qn(t))
      Sa.call(t, n) && Xn(e, n, t[n]);
  return e;
}, Aa = (e, t) => wa(e, ya(t));
let sn;
const gt = tt(null);
function Zn(e) {
  return e.split("-").map((t, n, i) => i.slice(0, n + 1).join("-")).reverse();
}
function St(e, t = Me().fallbackLocale) {
  const n = Zn(e);
  return t ? [.../* @__PURE__ */ new Set([...n, ...Zn(t)])] : n;
}
function Be() {
  return sn ?? void 0;
}
gt.subscribe((e) => {
  sn = e ?? void 0, typeof window < "u" && e != null && document.documentElement.setAttribute("lang", e);
});
const Ha = (e) => {
  if (e && ca(e) && on(e)) {
    const { loadingDelay: t } = Me();
    let n;
    return typeof window < "u" && Be() != null && t ? n = window.setTimeout(
      () => Zt.set(!0),
      t
    ) : Zt.set(!0), ur(e).then(() => {
      gt.set(e);
    }).finally(() => {
      clearTimeout(n), Zt.set(!1);
    });
  }
  return gt.set(e);
}, it = Aa(Ta({}, gt), {
  set: Ha
}), Tt = (e) => {
  const t = /* @__PURE__ */ Object.create(null);
  return (i) => {
    const r = JSON.stringify(i);
    return r in t ? t[r] : t[r] = e(i);
  };
};
var Ba = Object.defineProperty, pt = Object.getOwnPropertySymbols, fr = Object.prototype.hasOwnProperty, cr = Object.prototype.propertyIsEnumerable, Wn = (e, t, n) => t in e ? Ba(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, pn = (e, t) => {
  for (var n in t || (t = {}))
    fr.call(t, n) && Wn(e, n, t[n]);
  if (pt)
    for (var n of pt(t))
      cr.call(t, n) && Wn(e, n, t[n]);
  return e;
}, Ge = (e, t) => {
  var n = {};
  for (var i in e)
    fr.call(e, i) && t.indexOf(i) < 0 && (n[i] = e[i]);
  if (e != null && pt)
    for (var i of pt(e))
      t.indexOf(i) < 0 && cr.call(e, i) && (n[i] = e[i]);
  return n;
};
const Ye = (e, t) => {
  const { formats: n } = Me();
  if (e in n && t in n[e])
    return n[e][t];
  throw new Error(`[svelte-i18n] Unknown "${t}" ${e} format.`);
}, Ca = Tt(
  (e) => {
    var t = e, { locale: n, format: i } = t, r = Ge(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format numbers');
    return i && (r = Ye("number", i)), new Intl.NumberFormat(n, r);
  }
), Pa = Tt(
  (e) => {
    var t = e, { locale: n, format: i } = t, r = Ge(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format dates');
    return i ? r = Ye("date", i) : Object.keys(r).length === 0 && (r = Ye("date", "short")), new Intl.DateTimeFormat(n, r);
  }
), Ia = Tt(
  (e) => {
    var t = e, { locale: n, format: i } = t, r = Ge(t, ["locale", "format"]);
    if (n == null)
      throw new Error(
        '[svelte-i18n] A "locale" must be set to format time values'
      );
    return i ? r = Ye("time", i) : Object.keys(r).length === 0 && (r = Ye("time", "short")), new Intl.DateTimeFormat(n, r);
  }
), ka = (e = {}) => {
  var t = e, {
    locale: n = Be()
  } = t, i = Ge(t, [
    "locale"
  ]);
  return Ca(pn({ locale: n }, i));
}, La = (e = {}) => {
  var t = e, {
    locale: n = Be()
  } = t, i = Ge(t, [
    "locale"
  ]);
  return Pa(pn({ locale: n }, i));
}, Na = (e = {}) => {
  var t = e, {
    locale: n = Be()
  } = t, i = Ge(t, [
    "locale"
  ]);
  return Ia(pn({ locale: n }, i));
}, Oa = Tt(
  // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
  (e, t = Be()) => new oa(e, t, Me().formats, {
    ignoreTag: Me().ignoreTag
  })
), Ma = (e, t = {}) => {
  var n, i, r, l;
  let o = t;
  typeof e == "object" && (o = e, e = o.id);
  const {
    values: a,
    locale: s = Be(),
    default: u
  } = o;
  if (s == null)
    throw new Error(
      "[svelte-i18n] Cannot format a message without first setting the initial locale."
    );
  let f = or(e, s);
  if (!f)
    f = (l = (r = (i = (n = Me()).handleMissingMessage) == null ? void 0 : i.call(n, { locale: s, id: e, defaultValue: u })) != null ? r : u) != null ? l : e;
  else if (typeof f != "string")
    return console.warn(
      `[svelte-i18n] Message with id "${e}" must be of type "string", found: "${typeof f}". Gettin its value through the "$format" method is deprecated; use the "json" method instead.`
    ), f;
  if (!a)
    return f;
  let c = f;
  try {
    c = Oa(f, s).format(a);
  } catch (h) {
    h instanceof Error && console.warn(
      `[svelte-i18n] Message "${e}" has syntax error:`,
      h.message
    );
  }
  return c;
}, Ra = (e, t) => Na(t).format(e), Da = (e, t) => La(t).format(e), Ua = (e, t) => ka(t).format(e), Ga = (e, t = Be()) => or(e, t);
Ue([it, nt], () => Ma);
Ue([it], () => Ra);
Ue([it], () => Da);
Ue([it], () => Ua);
Ue([it, nt], () => Ga);
const {
  SvelteComponent: Fa,
  append: Qn,
  attr: xa,
  check_outros: Jn,
  create_component: vn,
  destroy_component: wn,
  detach: ja,
  element: Va,
  group_outros: Yn,
  init: za,
  insert: qa,
  mount_component: yn,
  safe_not_equal: Xa,
  set_style: Kn,
  space: $n,
  toggle_class: ei,
  transition_in: _e,
  transition_out: Te
} = window.__gradio__svelte__internal, { createEventDispatcher: Za } = window.__gradio__svelte__internal;
function ti(e) {
  let t, n;
  return t = new et({
    props: {
      Icon: bo,
      label: (
        /*i18n*/
        e[3]("common.edit")
      )
    }
  }), t.$on(
    "click",
    /*click_handler*/
    e[5]
  ), {
    c() {
      vn(t.$$.fragment);
    },
    m(i, r) {
      yn(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r & /*i18n*/
      8 && (l.label = /*i18n*/
      i[3]("common.edit")), t.$set(l);
    },
    i(i) {
      n || (_e(t.$$.fragment, i), n = !0);
    },
    o(i) {
      Te(t.$$.fragment, i), n = !1;
    },
    d(i) {
      wn(t, i);
    }
  };
}
function ni(e) {
  let t, n;
  return t = new et({
    props: {
      Icon: Po,
      label: (
        /*i18n*/
        e[3]("common.undo")
      )
    }
  }), t.$on(
    "click",
    /*click_handler_1*/
    e[6]
  ), {
    c() {
      vn(t.$$.fragment);
    },
    m(i, r) {
      yn(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r & /*i18n*/
      8 && (l.label = /*i18n*/
      i[3]("common.undo")), t.$set(l);
    },
    i(i) {
      n || (_e(t.$$.fragment, i), n = !0);
    },
    o(i) {
      Te(t.$$.fragment, i), n = !1;
    },
    d(i) {
      wn(t, i);
    }
  };
}
function Wa(e) {
  let t, n, i, r, l, o = (
    /*editable*/
    e[0] && ti(e)
  ), a = (
    /*undoable*/
    e[1] && ni(e)
  );
  return r = new et({
    props: {
      Icon: ql,
      label: (
        /*i18n*/
        e[3]("common.clear")
      )
    }
  }), r.$on(
    "click",
    /*click_handler_2*/
    e[7]
  ), {
    c() {
      t = Va("div"), o && o.c(), n = $n(), a && a.c(), i = $n(), vn(r.$$.fragment), xa(t, "class", "svelte-1wj0ocy"), ei(t, "not-absolute", !/*absolute*/
      e[2]), Kn(
        t,
        "position",
        /*absolute*/
        e[2] ? "absolute" : "static"
      );
    },
    m(s, u) {
      qa(s, t, u), o && o.m(t, null), Qn(t, n), a && a.m(t, null), Qn(t, i), yn(r, t, null), l = !0;
    },
    p(s, [u]) {
      /*editable*/
      s[0] ? o ? (o.p(s, u), u & /*editable*/
      1 && _e(o, 1)) : (o = ti(s), o.c(), _e(o, 1), o.m(t, n)) : o && (Yn(), Te(o, 1, 1, () => {
        o = null;
      }), Jn()), /*undoable*/
      s[1] ? a ? (a.p(s, u), u & /*undoable*/
      2 && _e(a, 1)) : (a = ni(s), a.c(), _e(a, 1), a.m(t, i)) : a && (Yn(), Te(a, 1, 1, () => {
        a = null;
      }), Jn());
      const f = {};
      u & /*i18n*/
      8 && (f.label = /*i18n*/
      s[3]("common.clear")), r.$set(f), (!l || u & /*absolute*/
      4) && ei(t, "not-absolute", !/*absolute*/
      s[2]), u & /*absolute*/
      4 && Kn(
        t,
        "position",
        /*absolute*/
        s[2] ? "absolute" : "static"
      );
    },
    i(s) {
      l || (_e(o), _e(a), _e(r.$$.fragment, s), l = !0);
    },
    o(s) {
      Te(o), Te(a), Te(r.$$.fragment, s), l = !1;
    },
    d(s) {
      s && ja(t), o && o.d(), a && a.d(), wn(r);
    }
  };
}
function Qa(e, t, n) {
  let { editable: i = !1 } = t, { undoable: r = !1 } = t, { absolute: l = !0 } = t, { i18n: o } = t;
  const a = Za(), s = () => a("edit"), u = () => a("undo"), f = (c) => {
    a("clear"), c.stopPropagation();
  };
  return e.$$set = (c) => {
    "editable" in c && n(0, i = c.editable), "undoable" in c && n(1, r = c.undoable), "absolute" in c && n(2, l = c.absolute), "i18n" in c && n(3, o = c.i18n);
  }, [
    i,
    r,
    l,
    o,
    a,
    s,
    u,
    f
  ];
}
class Ja extends Fa {
  constructor(t) {
    super(), za(this, t, Qa, Wa, Xa, {
      editable: 0,
      undoable: 1,
      absolute: 2,
      i18n: 3
    });
  }
}
var ii = Object.prototype.hasOwnProperty;
function ri(e, t, n) {
  for (n of e.keys())
    if (Qe(n, t))
      return n;
}
function Qe(e, t) {
  var n, i, r;
  if (e === t)
    return !0;
  if (e && t && (n = e.constructor) === t.constructor) {
    if (n === Date)
      return e.getTime() === t.getTime();
    if (n === RegExp)
      return e.toString() === t.toString();
    if (n === Array) {
      if ((i = e.length) === t.length)
        for (; i-- && Qe(e[i], t[i]); )
          ;
      return i === -1;
    }
    if (n === Set) {
      if (e.size !== t.size)
        return !1;
      for (i of e)
        if (r = i, r && typeof r == "object" && (r = ri(t, r), !r) || !t.has(r))
          return !1;
      return !0;
    }
    if (n === Map) {
      if (e.size !== t.size)
        return !1;
      for (i of e)
        if (r = i[0], r && typeof r == "object" && (r = ri(t, r), !r) || !Qe(i[1], t.get(r)))
          return !1;
      return !0;
    }
    if (n === ArrayBuffer)
      e = new Uint8Array(e), t = new Uint8Array(t);
    else if (n === DataView) {
      if ((i = e.byteLength) === t.byteLength)
        for (; i-- && e.getInt8(i) === t.getInt8(i); )
          ;
      return i === -1;
    }
    if (ArrayBuffer.isView(e)) {
      if ((i = e.byteLength) === t.byteLength)
        for (; i-- && e[i] === t[i]; )
          ;
      return i === -1;
    }
    if (!n || typeof e == "object") {
      i = 0;
      for (n in e)
        if (ii.call(e, n) && ++i && !ii.call(t, n) || !(n in t) || !Qe(e[n], t[n]))
          return !1;
      return Object.keys(t).length === i;
    }
  }
  return e !== e && t !== t;
}
async function Ya(e) {
  return e ? `<div style="display: flex; flex-wrap: wrap; gap: 16px">${(await Promise.all(
    e.map(async ([n, i]) => n === null || !n.url ? "" : await Lo(n.url, "url"))
  )).map((n) => `<img src="${n}" style="height: 400px" />`).join("")}</div>` : "";
}
const {
  SvelteComponent: Ka,
  add_iframe_resize_listener: $a,
  add_render_callback: hr,
  append: F,
  attr: w,
  binding_callbacks: li,
  bubble: ve,
  check_outros: Ke,
  create_component: Fe,
  destroy_component: xe,
  destroy_each: _r,
  detach: V,
  element: U,
  empty: eu,
  ensure_array_like: vt,
  globals: tu,
  group_outros: $e,
  init: nu,
  insert: z,
  listen: le,
  mount_component: je,
  run_all: mr,
  safe_not_equal: iu,
  set_data: dr,
  set_style: se,
  space: ae,
  src_url_equal: he,
  text: br,
  toggle_class: ue,
  transition_in: D,
  transition_out: x
} = window.__gradio__svelte__internal, { window: gr } = tu, { createEventDispatcher: ru } = window.__gradio__svelte__internal, { tick: lu } = window.__gradio__svelte__internal;
function oi(e, t, n) {
  const i = e.slice();
  return i[45] = t[n], i[47] = n, i;
}
function si(e, t, n) {
  const i = e.slice();
  return i[48] = t[n], i[49] = t, i[47] = n, i;
}
function ai(e) {
  let t, n;
  return t = new ol({
    props: {
      show_label: (
        /*show_label*/
        e[1]
      ),
      Icon: Ui,
      label: (
        /*label*/
        e[2] || "Gallery"
      )
    }
  }), {
    c() {
      Fe(t.$$.fragment);
    },
    m(i, r) {
      je(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r[0] & /*show_label*/
      2 && (l.show_label = /*show_label*/
      i[1]), r[0] & /*label*/
      4 && (l.label = /*label*/
      i[2] || "Gallery"), t.$set(l);
    },
    i(i) {
      n || (D(t.$$.fragment, i), n = !0);
    },
    o(i) {
      x(t.$$.fragment, i), n = !1;
    },
    d(i) {
      xe(t, i);
    }
  };
}
function ou(e) {
  let t, n, i, r, l, o, a = (
    /*selected_index*/
    e[0] !== null && /*allow_preview*/
    e[7] && ui(e)
  ), s = (
    /*show_share_button*/
    e[9] && _i(e)
  ), u = vt(
    /*_value*/
    e[12]
  ), f = [];
  for (let c = 0; c < u.length; c += 1)
    f[c] = di(oi(e, u, c));
  return {
    c() {
      a && a.c(), t = ae(), n = U("div"), i = U("div"), s && s.c(), r = ae();
      for (let c = 0; c < f.length; c += 1)
        f[c].c();
      w(i, "class", "grid-container svelte-1wl86it"), se(
        i,
        "--grid-cols",
        /*columns*/
        e[4]
      ), se(
        i,
        "--grid-rows",
        /*rows*/
        e[5]
      ), se(
        i,
        "--object-fit",
        /*object_fit*/
        e[8]
      ), se(
        i,
        "height",
        /*height*/
        e[6]
      ), ue(
        i,
        "pt-6",
        /*show_label*/
        e[1]
      ), w(n, "class", "grid-wrap svelte-1wl86it"), hr(() => (
        /*div1_elementresize_handler*/
        e[40].call(n)
      )), ue(n, "fixed-height", !/*height*/
      e[6] || /*height*/
      e[6] == "auto");
    },
    m(c, h) {
      a && a.m(c, h), z(c, t, h), z(c, n, h), F(n, i), s && s.m(i, null), F(i, r);
      for (let _ = 0; _ < f.length; _ += 1)
        f[_] && f[_].m(i, null);
      l = $a(
        n,
        /*div1_elementresize_handler*/
        e[40].bind(n)
      ), o = !0;
    },
    p(c, h) {
      if (/*selected_index*/
      c[0] !== null && /*allow_preview*/
      c[7] ? a ? (a.p(c, h), h[0] & /*selected_index, allow_preview*/
      129 && D(a, 1)) : (a = ui(c), a.c(), D(a, 1), a.m(t.parentNode, t)) : a && ($e(), x(a, 1, 1, () => {
        a = null;
      }), Ke()), /*show_share_button*/
      c[9] ? s ? (s.p(c, h), h[0] & /*show_share_button*/
      512 && D(s, 1)) : (s = _i(c), s.c(), D(s, 1), s.m(i, r)) : s && ($e(), x(s, 1, 1, () => {
        s = null;
      }), Ke()), h[0] & /*_value, selected_index*/
      4097) {
        u = vt(
          /*_value*/
          c[12]
        );
        let _;
        for (_ = 0; _ < u.length; _ += 1) {
          const b = oi(c, u, _);
          f[_] ? f[_].p(b, h) : (f[_] = di(b), f[_].c(), f[_].m(i, null));
        }
        for (; _ < f.length; _ += 1)
          f[_].d(1);
        f.length = u.length;
      }
      (!o || h[0] & /*columns*/
      16) && se(
        i,
        "--grid-cols",
        /*columns*/
        c[4]
      ), (!o || h[0] & /*rows*/
      32) && se(
        i,
        "--grid-rows",
        /*rows*/
        c[5]
      ), (!o || h[0] & /*object_fit*/
      256) && se(
        i,
        "--object-fit",
        /*object_fit*/
        c[8]
      ), (!o || h[0] & /*height*/
      64) && se(
        i,
        "height",
        /*height*/
        c[6]
      ), (!o || h[0] & /*show_label*/
      2) && ue(
        i,
        "pt-6",
        /*show_label*/
        c[1]
      ), (!o || h[0] & /*height*/
      64) && ue(n, "fixed-height", !/*height*/
      c[6] || /*height*/
      c[6] == "auto");
    },
    i(c) {
      o || (D(a), D(s), o = !0);
    },
    o(c) {
      x(a), x(s), o = !1;
    },
    d(c) {
      c && (V(t), V(n)), a && a.d(c), s && s.d(), _r(f, c), l();
    }
  };
}
function su(e) {
  let t, n;
  return t = new Ul({
    props: {
      unpadded_box: !0,
      size: "large",
      $$slots: { default: [hu] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      Fe(t.$$.fragment);
    },
    m(i, r) {
      je(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r[1] & /*$$scope*/
      524288 && (l.$$scope = { dirty: r, ctx: i }), t.$set(l);
    },
    i(i) {
      n || (D(t.$$.fragment, i), n = !0);
    },
    o(i) {
      x(t.$$.fragment, i), n = !1;
    },
    d(i) {
      xe(t, i);
    }
  };
}
function ui(e) {
  var m;
  let t, n, i, r, l, o, a, s, u, f, c, h = (
    /*show_download_button*/
    e[10] && fi(e)
  );
  r = new Ja({
    props: { i18n: (
      /*i18n*/
      e[11]
    ), absolute: !1 }
  }), r.$on(
    "clear",
    /*clear_handler*/
    e[32]
  );
  function _(g, p) {
    return (
      /*_value*/
      g[12][
        /*selected_index*/
        g[0]
      ].image.mime_type === "video/mp4" ? uu : au
    );
  }
  let b = _(e), T = b(e), y = (
    /*_value*/
    ((m = e[12][
      /*selected_index*/
      e[0]
    ]) == null ? void 0 : m.caption) && ci(e)
  ), C = vt(
    /*_value*/
    e[12]
  ), E = [];
  for (let g = 0; g < C.length; g += 1)
    E[g] = hi(si(e, C, g));
  return {
    c() {
      t = U("button"), n = U("div"), h && h.c(), i = ae(), Fe(r.$$.fragment), l = ae(), T.c(), o = ae(), y && y.c(), a = ae(), s = U("div");
      for (let g = 0; g < E.length; g += 1)
        E[g].c();
      w(n, "class", "icon-buttons svelte-1wl86it"), w(s, "class", "thumbnails scroll-hide svelte-1wl86it"), w(s, "data-testid", "container_el"), w(t, "class", "preview svelte-1wl86it");
    },
    m(g, p) {
      z(g, t, p), F(t, n), h && h.m(n, null), F(n, i), je(r, n, null), F(t, l), T.m(t, null), F(t, o), y && y.m(t, null), F(t, a), F(t, s);
      for (let N = 0; N < E.length; N += 1)
        E[N] && E[N].m(s, null);
      e[36](s), u = !0, f || (c = le(
        t,
        "keydown",
        /*on_keydown*/
        e[18]
      ), f = !0);
    },
    p(g, p) {
      var G;
      /*show_download_button*/
      g[10] ? h ? (h.p(g, p), p[0] & /*show_download_button*/
      1024 && D(h, 1)) : (h = fi(g), h.c(), D(h, 1), h.m(n, i)) : h && ($e(), x(h, 1, 1, () => {
        h = null;
      }), Ke());
      const N = {};
      if (p[0] & /*i18n*/
      2048 && (N.i18n = /*i18n*/
      g[11]), r.$set(N), b === (b = _(g)) && T ? T.p(g, p) : (T.d(1), T = b(g), T && (T.c(), T.m(t, o))), /*_value*/
      (G = g[12][
        /*selected_index*/
        g[0]
      ]) != null && G.caption ? y ? y.p(g, p) : (y = ci(g), y.c(), y.m(t, a)) : y && (y.d(1), y = null), p[0] & /*_value, el, selected_index*/
      12289) {
        C = vt(
          /*_value*/
          g[12]
        );
        let L;
        for (L = 0; L < C.length; L += 1) {
          const Z = si(g, C, L);
          E[L] ? E[L].p(Z, p) : (E[L] = hi(Z), E[L].c(), E[L].m(s, null));
        }
        for (; L < E.length; L += 1)
          E[L].d(1);
        E.length = C.length;
      }
    },
    i(g) {
      u || (D(h), D(r.$$.fragment, g), u = !0);
    },
    o(g) {
      x(h), x(r.$$.fragment, g), u = !1;
    },
    d(g) {
      g && V(t), h && h.d(), xe(r), T.d(), y && y.d(), _r(E, g), e[36](null), f = !1, c();
    }
  };
}
function fi(e) {
  let t, n, i, r;
  return n = new et({
    props: {
      Icon: so,
      label: (
        /*i18n*/
        e[11]("common.download")
      )
    }
  }), {
    c() {
      t = U("a"), Fe(n.$$.fragment), w(t, "href", i = an(
        /*value*/
        e[3][
          /*selected_index*/
          e[0]
        ]
      )), w(t, "target", window.__is_colab__ ? "_blank" : null), w(t, "download", "image"), w(t, "class", "svelte-1wl86it");
    },
    m(l, o) {
      z(l, t, o), je(n, t, null), r = !0;
    },
    p(l, o) {
      const a = {};
      o[0] & /*i18n*/
      2048 && (a.label = /*i18n*/
      l[11]("common.download")), n.$set(a), (!r || o[0] & /*value, selected_index*/
      9 && i !== (i = an(
        /*value*/
        l[3][
          /*selected_index*/
          l[0]
        ]
      ))) && w(t, "href", i);
    },
    i(l) {
      r || (D(n.$$.fragment, l), r = !0);
    },
    o(l) {
      x(n.$$.fragment, l), r = !1;
    },
    d(l) {
      l && V(t), xe(n);
    }
  };
}
function au(e) {
  let t, n, i, r, l, o, a;
  return {
    c() {
      t = U("button"), n = U("img"), w(n, "data-testid", "detailed-image"), he(n.src, i = /*_value*/
      e[12][
        /*selected_index*/
        e[0]
      ].image.url) || w(n, "src", i), w(n, "alt", r = /*_value*/
      e[12][
        /*selected_index*/
        e[0]
      ].caption || ""), w(n, "title", l = /*_value*/
      e[12][
        /*selected_index*/
        e[0]
      ].caption || null), w(n, "loading", "lazy"), w(n, "class", "svelte-1wl86it"), ue(n, "with-caption", !!/*_value*/
      e[12][
        /*selected_index*/
        e[0]
      ].caption), w(t, "class", "image-button svelte-1wl86it"), se(t, "height", "calc(100% - " + /*_value*/
      (e[12][
        /*selected_index*/
        e[0]
      ].caption ? "80px" : "60px") + ")"), w(t, "aria-label", "detailed view of selected image");
    },
    m(s, u) {
      z(s, t, u), F(t, n), o || (a = le(
        t,
        "click",
        /*click_handler*/
        e[33]
      ), o = !0);
    },
    p(s, u) {
      u[0] & /*_value, selected_index*/
      4097 && !he(n.src, i = /*_value*/
      s[12][
        /*selected_index*/
        s[0]
      ].image.url) && w(n, "src", i), u[0] & /*_value, selected_index*/
      4097 && r !== (r = /*_value*/
      s[12][
        /*selected_index*/
        s[0]
      ].caption || "") && w(n, "alt", r), u[0] & /*_value, selected_index*/
      4097 && l !== (l = /*_value*/
      s[12][
        /*selected_index*/
        s[0]
      ].caption || null) && w(n, "title", l), u[0] & /*_value, selected_index*/
      4097 && ue(n, "with-caption", !!/*_value*/
      s[12][
        /*selected_index*/
        s[0]
      ].caption), u[0] & /*_value, selected_index*/
      4097 && se(t, "height", "calc(100% - " + /*_value*/
      (s[12][
        /*selected_index*/
        s[0]
      ].caption ? "80px" : "60px") + ")");
    },
    d(s) {
      s && V(t), o = !1, a();
    }
  };
}
function uu(e) {
  let t, n, i, r, l, o;
  return {
    c() {
      t = U("video"), n = U("track"), w(n, "kind", "captions"), w(t, "class", "detailed-video svelte-1wl86it"), w(t, "data-testid", "detailed-video"), t.controls = !0, he(t.src, i = /*_value*/
      e[12][
        /*selected_index*/
        e[0]
      ].image.path) || w(t, "src", i), w(t, "title", r = /*_value*/
      e[12][
        /*selected_index*/
        e[0]
      ].image.alt_text), w(t, "preload", "auto");
    },
    m(a, s) {
      z(a, t, s), F(t, n), l || (o = [
        le(
          t,
          "play",
          /*play_handler*/
          e[28]
        ),
        le(
          t,
          "pause",
          /*pause_handler*/
          e[29]
        ),
        le(
          t,
          "ended",
          /*ended_handler*/
          e[30]
        )
      ], l = !0);
    },
    p(a, s) {
      s[0] & /*_value, selected_index*/
      4097 && !he(t.src, i = /*_value*/
      a[12][
        /*selected_index*/
        a[0]
      ].image.path) && w(t, "src", i), s[0] & /*_value, selected_index*/
      4097 && r !== (r = /*_value*/
      a[12][
        /*selected_index*/
        a[0]
      ].image.alt_text) && w(t, "title", r);
    },
    d(a) {
      a && V(t), l = !1, mr(o);
    }
  };
}
function ci(e) {
  let t, n = (
    /*_value*/
    e[12][
      /*selected_index*/
      e[0]
    ].caption + ""
  ), i;
  return {
    c() {
      t = U("caption"), i = br(n), w(t, "class", "caption svelte-1wl86it");
    },
    m(r, l) {
      z(r, t, l), F(t, i);
    },
    p(r, l) {
      l[0] & /*_value, selected_index*/
      4097 && n !== (n = /*_value*/
      r[12][
        /*selected_index*/
        r[0]
      ].caption + "") && dr(i, n);
    },
    d(r) {
      r && V(t);
    }
  };
}
function hi(e) {
  let t, n, i, r, l, o, a = (
    /*i*/
    e[47]
  ), s, u;
  const f = () => (
    /*button_binding*/
    e[34](t, a)
  ), c = () => (
    /*button_binding*/
    e[34](null, a)
  );
  function h() {
    return (
      /*click_handler_1*/
      e[35](
        /*i*/
        e[47]
      )
    );
  }
  return {
    c() {
      t = U("button"), n = U("img"), l = ae(), he(n.src, i = /*media*/
      e[48].image.url) || w(n, "src", i), w(n, "title", r = /*media*/
      e[48].caption || null), w(n, "data-testid", "thumbnail " + /*i*/
      (e[47] + 1)), w(n, "alt", ""), w(n, "loading", "lazy"), w(n, "class", "svelte-1wl86it"), w(t, "class", "thumbnail-item thumbnail-small svelte-1wl86it"), w(t, "aria-label", o = "Thumbnail " + /*i*/
      (e[47] + 1) + " of " + /*_value*/
      e[12].length), ue(
        t,
        "selected",
        /*selected_index*/
        e[0] === /*i*/
        e[47]
      );
    },
    m(_, b) {
      z(_, t, b), F(t, n), F(t, l), f(), s || (u = le(t, "click", h), s = !0);
    },
    p(_, b) {
      e = _, b[0] & /*_value*/
      4096 && !he(n.src, i = /*media*/
      e[48].image.url) && w(n, "src", i), b[0] & /*_value*/
      4096 && r !== (r = /*media*/
      e[48].caption || null) && w(n, "title", r), b[0] & /*_value*/
      4096 && o !== (o = "Thumbnail " + /*i*/
      (e[47] + 1) + " of " + /*_value*/
      e[12].length) && w(t, "aria-label", o), a !== /*i*/
      e[47] && (c(), a = /*i*/
      e[47], f()), b[0] & /*selected_index*/
      1 && ue(
        t,
        "selected",
        /*selected_index*/
        e[0] === /*i*/
        e[47]
      );
    },
    d(_) {
      _ && V(t), c(), s = !1, u();
    }
  };
}
function _i(e) {
  let t, n, i;
  return n = new qo({
    props: {
      i18n: (
        /*i18n*/
        e[11]
      ),
      value: (
        /*_value*/
        e[12]
      ),
      formatter: Ya
    }
  }), n.$on(
    "share",
    /*share_handler*/
    e[37]
  ), n.$on(
    "error",
    /*error_handler*/
    e[38]
  ), {
    c() {
      t = U("div"), Fe(n.$$.fragment), w(t, "class", "icon-button svelte-1wl86it");
    },
    m(r, l) {
      z(r, t, l), je(n, t, null), i = !0;
    },
    p(r, l) {
      const o = {};
      l[0] & /*i18n*/
      2048 && (o.i18n = /*i18n*/
      r[11]), l[0] & /*_value*/
      4096 && (o.value = /*_value*/
      r[12]), n.$set(o);
    },
    i(r) {
      i || (D(n.$$.fragment, r), i = !0);
    },
    o(r) {
      x(n.$$.fragment, r), i = !1;
    },
    d(r) {
      r && V(t), xe(n);
    }
  };
}
function fu(e) {
  let t, n, i;
  return {
    c() {
      t = U("img"), w(t, "alt", n = /*entry*/
      e[45].caption || ""), he(t.src, i = typeof /*entry*/
      e[45].image == "string" ? (
        /*entry*/
        e[45].image
      ) : (
        /*entry*/
        e[45].image.url
      )) || w(t, "src", i), w(t, "loading", "lazy"), w(t, "class", "svelte-1wl86it");
    },
    m(r, l) {
      z(r, t, l);
    },
    p(r, l) {
      l[0] & /*_value*/
      4096 && n !== (n = /*entry*/
      r[45].caption || "") && w(t, "alt", n), l[0] & /*_value*/
      4096 && !he(t.src, i = typeof /*entry*/
      r[45].image == "string" ? (
        /*entry*/
        r[45].image
      ) : (
        /*entry*/
        r[45].image.url
      )) && w(t, "src", i);
    },
    d(r) {
      r && V(t);
    }
  };
}
function cu(e) {
  let t, n, i, r, l, o;
  return {
    c() {
      t = U("video"), n = U("track"), w(n, "kind", "captions"), w(t, "class", "detailed-video svelte-1wl86it"), w(t, "data-testid", "detailed-video"), t.controls = !0, he(t.src, i = /*entry*/
      e[45].image.path) || w(t, "src", i), w(t, "title", r = /*entry*/
      e[45].image.alt_text), w(t, "preload", "auto");
    },
    m(a, s) {
      z(a, t, s), F(t, n), l || (o = [
        le(
          t,
          "play",
          /*play_handler_1*/
          e[25]
        ),
        le(
          t,
          "pause",
          /*pause_handler_1*/
          e[26]
        ),
        le(
          t,
          "ended",
          /*ended_handler_1*/
          e[27]
        )
      ], l = !0);
    },
    p(a, s) {
      s[0] & /*_value*/
      4096 && !he(t.src, i = /*entry*/
      a[45].image.path) && w(t, "src", i), s[0] & /*_value*/
      4096 && r !== (r = /*entry*/
      a[45].image.alt_text) && w(t, "title", r);
    },
    d(a) {
      a && V(t), l = !1, mr(o);
    }
  };
}
function mi(e) {
  let t, n = (
    /*entry*/
    e[45].caption + ""
  ), i;
  return {
    c() {
      t = U("div"), i = br(n), w(t, "class", "caption-label svelte-1wl86it");
    },
    m(r, l) {
      z(r, t, l), F(t, i);
    },
    p(r, l) {
      l[0] & /*_value*/
      4096 && n !== (n = /*entry*/
      r[45].caption + "") && dr(i, n);
    },
    d(r) {
      r && V(t);
    }
  };
}
function di(e) {
  let t, n, i, r, l, o;
  function a(h, _) {
    return (
      /*entry*/
      h[45].image.mime_type === "video/mp4" ? cu : fu
    );
  }
  let s = a(e), u = s(e), f = (
    /*entry*/
    e[45].caption && mi(e)
  );
  function c() {
    return (
      /*click_handler_2*/
      e[39](
        /*i*/
        e[47]
      )
    );
  }
  return {
    c() {
      t = U("button"), u.c(), n = ae(), f && f.c(), i = ae(), w(t, "class", "thumbnail-item thumbnail-lg svelte-1wl86it"), w(t, "aria-label", r = "Thumbnail " + /*i*/
      (e[47] + 1) + " of " + /*_value*/
      e[12].length), ue(
        t,
        "selected",
        /*selected_index*/
        e[0] === /*i*/
        e[47]
      );
    },
    m(h, _) {
      z(h, t, _), u.m(t, null), F(t, n), f && f.m(t, null), F(t, i), l || (o = le(t, "click", c), l = !0);
    },
    p(h, _) {
      e = h, s === (s = a(e)) && u ? u.p(e, _) : (u.d(1), u = s(e), u && (u.c(), u.m(t, n))), /*entry*/
      e[45].caption ? f ? f.p(e, _) : (f = mi(e), f.c(), f.m(t, i)) : f && (f.d(1), f = null), _[0] & /*_value*/
      4096 && r !== (r = "Thumbnail " + /*i*/
      (e[47] + 1) + " of " + /*_value*/
      e[12].length) && w(t, "aria-label", r), _[0] & /*selected_index*/
      1 && ue(
        t,
        "selected",
        /*selected_index*/
        e[0] === /*i*/
        e[47]
      );
    },
    d(h) {
      h && V(t), u.d(), f && f.d(), l = !1, o();
    }
  };
}
function hu(e) {
  let t, n;
  return t = new Ui({}), {
    c() {
      Fe(t.$$.fragment);
    },
    m(i, r) {
      je(t, i, r), n = !0;
    },
    i(i) {
      n || (D(t.$$.fragment, i), n = !0);
    },
    o(i) {
      x(t.$$.fragment, i), n = !1;
    },
    d(i) {
      xe(t, i);
    }
  };
}
function _u(e) {
  let t, n, i, r, l, o, a;
  hr(
    /*onwindowresize*/
    e[31]
  );
  let s = (
    /*show_label*/
    e[1] && ai(e)
  );
  const u = [su, ou], f = [];
  function c(h, _) {
    return (
      /*value*/
      h[3] === null || /*_value*/
      h[12] === null || /*_value*/
      h[12].length === 0 ? 0 : 1
    );
  }
  return n = c(e), i = f[n] = u[n](e), {
    c() {
      s && s.c(), t = ae(), i.c(), r = eu();
    },
    m(h, _) {
      s && s.m(h, _), z(h, t, _), f[n].m(h, _), z(h, r, _), l = !0, o || (a = le(
        gr,
        "resize",
        /*onwindowresize*/
        e[31]
      ), o = !0);
    },
    p(h, _) {
      /*show_label*/
      h[1] ? s ? (s.p(h, _), _[0] & /*show_label*/
      2 && D(s, 1)) : (s = ai(h), s.c(), D(s, 1), s.m(t.parentNode, t)) : s && ($e(), x(s, 1, 1, () => {
        s = null;
      }), Ke());
      let b = n;
      n = c(h), n === b ? f[n].p(h, _) : ($e(), x(f[b], 1, 1, () => {
        f[b] = null;
      }), Ke(), i = f[n], i ? i.p(h, _) : (i = f[n] = u[n](h), i.c()), D(i, 1), i.m(r.parentNode, r));
    },
    i(h) {
      l || (D(s), D(i), l = !0);
    },
    o(h) {
      x(s), x(i), l = !1;
    },
    d(h) {
      h && (V(t), V(r)), s && s.d(h), f[n].d(h), o = !1, a();
    }
  };
}
function We(e, t) {
  return e ?? t();
}
function Ee(e) {
  let t, n = e[0], i = 1;
  for (; i < e.length; ) {
    const r = e[i], l = e[i + 1];
    if (i += 2, (r === "optionalAccess" || r === "optionalCall") && n == null)
      return;
    r === "access" || r === "optionalAccess" ? (t = n, n = l(n)) : (r === "call" || r === "optionalCall") && (n = l((...o) => n.call(t, ...o)), t = void 0);
  }
  return n;
}
function mu(e) {
  return typeof e == "object" && e !== null && "data" in e;
}
function an(e) {
  return mu(e) ? e.path : typeof e == "string" ? e : Array.isArray(e) ? an(e[0]) : "";
}
function du(e, t, n) {
  let i, r, { show_label: l = !0 } = t, { label: o } = t, { root: a = "" } = t, { proxy_url: s = null } = t, { value: u = null } = t, { columns: f = [2] } = t, { rows: c = void 0 } = t, { height: h = "auto" } = t, { preview: _ } = t, { allow_preview: b = !0 } = t, { object_fit: T = "cover" } = t, { show_share_button: y = !1 } = t, { show_download_button: C = !1 } = t, { i18n: E } = t, { selected_index: m = null } = t;
  const g = ru();
  let p = !0, N = null, G = u;
  m === null && _ && Ee([u, "optionalAccess", (d) => d.length]) && (m = 0);
  let L = m;
  function Z(d) {
    const ze = d.target, Ct = d.clientX, Pt = ze.offsetWidth / 2;
    Ct < Pt ? n(0, m = i) : n(0, m = r);
  }
  function K(d) {
    switch (d.code) {
      case "Escape":
        d.preventDefault(), n(0, m = null);
        break;
      case "ArrowLeft":
        d.preventDefault(), n(0, m = i);
        break;
      case "ArrowRight":
        d.preventDefault(), n(0, m = r);
        break;
    }
  }
  let W = [], q;
  async function $(d) {
    if (typeof d != "number" || (await lu(), W[d] === void 0))
      return;
    Ee([
      W,
      "access",
      (qe) => qe[d],
      "optionalAccess",
      (qe) => qe.focus,
      "call",
      (qe) => qe()
    ]);
    const { left: ze, width: Ct } = q.getBoundingClientRect(), { left: En, width: Pt } = W[d].getBoundingClientRect(), Sn = En - ze + Pt / 2 - Ct / 2 + q.scrollLeft;
    q && typeof q.scrollTo == "function" && q.scrollTo({
      left: Sn < 0 ? 0 : Sn,
      behavior: "smooth"
    });
  }
  let ee = 0, v = 0;
  function rt(d) {
    ve.call(this, e, d);
  }
  function At(d) {
    ve.call(this, e, d);
  }
  function lt(d) {
    ve.call(this, e, d);
  }
  function ot(d) {
    ve.call(this, e, d);
  }
  function st(d) {
    ve.call(this, e, d);
  }
  function Ht(d) {
    ve.call(this, e, d);
  }
  function Bt() {
    n(16, v = gr.innerHeight);
  }
  const S = () => n(0, m = null), yr = (d) => Z(d);
  function Er(d, ze) {
    li[d ? "unshift" : "push"](() => {
      W[ze] = d, n(13, W);
    });
  }
  const Sr = (d) => n(0, m = d);
  function Tr(d) {
    li[d ? "unshift" : "push"](() => {
      q = d, n(14, q);
    });
  }
  function Ar(d) {
    ve.call(this, e, d);
  }
  function Hr(d) {
    ve.call(this, e, d);
  }
  const Br = (d) => n(0, m = d);
  function Cr() {
    ee = this.clientHeight, n(15, ee);
  }
  return e.$$set = (d) => {
    "show_label" in d && n(1, l = d.show_label), "label" in d && n(2, o = d.label), "root" in d && n(19, a = d.root), "proxy_url" in d && n(20, s = d.proxy_url), "value" in d && n(3, u = d.value), "columns" in d && n(4, f = d.columns), "rows" in d && n(5, c = d.rows), "height" in d && n(6, h = d.height), "preview" in d && n(21, _ = d.preview), "allow_preview" in d && n(7, b = d.allow_preview), "object_fit" in d && n(8, T = d.object_fit), "show_share_button" in d && n(9, y = d.show_share_button), "show_download_button" in d && n(10, C = d.show_download_button), "i18n" in d && n(11, E = d.i18n), "selected_index" in d && n(0, m = d.selected_index);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*value, was_reset*/
    4194312 && n(22, p = u == null || u.length == 0 ? !0 : p), e.$$.dirty[0] & /*value, root, proxy_url*/
    1572872 && n(12, N = u === null ? null : u.map((d) => ({
      image: Gi(d.image, a, s),
      caption: d.caption
    }))), e.$$.dirty[0] & /*prevValue, value, was_reset, preview, selected_index*/
    14680073 && (Qe(G, u) || (p ? (n(0, m = _ && Ee([u, "optionalAccess", (d) => d.length]) ? 0 : null), n(22, p = !1)) : n(
      0,
      m = m !== null && u !== null && m < u.length ? m : null
    ), g("change"), n(23, G = u))), e.$$.dirty[0] & /*selected_index, _value*/
    4097 && (i = (We(m, () => 0) + We(Ee([N, "optionalAccess", (d) => d.length]), () => 0) - 1) % We(Ee([N, "optionalAccess", (d) => d.length]), () => 0)), e.$$.dirty[0] & /*selected_index, _value*/
    4097 && (r = (We(m, () => 0) + 1) % We(Ee([N, "optionalAccess", (d) => d.length]), () => 0)), e.$$.dirty[0] & /*selected_index, old_selected_index, _value*/
    16781313 && m !== L && (n(24, L = m), m !== null && g("select", {
      index: m,
      value: Ee([N, "optionalAccess", (d) => d[m]])
    })), e.$$.dirty[0] & /*allow_preview, selected_index*/
    129 && b && $(m);
  }, [
    m,
    l,
    o,
    u,
    f,
    c,
    h,
    b,
    T,
    y,
    C,
    E,
    N,
    W,
    q,
    ee,
    v,
    Z,
    K,
    a,
    s,
    _,
    p,
    G,
    L,
    rt,
    At,
    lt,
    ot,
    st,
    Ht,
    Bt,
    S,
    yr,
    Er,
    Sr,
    Tr,
    Ar,
    Hr,
    Br,
    Cr
  ];
}
class bu extends Ka {
  constructor(t) {
    super(), nu(
      this,
      t,
      du,
      _u,
      iu,
      {
        show_label: 1,
        label: 2,
        root: 19,
        proxy_url: 20,
        value: 3,
        columns: 4,
        rows: 5,
        height: 6,
        preview: 21,
        allow_preview: 7,
        object_fit: 8,
        show_share_button: 9,
        show_download_button: 10,
        i18n: 11,
        selected_index: 0
      },
      null,
      [-1, -1]
    );
  }
}
function Ie(e) {
  let t = ["", "k", "M", "G", "T", "P", "E", "Z"], n = 0;
  for (; e > 1e3 && n < t.length - 1; )
    e /= 1e3, n++;
  let i = t[n];
  return (Number.isInteger(e) ? e : e.toFixed(1)) + i;
}
const {
  SvelteComponent: gu,
  append: ie,
  attr: I,
  component_subscribe: bi,
  detach: pu,
  element: vu,
  init: wu,
  insert: yu,
  noop: gi,
  safe_not_equal: Eu,
  set_style: ht,
  svg_element: re,
  toggle_class: pi
} = window.__gradio__svelte__internal, { onMount: Su } = window.__gradio__svelte__internal;
function Tu(e) {
  let t, n, i, r, l, o, a, s, u, f, c, h;
  return {
    c() {
      t = vu("div"), n = re("svg"), i = re("g"), r = re("path"), l = re("path"), o = re("path"), a = re("path"), s = re("g"), u = re("path"), f = re("path"), c = re("path"), h = re("path"), I(r, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), I(r, "fill", "#FF7C00"), I(r, "fill-opacity", "0.4"), I(r, "class", "svelte-43sxxs"), I(l, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), I(l, "fill", "#FF7C00"), I(l, "class", "svelte-43sxxs"), I(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), I(o, "fill", "#FF7C00"), I(o, "fill-opacity", "0.4"), I(o, "class", "svelte-43sxxs"), I(a, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), I(a, "fill", "#FF7C00"), I(a, "class", "svelte-43sxxs"), ht(i, "transform", "translate(" + /*$top*/
      e[1][0] + "px, " + /*$top*/
      e[1][1] + "px)"), I(u, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), I(u, "fill", "#FF7C00"), I(u, "fill-opacity", "0.4"), I(u, "class", "svelte-43sxxs"), I(f, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), I(f, "fill", "#FF7C00"), I(f, "class", "svelte-43sxxs"), I(c, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), I(c, "fill", "#FF7C00"), I(c, "fill-opacity", "0.4"), I(c, "class", "svelte-43sxxs"), I(h, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), I(h, "fill", "#FF7C00"), I(h, "class", "svelte-43sxxs"), ht(s, "transform", "translate(" + /*$bottom*/
      e[2][0] + "px, " + /*$bottom*/
      e[2][1] + "px)"), I(n, "viewBox", "-1200 -1200 3000 3000"), I(n, "fill", "none"), I(n, "xmlns", "http://www.w3.org/2000/svg"), I(n, "class", "svelte-43sxxs"), I(t, "class", "svelte-43sxxs"), pi(
        t,
        "margin",
        /*margin*/
        e[0]
      );
    },
    m(_, b) {
      yu(_, t, b), ie(t, n), ie(n, i), ie(i, r), ie(i, l), ie(i, o), ie(i, a), ie(n, s), ie(s, u), ie(s, f), ie(s, c), ie(s, h);
    },
    p(_, [b]) {
      b & /*$top*/
      2 && ht(i, "transform", "translate(" + /*$top*/
      _[1][0] + "px, " + /*$top*/
      _[1][1] + "px)"), b & /*$bottom*/
      4 && ht(s, "transform", "translate(" + /*$bottom*/
      _[2][0] + "px, " + /*$bottom*/
      _[2][1] + "px)"), b & /*margin*/
      1 && pi(
        t,
        "margin",
        /*margin*/
        _[0]
      );
    },
    i: gi,
    o: gi,
    d(_) {
      _ && pu(t);
    }
  };
}
function Au(e, t, n) {
  let i, r, { margin: l = !0 } = t;
  const o = Mn([0, 0]);
  bi(e, o, (h) => n(1, i = h));
  const a = Mn([0, 0]);
  bi(e, a, (h) => n(2, r = h));
  let s;
  async function u() {
    await Promise.all([o.set([125, 140]), a.set([-125, -140])]), await Promise.all([o.set([-125, 140]), a.set([125, -140])]), await Promise.all([o.set([-125, 0]), a.set([125, -0])]), await Promise.all([o.set([125, 0]), a.set([-125, 0])]);
  }
  async function f() {
    await u(), s || f();
  }
  async function c() {
    await Promise.all([o.set([125, 0]), a.set([-125, 0])]), f();
  }
  return Su(() => (c(), () => s = !0)), e.$$set = (h) => {
    "margin" in h && n(0, l = h.margin);
  }, [l, i, r, o, a];
}
class Hu extends gu {
  constructor(t) {
    super(), wu(this, t, Au, Tu, Eu, { margin: 0 });
  }
}
const {
  SvelteComponent: Bu,
  append: Ae,
  attr: fe,
  binding_callbacks: vi,
  check_outros: pr,
  create_component: Cu,
  create_slot: Pu,
  destroy_component: Iu,
  destroy_each: vr,
  detach: A,
  element: me,
  empty: Ve,
  ensure_array_like: wt,
  get_all_dirty_from_scope: ku,
  get_slot_changes: Lu,
  group_outros: wr,
  init: Nu,
  insert: H,
  mount_component: Ou,
  noop: un,
  safe_not_equal: Mu,
  set_data: Y,
  set_style: ye,
  space: ce,
  text: M,
  toggle_class: J,
  transition_in: Re,
  transition_out: De,
  update_slot_base: Ru
} = window.__gradio__svelte__internal, { tick: Du } = window.__gradio__svelte__internal, { onDestroy: Uu } = window.__gradio__svelte__internal, Gu = (e) => ({}), wi = (e) => ({});
function yi(e, t, n) {
  const i = e.slice();
  return i[38] = t[n], i[40] = n, i;
}
function Ei(e, t, n) {
  const i = e.slice();
  return i[38] = t[n], i;
}
function Fu(e) {
  let t, n = (
    /*i18n*/
    e[1]("common.error") + ""
  ), i, r, l;
  const o = (
    /*#slots*/
    e[29].error
  ), a = Pu(
    o,
    e,
    /*$$scope*/
    e[28],
    wi
  );
  return {
    c() {
      t = me("span"), i = M(n), r = ce(), a && a.c(), fe(t, "class", "error svelte-14miwb5");
    },
    m(s, u) {
      H(s, t, u), Ae(t, i), H(s, r, u), a && a.m(s, u), l = !0;
    },
    p(s, u) {
      (!l || u[0] & /*i18n*/
      2) && n !== (n = /*i18n*/
      s[1]("common.error") + "") && Y(i, n), a && a.p && (!l || u[0] & /*$$scope*/
      268435456) && Ru(
        a,
        o,
        s,
        /*$$scope*/
        s[28],
        l ? Lu(
          o,
          /*$$scope*/
          s[28],
          u,
          Gu
        ) : ku(
          /*$$scope*/
          s[28]
        ),
        wi
      );
    },
    i(s) {
      l || (Re(a, s), l = !0);
    },
    o(s) {
      De(a, s), l = !1;
    },
    d(s) {
      s && (A(t), A(r)), a && a.d(s);
    }
  };
}
function xu(e) {
  let t, n, i, r, l, o, a, s, u, f = (
    /*variant*/
    e[8] === "default" && /*show_eta_bar*/
    e[18] && /*show_progress*/
    e[6] === "full" && Si(e)
  );
  function c(m, g) {
    if (
      /*progress*/
      m[7]
    )
      return zu;
    if (
      /*queue_position*/
      m[2] !== null && /*queue_size*/
      m[3] !== void 0 && /*queue_position*/
      m[2] >= 0
    )
      return Vu;
    if (
      /*queue_position*/
      m[2] === 0
    )
      return ju;
  }
  let h = c(e), _ = h && h(e), b = (
    /*timer*/
    e[5] && Hi(e)
  );
  const T = [Wu, Zu], y = [];
  function C(m, g) {
    return (
      /*last_progress_level*/
      m[15] != null ? 0 : (
        /*show_progress*/
        m[6] === "full" ? 1 : -1
      )
    );
  }
  ~(l = C(e)) && (o = y[l] = T[l](e));
  let E = !/*timer*/
  e[5] && Ni(e);
  return {
    c() {
      f && f.c(), t = ce(), n = me("div"), _ && _.c(), i = ce(), b && b.c(), r = ce(), o && o.c(), a = ce(), E && E.c(), s = Ve(), fe(n, "class", "progress-text svelte-14miwb5"), J(
        n,
        "meta-text-center",
        /*variant*/
        e[8] === "center"
      ), J(
        n,
        "meta-text",
        /*variant*/
        e[8] === "default"
      );
    },
    m(m, g) {
      f && f.m(m, g), H(m, t, g), H(m, n, g), _ && _.m(n, null), Ae(n, i), b && b.m(n, null), H(m, r, g), ~l && y[l].m(m, g), H(m, a, g), E && E.m(m, g), H(m, s, g), u = !0;
    },
    p(m, g) {
      /*variant*/
      m[8] === "default" && /*show_eta_bar*/
      m[18] && /*show_progress*/
      m[6] === "full" ? f ? f.p(m, g) : (f = Si(m), f.c(), f.m(t.parentNode, t)) : f && (f.d(1), f = null), h === (h = c(m)) && _ ? _.p(m, g) : (_ && _.d(1), _ = h && h(m), _ && (_.c(), _.m(n, i))), /*timer*/
      m[5] ? b ? b.p(m, g) : (b = Hi(m), b.c(), b.m(n, null)) : b && (b.d(1), b = null), (!u || g[0] & /*variant*/
      256) && J(
        n,
        "meta-text-center",
        /*variant*/
        m[8] === "center"
      ), (!u || g[0] & /*variant*/
      256) && J(
        n,
        "meta-text",
        /*variant*/
        m[8] === "default"
      );
      let p = l;
      l = C(m), l === p ? ~l && y[l].p(m, g) : (o && (wr(), De(y[p], 1, 1, () => {
        y[p] = null;
      }), pr()), ~l ? (o = y[l], o ? o.p(m, g) : (o = y[l] = T[l](m), o.c()), Re(o, 1), o.m(a.parentNode, a)) : o = null), /*timer*/
      m[5] ? E && (E.d(1), E = null) : E ? E.p(m, g) : (E = Ni(m), E.c(), E.m(s.parentNode, s));
    },
    i(m) {
      u || (Re(o), u = !0);
    },
    o(m) {
      De(o), u = !1;
    },
    d(m) {
      m && (A(t), A(n), A(r), A(a), A(s)), f && f.d(m), _ && _.d(), b && b.d(), ~l && y[l].d(m), E && E.d(m);
    }
  };
}
function Si(e) {
  let t, n = `translateX(${/*eta_level*/
  (e[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      t = me("div"), fe(t, "class", "eta-bar svelte-14miwb5"), ye(t, "transform", n);
    },
    m(i, r) {
      H(i, t, r);
    },
    p(i, r) {
      r[0] & /*eta_level*/
      131072 && n !== (n = `translateX(${/*eta_level*/
      (i[17] || 0) * 100 - 100}%)`) && ye(t, "transform", n);
    },
    d(i) {
      i && A(t);
    }
  };
}
function ju(e) {
  let t;
  return {
    c() {
      t = M("processing |");
    },
    m(n, i) {
      H(n, t, i);
    },
    p: un,
    d(n) {
      n && A(t);
    }
  };
}
function Vu(e) {
  let t, n = (
    /*queue_position*/
    e[2] + 1 + ""
  ), i, r, l, o;
  return {
    c() {
      t = M("queue: "), i = M(n), r = M("/"), l = M(
        /*queue_size*/
        e[3]
      ), o = M(" |");
    },
    m(a, s) {
      H(a, t, s), H(a, i, s), H(a, r, s), H(a, l, s), H(a, o, s);
    },
    p(a, s) {
      s[0] & /*queue_position*/
      4 && n !== (n = /*queue_position*/
      a[2] + 1 + "") && Y(i, n), s[0] & /*queue_size*/
      8 && Y(
        l,
        /*queue_size*/
        a[3]
      );
    },
    d(a) {
      a && (A(t), A(i), A(r), A(l), A(o));
    }
  };
}
function zu(e) {
  let t, n = wt(
    /*progress*/
    e[7]
  ), i = [];
  for (let r = 0; r < n.length; r += 1)
    i[r] = Ai(Ei(e, n, r));
  return {
    c() {
      for (let r = 0; r < i.length; r += 1)
        i[r].c();
      t = Ve();
    },
    m(r, l) {
      for (let o = 0; o < i.length; o += 1)
        i[o] && i[o].m(r, l);
      H(r, t, l);
    },
    p(r, l) {
      if (l[0] & /*progress*/
      128) {
        n = wt(
          /*progress*/
          r[7]
        );
        let o;
        for (o = 0; o < n.length; o += 1) {
          const a = Ei(r, n, o);
          i[o] ? i[o].p(a, l) : (i[o] = Ai(a), i[o].c(), i[o].m(t.parentNode, t));
        }
        for (; o < i.length; o += 1)
          i[o].d(1);
        i.length = n.length;
      }
    },
    d(r) {
      r && A(t), vr(i, r);
    }
  };
}
function Ti(e) {
  let t, n = (
    /*p*/
    e[38].unit + ""
  ), i, r, l = " ", o;
  function a(f, c) {
    return (
      /*p*/
      f[38].length != null ? Xu : qu
    );
  }
  let s = a(e), u = s(e);
  return {
    c() {
      u.c(), t = ce(), i = M(n), r = M(" | "), o = M(l);
    },
    m(f, c) {
      u.m(f, c), H(f, t, c), H(f, i, c), H(f, r, c), H(f, o, c);
    },
    p(f, c) {
      s === (s = a(f)) && u ? u.p(f, c) : (u.d(1), u = s(f), u && (u.c(), u.m(t.parentNode, t))), c[0] & /*progress*/
      128 && n !== (n = /*p*/
      f[38].unit + "") && Y(i, n);
    },
    d(f) {
      f && (A(t), A(i), A(r), A(o)), u.d(f);
    }
  };
}
function qu(e) {
  let t = Ie(
    /*p*/
    e[38].index || 0
  ) + "", n;
  return {
    c() {
      n = M(t);
    },
    m(i, r) {
      H(i, n, r);
    },
    p(i, r) {
      r[0] & /*progress*/
      128 && t !== (t = Ie(
        /*p*/
        i[38].index || 0
      ) + "") && Y(n, t);
    },
    d(i) {
      i && A(n);
    }
  };
}
function Xu(e) {
  let t = Ie(
    /*p*/
    e[38].index || 0
  ) + "", n, i, r = Ie(
    /*p*/
    e[38].length
  ) + "", l;
  return {
    c() {
      n = M(t), i = M("/"), l = M(r);
    },
    m(o, a) {
      H(o, n, a), H(o, i, a), H(o, l, a);
    },
    p(o, a) {
      a[0] & /*progress*/
      128 && t !== (t = Ie(
        /*p*/
        o[38].index || 0
      ) + "") && Y(n, t), a[0] & /*progress*/
      128 && r !== (r = Ie(
        /*p*/
        o[38].length
      ) + "") && Y(l, r);
    },
    d(o) {
      o && (A(n), A(i), A(l));
    }
  };
}
function Ai(e) {
  let t, n = (
    /*p*/
    e[38].index != null && Ti(e)
  );
  return {
    c() {
      n && n.c(), t = Ve();
    },
    m(i, r) {
      n && n.m(i, r), H(i, t, r);
    },
    p(i, r) {
      /*p*/
      i[38].index != null ? n ? n.p(i, r) : (n = Ti(i), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(i) {
      i && A(t), n && n.d(i);
    }
  };
}
function Hi(e) {
  let t, n = (
    /*eta*/
    e[0] ? `/${/*formatted_eta*/
    e[19]}` : ""
  ), i, r;
  return {
    c() {
      t = M(
        /*formatted_timer*/
        e[20]
      ), i = M(n), r = M("s");
    },
    m(l, o) {
      H(l, t, o), H(l, i, o), H(l, r, o);
    },
    p(l, o) {
      o[0] & /*formatted_timer*/
      1048576 && Y(
        t,
        /*formatted_timer*/
        l[20]
      ), o[0] & /*eta, formatted_eta*/
      524289 && n !== (n = /*eta*/
      l[0] ? `/${/*formatted_eta*/
      l[19]}` : "") && Y(i, n);
    },
    d(l) {
      l && (A(t), A(i), A(r));
    }
  };
}
function Zu(e) {
  let t, n;
  return t = new Hu({
    props: { margin: (
      /*variant*/
      e[8] === "default"
    ) }
  }), {
    c() {
      Cu(t.$$.fragment);
    },
    m(i, r) {
      Ou(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r[0] & /*variant*/
      256 && (l.margin = /*variant*/
      i[8] === "default"), t.$set(l);
    },
    i(i) {
      n || (Re(t.$$.fragment, i), n = !0);
    },
    o(i) {
      De(t.$$.fragment, i), n = !1;
    },
    d(i) {
      Iu(t, i);
    }
  };
}
function Wu(e) {
  let t, n, i, r, l, o = `${/*last_progress_level*/
  e[15] * 100}%`, a = (
    /*progress*/
    e[7] != null && Bi(e)
  );
  return {
    c() {
      t = me("div"), n = me("div"), a && a.c(), i = ce(), r = me("div"), l = me("div"), fe(n, "class", "progress-level-inner svelte-14miwb5"), fe(l, "class", "progress-bar svelte-14miwb5"), ye(l, "width", o), fe(r, "class", "progress-bar-wrap svelte-14miwb5"), fe(t, "class", "progress-level svelte-14miwb5");
    },
    m(s, u) {
      H(s, t, u), Ae(t, n), a && a.m(n, null), Ae(t, i), Ae(t, r), Ae(r, l), e[30](l);
    },
    p(s, u) {
      /*progress*/
      s[7] != null ? a ? a.p(s, u) : (a = Bi(s), a.c(), a.m(n, null)) : a && (a.d(1), a = null), u[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      s[15] * 100}%`) && ye(l, "width", o);
    },
    i: un,
    o: un,
    d(s) {
      s && A(t), a && a.d(), e[30](null);
    }
  };
}
function Bi(e) {
  let t, n = wt(
    /*progress*/
    e[7]
  ), i = [];
  for (let r = 0; r < n.length; r += 1)
    i[r] = Li(yi(e, n, r));
  return {
    c() {
      for (let r = 0; r < i.length; r += 1)
        i[r].c();
      t = Ve();
    },
    m(r, l) {
      for (let o = 0; o < i.length; o += 1)
        i[o] && i[o].m(r, l);
      H(r, t, l);
    },
    p(r, l) {
      if (l[0] & /*progress_level, progress*/
      16512) {
        n = wt(
          /*progress*/
          r[7]
        );
        let o;
        for (o = 0; o < n.length; o += 1) {
          const a = yi(r, n, o);
          i[o] ? i[o].p(a, l) : (i[o] = Li(a), i[o].c(), i[o].m(t.parentNode, t));
        }
        for (; o < i.length; o += 1)
          i[o].d(1);
        i.length = n.length;
      }
    },
    d(r) {
      r && A(t), vr(i, r);
    }
  };
}
function Ci(e) {
  let t, n, i, r, l = (
    /*i*/
    e[40] !== 0 && Qu()
  ), o = (
    /*p*/
    e[38].desc != null && Pi(e)
  ), a = (
    /*p*/
    e[38].desc != null && /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null && Ii()
  ), s = (
    /*progress_level*/
    e[14] != null && ki(e)
  );
  return {
    c() {
      l && l.c(), t = ce(), o && o.c(), n = ce(), a && a.c(), i = ce(), s && s.c(), r = Ve();
    },
    m(u, f) {
      l && l.m(u, f), H(u, t, f), o && o.m(u, f), H(u, n, f), a && a.m(u, f), H(u, i, f), s && s.m(u, f), H(u, r, f);
    },
    p(u, f) {
      /*p*/
      u[38].desc != null ? o ? o.p(u, f) : (o = Pi(u), o.c(), o.m(n.parentNode, n)) : o && (o.d(1), o = null), /*p*/
      u[38].desc != null && /*progress_level*/
      u[14] && /*progress_level*/
      u[14][
        /*i*/
        u[40]
      ] != null ? a || (a = Ii(), a.c(), a.m(i.parentNode, i)) : a && (a.d(1), a = null), /*progress_level*/
      u[14] != null ? s ? s.p(u, f) : (s = ki(u), s.c(), s.m(r.parentNode, r)) : s && (s.d(1), s = null);
    },
    d(u) {
      u && (A(t), A(n), A(i), A(r)), l && l.d(u), o && o.d(u), a && a.d(u), s && s.d(u);
    }
  };
}
function Qu(e) {
  let t;
  return {
    c() {
      t = M(" /");
    },
    m(n, i) {
      H(n, t, i);
    },
    d(n) {
      n && A(t);
    }
  };
}
function Pi(e) {
  let t = (
    /*p*/
    e[38].desc + ""
  ), n;
  return {
    c() {
      n = M(t);
    },
    m(i, r) {
      H(i, n, r);
    },
    p(i, r) {
      r[0] & /*progress*/
      128 && t !== (t = /*p*/
      i[38].desc + "") && Y(n, t);
    },
    d(i) {
      i && A(n);
    }
  };
}
function Ii(e) {
  let t;
  return {
    c() {
      t = M("-");
    },
    m(n, i) {
      H(n, t, i);
    },
    d(n) {
      n && A(t);
    }
  };
}
function ki(e) {
  let t = (100 * /*progress_level*/
  (e[14][
    /*i*/
    e[40]
  ] || 0)).toFixed(1) + "", n, i;
  return {
    c() {
      n = M(t), i = M("%");
    },
    m(r, l) {
      H(r, n, l), H(r, i, l);
    },
    p(r, l) {
      l[0] & /*progress_level*/
      16384 && t !== (t = (100 * /*progress_level*/
      (r[14][
        /*i*/
        r[40]
      ] || 0)).toFixed(1) + "") && Y(n, t);
    },
    d(r) {
      r && (A(n), A(i));
    }
  };
}
function Li(e) {
  let t, n = (
    /*p*/
    (e[38].desc != null || /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null) && Ci(e)
  );
  return {
    c() {
      n && n.c(), t = Ve();
    },
    m(i, r) {
      n && n.m(i, r), H(i, t, r);
    },
    p(i, r) {
      /*p*/
      i[38].desc != null || /*progress_level*/
      i[14] && /*progress_level*/
      i[14][
        /*i*/
        i[40]
      ] != null ? n ? n.p(i, r) : (n = Ci(i), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(i) {
      i && A(t), n && n.d(i);
    }
  };
}
function Ni(e) {
  let t, n;
  return {
    c() {
      t = me("p"), n = M(
        /*loading_text*/
        e[9]
      ), fe(t, "class", "loading svelte-14miwb5");
    },
    m(i, r) {
      H(i, t, r), Ae(t, n);
    },
    p(i, r) {
      r[0] & /*loading_text*/
      512 && Y(
        n,
        /*loading_text*/
        i[9]
      );
    },
    d(i) {
      i && A(t);
    }
  };
}
function Ju(e) {
  let t, n, i, r, l;
  const o = [xu, Fu], a = [];
  function s(u, f) {
    return (
      /*status*/
      u[4] === "pending" ? 0 : (
        /*status*/
        u[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(n = s(e)) && (i = a[n] = o[n](e)), {
    c() {
      t = me("div"), i && i.c(), fe(t, "class", r = "wrap " + /*variant*/
      e[8] + " " + /*show_progress*/
      e[6] + " svelte-14miwb5"), J(t, "hide", !/*status*/
      e[4] || /*status*/
      e[4] === "complete" || /*show_progress*/
      e[6] === "hidden"), J(
        t,
        "translucent",
        /*variant*/
        e[8] === "center" && /*status*/
        (e[4] === "pending" || /*status*/
        e[4] === "error") || /*translucent*/
        e[11] || /*show_progress*/
        e[6] === "minimal"
      ), J(
        t,
        "generating",
        /*status*/
        e[4] === "generating"
      ), J(
        t,
        "border",
        /*border*/
        e[12]
      ), ye(
        t,
        "position",
        /*absolute*/
        e[10] ? "absolute" : "static"
      ), ye(
        t,
        "padding",
        /*absolute*/
        e[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(u, f) {
      H(u, t, f), ~n && a[n].m(t, null), e[31](t), l = !0;
    },
    p(u, f) {
      let c = n;
      n = s(u), n === c ? ~n && a[n].p(u, f) : (i && (wr(), De(a[c], 1, 1, () => {
        a[c] = null;
      }), pr()), ~n ? (i = a[n], i ? i.p(u, f) : (i = a[n] = o[n](u), i.c()), Re(i, 1), i.m(t, null)) : i = null), (!l || f[0] & /*variant, show_progress*/
      320 && r !== (r = "wrap " + /*variant*/
      u[8] + " " + /*show_progress*/
      u[6] + " svelte-14miwb5")) && fe(t, "class", r), (!l || f[0] & /*variant, show_progress, status, show_progress*/
      336) && J(t, "hide", !/*status*/
      u[4] || /*status*/
      u[4] === "complete" || /*show_progress*/
      u[6] === "hidden"), (!l || f[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && J(
        t,
        "translucent",
        /*variant*/
        u[8] === "center" && /*status*/
        (u[4] === "pending" || /*status*/
        u[4] === "error") || /*translucent*/
        u[11] || /*show_progress*/
        u[6] === "minimal"
      ), (!l || f[0] & /*variant, show_progress, status*/
      336) && J(
        t,
        "generating",
        /*status*/
        u[4] === "generating"
      ), (!l || f[0] & /*variant, show_progress, border*/
      4416) && J(
        t,
        "border",
        /*border*/
        u[12]
      ), f[0] & /*absolute*/
      1024 && ye(
        t,
        "position",
        /*absolute*/
        u[10] ? "absolute" : "static"
      ), f[0] & /*absolute*/
      1024 && ye(
        t,
        "padding",
        /*absolute*/
        u[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(u) {
      l || (Re(i), l = !0);
    },
    o(u) {
      De(i), l = !1;
    },
    d(u) {
      u && A(t), ~n && a[n].d(), e[31](null);
    }
  };
}
let _t = [], Wt = !1;
async function Yu(e, t = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
    if (_t.push(e), !Wt)
      Wt = !0;
    else
      return;
    await Du(), requestAnimationFrame(() => {
      let n = [0, 0];
      for (let i = 0; i < _t.length; i++) {
        const l = _t[i].getBoundingClientRect();
        (i === 0 || l.top + window.scrollY <= n[0]) && (n[0] = l.top + window.scrollY, n[1] = i);
      }
      window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), Wt = !1, _t = [];
    });
  }
}
function Ku(e, t, n) {
  let i, { $$slots: r = {}, $$scope: l } = t, { i18n: o } = t, { eta: a = null } = t, { queue: s = !1 } = t, { queue_position: u } = t, { queue_size: f } = t, { status: c } = t, { scroll_to_output: h = !1 } = t, { timer: _ = !0 } = t, { show_progress: b = "full" } = t, { message: T = null } = t, { progress: y = null } = t, { variant: C = "default" } = t, { loading_text: E = "Loading..." } = t, { absolute: m = !0 } = t, { translucent: g = !1 } = t, { border: p = !1 } = t, { autoscroll: N } = t, G, L = !1, Z = 0, K = 0, W = null, q = 0, $ = null, ee, v = null, rt = !0;
  const At = () => {
    n(25, Z = performance.now()), n(26, K = 0), L = !0, lt();
  };
  function lt() {
    requestAnimationFrame(() => {
      n(26, K = (performance.now() - Z) / 1e3), L && lt();
    });
  }
  function ot() {
    n(26, K = 0), L && (L = !1);
  }
  Uu(() => {
    L && ot();
  });
  let st = null;
  function Ht(S) {
    vi[S ? "unshift" : "push"](() => {
      v = S, n(16, v), n(7, y), n(14, $), n(15, ee);
    });
  }
  function Bt(S) {
    vi[S ? "unshift" : "push"](() => {
      G = S, n(13, G);
    });
  }
  return e.$$set = (S) => {
    "i18n" in S && n(1, o = S.i18n), "eta" in S && n(0, a = S.eta), "queue" in S && n(21, s = S.queue), "queue_position" in S && n(2, u = S.queue_position), "queue_size" in S && n(3, f = S.queue_size), "status" in S && n(4, c = S.status), "scroll_to_output" in S && n(22, h = S.scroll_to_output), "timer" in S && n(5, _ = S.timer), "show_progress" in S && n(6, b = S.show_progress), "message" in S && n(23, T = S.message), "progress" in S && n(7, y = S.progress), "variant" in S && n(8, C = S.variant), "loading_text" in S && n(9, E = S.loading_text), "absolute" in S && n(10, m = S.absolute), "translucent" in S && n(11, g = S.translucent), "border" in S && n(12, p = S.border), "autoscroll" in S && n(24, N = S.autoscroll), "$$scope" in S && n(28, l = S.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*eta, old_eta, queue, timer_start*/
    169869313 && (a === null ? n(0, a = W) : s && n(0, a = (performance.now() - Z) / 1e3 + a), a != null && (n(19, st = a.toFixed(1)), n(27, W = a))), e.$$.dirty[0] & /*eta, timer_diff*/
    67108865 && n(17, q = a === null || a <= 0 || !K ? null : Math.min(K / a, 1)), e.$$.dirty[0] & /*progress*/
    128 && y != null && n(18, rt = !1), e.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (y != null ? n(14, $ = y.map((S) => {
      if (S.index != null && S.length != null)
        return S.index / S.length;
      if (S.progress != null)
        return S.progress;
    })) : n(14, $ = null), $ ? (n(15, ee = $[$.length - 1]), v && (ee === 0 ? n(16, v.style.transition = "0", v) : n(16, v.style.transition = "150ms", v))) : n(15, ee = void 0)), e.$$.dirty[0] & /*status*/
    16 && (c === "pending" ? At() : ot()), e.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && G && h && (c === "pending" || c === "complete") && Yu(G, N), e.$$.dirty[0] & /*status, message*/
    8388624, e.$$.dirty[0] & /*timer_diff*/
    67108864 && n(20, i = K.toFixed(1));
  }, [
    a,
    o,
    u,
    f,
    c,
    _,
    b,
    y,
    C,
    E,
    m,
    g,
    p,
    G,
    $,
    ee,
    v,
    q,
    rt,
    st,
    i,
    s,
    h,
    T,
    N,
    Z,
    K,
    W,
    l,
    r,
    Ht,
    Bt
  ];
}
class $u extends Bu {
  constructor(t) {
    super(), Nu(
      this,
      t,
      Ku,
      Ju,
      Mu,
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
const {
  SvelteComponent: ef,
  add_flush_callback: tf,
  assign: nf,
  bind: rf,
  binding_callbacks: lf,
  create_component: fn,
  destroy_component: cn,
  detach: of,
  get_spread_object: sf,
  get_spread_update: af,
  init: uf,
  insert: ff,
  mount_component: hn,
  safe_not_equal: cf,
  space: hf,
  transition_in: _n,
  transition_out: mn
} = window.__gradio__svelte__internal, { createEventDispatcher: _f } = window.__gradio__svelte__internal;
function mf(e) {
  let t, n, i, r, l;
  const o = [
    {
      autoscroll: (
        /*gradio*/
        e[21].autoscroll
      )
    },
    { i18n: (
      /*gradio*/
      e[21].i18n
    ) },
    /*loading_status*/
    e[1]
  ];
  let a = {};
  for (let f = 0; f < o.length; f += 1)
    a = nf(a, o[f]);
  t = new $u({ props: a });
  function s(f) {
    e[22](f);
  }
  let u = {
    label: (
      /*label*/
      e[3]
    ),
    value: (
      /*value*/
      e[9]
    ),
    show_label: (
      /*show_label*/
      e[2]
    ),
    root: (
      /*root*/
      e[4]
    ),
    proxy_url: (
      /*proxy_url*/
      e[5]
    ),
    columns: (
      /*columns*/
      e[13]
    ),
    rows: (
      /*rows*/
      e[14]
    ),
    height: (
      /*height*/
      e[15]
    ),
    preview: (
      /*preview*/
      e[16]
    ),
    object_fit: (
      /*object_fit*/
      e[18]
    ),
    allow_preview: (
      /*allow_preview*/
      e[17]
    ),
    show_share_button: (
      /*show_share_button*/
      e[19]
    ),
    show_download_button: (
      /*show_download_button*/
      e[20]
    ),
    i18n: (
      /*gradio*/
      e[21].i18n
    )
  };
  return (
    /*selected_index*/
    e[0] !== void 0 && (u.selected_index = /*selected_index*/
    e[0]), i = new bu({ props: u }), lf.push(() => rf(i, "selected_index", s)), i.$on(
      "change",
      /*change_handler*/
      e[23]
    ), i.$on(
      "select",
      /*select_handler*/
      e[24]
    ), i.$on(
      "share",
      /*share_handler*/
      e[25]
    ), i.$on(
      "error",
      /*error_handler*/
      e[26]
    ), {
      c() {
        fn(t.$$.fragment), n = hf(), fn(i.$$.fragment);
      },
      m(f, c) {
        hn(t, f, c), ff(f, n, c), hn(i, f, c), l = !0;
      },
      p(f, c) {
        const h = c & /*gradio, loading_status*/
        2097154 ? af(o, [
          c & /*gradio*/
          2097152 && {
            autoscroll: (
              /*gradio*/
              f[21].autoscroll
            )
          },
          c & /*gradio*/
          2097152 && { i18n: (
            /*gradio*/
            f[21].i18n
          ) },
          c & /*loading_status*/
          2 && sf(
            /*loading_status*/
            f[1]
          )
        ]) : {};
        t.$set(h);
        const _ = {};
        c & /*label*/
        8 && (_.label = /*label*/
        f[3]), c & /*value*/
        512 && (_.value = /*value*/
        f[9]), c & /*show_label*/
        4 && (_.show_label = /*show_label*/
        f[2]), c & /*root*/
        16 && (_.root = /*root*/
        f[4]), c & /*proxy_url*/
        32 && (_.proxy_url = /*proxy_url*/
        f[5]), c & /*columns*/
        8192 && (_.columns = /*columns*/
        f[13]), c & /*rows*/
        16384 && (_.rows = /*rows*/
        f[14]), c & /*height*/
        32768 && (_.height = /*height*/
        f[15]), c & /*preview*/
        65536 && (_.preview = /*preview*/
        f[16]), c & /*object_fit*/
        262144 && (_.object_fit = /*object_fit*/
        f[18]), c & /*allow_preview*/
        131072 && (_.allow_preview = /*allow_preview*/
        f[17]), c & /*show_share_button*/
        524288 && (_.show_share_button = /*show_share_button*/
        f[19]), c & /*show_download_button*/
        1048576 && (_.show_download_button = /*show_download_button*/
        f[20]), c & /*gradio*/
        2097152 && (_.i18n = /*gradio*/
        f[21].i18n), !r && c & /*selected_index*/
        1 && (r = !0, _.selected_index = /*selected_index*/
        f[0], tf(() => r = !1)), i.$set(_);
      },
      i(f) {
        l || (_n(t.$$.fragment, f), _n(i.$$.fragment, f), l = !0);
      },
      o(f) {
        mn(t.$$.fragment, f), mn(i.$$.fragment, f), l = !1;
      },
      d(f) {
        f && of(n), cn(t, f), cn(i, f);
      }
    }
  );
}
function df(e) {
  let t, n;
  return t = new zr({
    props: {
      visible: (
        /*visible*/
        e[8]
      ),
      variant: "solid",
      padding: !1,
      elem_id: (
        /*elem_id*/
        e[6]
      ),
      elem_classes: (
        /*elem_classes*/
        e[7]
      ),
      container: (
        /*container*/
        e[10]
      ),
      scale: (
        /*scale*/
        e[11]
      ),
      min_width: (
        /*min_width*/
        e[12]
      ),
      allow_overflow: !1,
      height: typeof /*height*/
      e[15] == "number" ? (
        /*height*/
        e[15]
      ) : void 0,
      $$slots: { default: [mf] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      fn(t.$$.fragment);
    },
    m(i, r) {
      hn(t, i, r), n = !0;
    },
    p(i, [r]) {
      const l = {};
      r & /*visible*/
      256 && (l.visible = /*visible*/
      i[8]), r & /*elem_id*/
      64 && (l.elem_id = /*elem_id*/
      i[6]), r & /*elem_classes*/
      128 && (l.elem_classes = /*elem_classes*/
      i[7]), r & /*container*/
      1024 && (l.container = /*container*/
      i[10]), r & /*scale*/
      2048 && (l.scale = /*scale*/
      i[11]), r & /*min_width*/
      4096 && (l.min_width = /*min_width*/
      i[12]), r & /*height*/
      32768 && (l.height = typeof /*height*/
      i[15] == "number" ? (
        /*height*/
        i[15]
      ) : void 0), r & /*$$scope, label, value, show_label, root, proxy_url, columns, rows, height, preview, object_fit, allow_preview, show_share_button, show_download_button, gradio, selected_index, loading_status*/
      272622143 && (l.$$scope = { dirty: r, ctx: i }), t.$set(l);
    },
    i(i) {
      n || (_n(t.$$.fragment, i), n = !0);
    },
    o(i) {
      mn(t.$$.fragment, i), n = !1;
    },
    d(i) {
      cn(t, i);
    }
  };
}
function bf(e, t, n) {
  let { loading_status: i } = t, { show_label: r } = t, { label: l } = t, { root: o } = t, { proxy_url: a } = t, { elem_id: s = "" } = t, { elem_classes: u = [] } = t, { visible: f = !0 } = t, { value: c = null } = t, { container: h = !0 } = t, { scale: _ = null } = t, { min_width: b = void 0 } = t, { columns: T = [2] } = t, { rows: y = void 0 } = t, { height: C = "auto" } = t, { preview: E } = t, { allow_preview: m = !0 } = t, { selected_index: g = null } = t, { object_fit: p = "cover" } = t, { show_share_button: N = !1 } = t, { show_download_button: G = !1 } = t, { gradio: L } = t;
  const Z = _f();
  function K(v) {
    g = v, n(0, g);
  }
  const W = () => L.dispatch("change", c), q = (v) => L.dispatch("select", v.detail), $ = (v) => L.dispatch("share", v.detail), ee = (v) => L.dispatch("error", v.detail);
  return e.$$set = (v) => {
    "loading_status" in v && n(1, i = v.loading_status), "show_label" in v && n(2, r = v.show_label), "label" in v && n(3, l = v.label), "root" in v && n(4, o = v.root), "proxy_url" in v && n(5, a = v.proxy_url), "elem_id" in v && n(6, s = v.elem_id), "elem_classes" in v && n(7, u = v.elem_classes), "visible" in v && n(8, f = v.visible), "value" in v && n(9, c = v.value), "container" in v && n(10, h = v.container), "scale" in v && n(11, _ = v.scale), "min_width" in v && n(12, b = v.min_width), "columns" in v && n(13, T = v.columns), "rows" in v && n(14, y = v.rows), "height" in v && n(15, C = v.height), "preview" in v && n(16, E = v.preview), "allow_preview" in v && n(17, m = v.allow_preview), "selected_index" in v && n(0, g = v.selected_index), "object_fit" in v && n(18, p = v.object_fit), "show_share_button" in v && n(19, N = v.show_share_button), "show_download_button" in v && n(20, G = v.show_download_button), "gradio" in v && n(21, L = v.gradio);
  }, e.$$.update = () => {
    e.$$.dirty & /*selected_index*/
    1 && Z("prop_change", { selected_index: g });
  }, [
    g,
    i,
    r,
    l,
    o,
    a,
    s,
    u,
    f,
    c,
    h,
    _,
    b,
    T,
    y,
    C,
    E,
    m,
    p,
    N,
    G,
    L,
    K,
    W,
    q,
    $,
    ee
  ];
}
class pf extends ef {
  constructor(t) {
    super(), uf(this, t, bf, df, cf, {
      loading_status: 1,
      show_label: 2,
      label: 3,
      root: 4,
      proxy_url: 5,
      elem_id: 6,
      elem_classes: 7,
      visible: 8,
      value: 9,
      container: 10,
      scale: 11,
      min_width: 12,
      columns: 13,
      rows: 14,
      height: 15,
      preview: 16,
      allow_preview: 17,
      selected_index: 0,
      object_fit: 18,
      show_share_button: 19,
      show_download_button: 20,
      gradio: 21
    });
  }
}
export {
  bu as BaseGallery,
  pf as default
};
