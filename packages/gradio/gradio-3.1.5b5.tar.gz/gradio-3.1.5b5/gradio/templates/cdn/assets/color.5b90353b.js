import { ae as ordered_colors } from './index.f28538c7.js';

const get_next_color = (index) => {
  return ordered_colors[index % ordered_colors.length];
};

export { get_next_color as g };
