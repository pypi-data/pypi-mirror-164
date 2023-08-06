import { ae as ordered_colors } from './index.a3972c49.js';

const get_next_color = (index) => {
  return ordered_colors[index % ordered_colors.length];
};

export { get_next_color as g };
