import { S as SvelteComponent, i as init, s as safe_not_equal, f as element, h as text, b as attr, c as insert, d as append, j as set_data, e as detach, V as create_slot, m as space, t as toggle_class, Q as update_slot_base, R as get_all_dirty_from_scope, T as get_slot_changes, v as transition_in, w as transition_out, U as getContext, K as component_subscribe, E as onDestroy, q as create_component, u as mount_component, x as destroy_component } from './index.230aa104.js';
import { a as CAROUSEL } from './CarouselItem.svelte_svelte_type_style_lang.b72f6d83.js';

/* home/runner/work/gradio/gradio/ui/packages/carousel/src/CarouselItem.svelte generated by Svelte v3.49.0 */

function create_if_block(ctx) {
	let div;
	let t;

	return {
		c() {
			div = element("div");
			t = text(/*label*/ ctx[0]);
			attr(div, "class", "absolute left-0 top-0 py-1 px-2 rounded-br-lg shadow-sm text-xs text-gray-500 flex items-center pointer-events-none bg-white z-20 dark:bg-gray-800");
		},
		m(target, anchor) {
			insert(target, div, anchor);
			append(div, t);
		},
		p(ctx, dirty) {
			if (dirty & /*label*/ 1) set_data(t, /*label*/ ctx[0]);
		},
		d(detaching) {
			if (detaching) detach(div);
		}
	};
}

function create_fragment$1(ctx) {
	let div;
	let t;
	let current;
	let if_block = /*label*/ ctx[0] && create_if_block(ctx);
	const default_slot_template = /*#slots*/ ctx[5].default;
	const default_slot = create_slot(default_slot_template, ctx, /*$$scope*/ ctx[4], null);

	return {
		c() {
			div = element("div");
			if (if_block) if_block.c();
			t = space();
			if (default_slot) default_slot.c();
			attr(div, "class", "carousel-item hidden component min-h-[200px] border rounded-lg overflow-hidden relative svelte-89gglt");
			toggle_class(div, "!block", /*$current*/ ctx[1] === /*id*/ ctx[3]);
		},
		m(target, anchor) {
			insert(target, div, anchor);
			if (if_block) if_block.m(div, null);
			append(div, t);

			if (default_slot) {
				default_slot.m(div, null);
			}

			current = true;
		},
		p(ctx, [dirty]) {
			if (/*label*/ ctx[0]) {
				if (if_block) {
					if_block.p(ctx, dirty);
				} else {
					if_block = create_if_block(ctx);
					if_block.c();
					if_block.m(div, t);
				}
			} else if (if_block) {
				if_block.d(1);
				if_block = null;
			}

			if (default_slot) {
				if (default_slot.p && (!current || dirty & /*$$scope*/ 16)) {
					update_slot_base(
						default_slot,
						default_slot_template,
						ctx,
						/*$$scope*/ ctx[4],
						!current
						? get_all_dirty_from_scope(/*$$scope*/ ctx[4])
						: get_slot_changes(default_slot_template, /*$$scope*/ ctx[4], dirty, null),
						null
					);
				}
			}

			if (dirty & /*$current, id*/ 10) {
				toggle_class(div, "!block", /*$current*/ ctx[1] === /*id*/ ctx[3]);
			}
		},
		i(local) {
			if (current) return;
			transition_in(default_slot, local);
			current = true;
		},
		o(local) {
			transition_out(default_slot, local);
			current = false;
		},
		d(detaching) {
			if (detaching) detach(div);
			if (if_block) if_block.d();
			if (default_slot) default_slot.d(detaching);
		}
	};
}

function instance$1($$self, $$props, $$invalidate) {
	let $current;
	let { $$slots: slots = {}, $$scope } = $$props;
	let { label = undefined } = $$props;
	const { register, unregister, current } = getContext(CAROUSEL);
	component_subscribe($$self, current, value => $$invalidate(1, $current = value));
	let id = register();
	onDestroy(() => unregister(id));

	$$self.$$set = $$props => {
		if ('label' in $$props) $$invalidate(0, label = $$props.label);
		if ('$$scope' in $$props) $$invalidate(4, $$scope = $$props.$$scope);
	};

	return [label, $current, current, id, $$scope, slots];
}

class CarouselItem extends SvelteComponent {
	constructor(options) {
		super();
		init(this, options, instance$1, create_fragment$1, safe_not_equal, { label: 0 });
	}
}

/* src/components/CarouselItem/CarouselItem.svelte generated by Svelte v3.49.0 */

function create_default_slot(ctx) {
	let current;
	const default_slot_template = /*#slots*/ ctx[0].default;
	const default_slot = create_slot(default_slot_template, ctx, /*$$scope*/ ctx[1], null);

	return {
		c() {
			if (default_slot) default_slot.c();
		},
		m(target, anchor) {
			if (default_slot) {
				default_slot.m(target, anchor);
			}

			current = true;
		},
		p(ctx, dirty) {
			if (default_slot) {
				if (default_slot.p && (!current || dirty & /*$$scope*/ 2)) {
					update_slot_base(
						default_slot,
						default_slot_template,
						ctx,
						/*$$scope*/ ctx[1],
						!current
						? get_all_dirty_from_scope(/*$$scope*/ ctx[1])
						: get_slot_changes(default_slot_template, /*$$scope*/ ctx[1], dirty, null),
						null
					);
				}
			}
		},
		i(local) {
			if (current) return;
			transition_in(default_slot, local);
			current = true;
		},
		o(local) {
			transition_out(default_slot, local);
			current = false;
		},
		d(detaching) {
			if (default_slot) default_slot.d(detaching);
		}
	};
}

function create_fragment(ctx) {
	let carouselitem;
	let current;

	carouselitem = new CarouselItem({
			props: {
				$$slots: { default: [create_default_slot] },
				$$scope: { ctx }
			}
		});

	return {
		c() {
			create_component(carouselitem.$$.fragment);
		},
		m(target, anchor) {
			mount_component(carouselitem, target, anchor);
			current = true;
		},
		p(ctx, [dirty]) {
			const carouselitem_changes = {};

			if (dirty & /*$$scope*/ 2) {
				carouselitem_changes.$$scope = { dirty, ctx };
			}

			carouselitem.$set(carouselitem_changes);
		},
		i(local) {
			if (current) return;
			transition_in(carouselitem.$$.fragment, local);
			current = true;
		},
		o(local) {
			transition_out(carouselitem.$$.fragment, local);
			current = false;
		},
		d(detaching) {
			destroy_component(carouselitem, detaching);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let { $$slots: slots = {}, $$scope } = $$props;

	$$self.$$set = $$props => {
		if ('$$scope' in $$props) $$invalidate(1, $$scope = $$props.$$scope);
	};

	return [slots, $$scope];
}

class CarouselItem_1 extends SvelteComponent {
	constructor(options) {
		super();
		init(this, options, instance, create_fragment, safe_not_equal, {});
	}
}

var CarouselItem_1$1 = CarouselItem_1;

const modes = ["static"];

export { CarouselItem_1$1 as Component, modes };
