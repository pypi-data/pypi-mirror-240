/* Routine optimized for shuffling a buffer for a type size of 16 bytes. */
void shuffle16_neon(uint8_t* const dest, const uint8_t* const src,
               const size_t vectorizable_elements, const size_t total_elements)
{
  size_t i, j, k;
  static const size_t bytesoftype = 16;
  uint8x8x2_t r0[8];
  uint16x4x2_t r1[8];
  uint32x2x2_t r2[8];

  for(i = 0, k = 0; i < vectorizable_elements*bytesoftype; i += 128, k++) {
    /* Load and interleave groups of 16 bytes (128 bytes) to the structure r0 */
    r0[0] = vzip_u8(vld1_u8(src + i + 0*8), vld1_u8(src + i + 2*8));
    r0[1] = vzip_u8(vld1_u8(src + i + 1*8), vld1_u8(src + i + 3*8));
    r0[2] = vzip_u8(vld1_u8(src + i + 4*8), vld1_u8(src + i + 6*8));
    r0[3] = vzip_u8(vld1_u8(src + i + 5*8), vld1_u8(src + i + 7*8));
    r0[4] = vzip_u8(vld1_u8(src + i + 8*8), vld1_u8(src + i + 10*8));
    r0[5] = vzip_u8(vld1_u8(src + i + 9*8), vld1_u8(src + i + 11*8));
    r0[6] = vzip_u8(vld1_u8(src + i + 12*8), vld1_u8(src + i + 14*8));
    r0[7] = vzip_u8(vld1_u8(src + i + 13*8), vld1_u8(src + i + 15*8));
    /* Interleave 16 bytes */
    r1[0] = vzip_u16(vreinterpret_u16_u8(r0[0].val[0]), vreinterpret_u16_u8(r0[2].val[0]));
    r1[1] = vzip_u16(vreinterpret_u16_u8(r0[0].val[1]), vreinterpret_u16_u8(r0[2].val[1]));
    r1[2] = vzip_u16(vreinterpret_u16_u8(r0[1].val[0]), vreinterpret_u16_u8(r0[3].val[0]));
    r1[3] = vzip_u16(vreinterpret_u16_u8(r0[1].val[1]), vreinterpret_u16_u8(r0[3].val[1]));
    r1[4] = vzip_u16(vreinterpret_u16_u8(r0[4].val[0]), vreinterpret_u16_u8(r0[6].val[0]));
    r1[5] = vzip_u16(vreinterpret_u16_u8(r0[4].val[1]), vreinterpret_u16_u8(r0[6].val[1]));
    r1[6] = vzip_u16(vreinterpret_u16_u8(r0[5].val[0]), vreinterpret_u16_u8(r0[7].val[0]));
    r1[7] = vzip_u16(vreinterpret_u16_u8(r0[5].val[1]), vreinterpret_u16_u8(r0[7].val[1]));
    /* Interleave 32 bytes */
    r2[0] = vzip_u32(vreinterpret_u32_u16(r1[0].val[0]), vreinterpret_u32_u16(r1[4].val[0]));
    r2[1] = vzip_u32(vreinterpret_u32_u16(r1[0].val[1]), vreinterpret_u32_u16(r1[4].val[1]));
    r2[2] = vzip_u32(vreinterpret_u32_u16(r1[1].val[0]), vreinterpret_u32_u16(r1[5].val[0]));
    r2[3] = vzip_u32(vreinterpret_u32_u16(r1[1].val[1]), vreinterpret_u32_u16(r1[5].val[1]));
    r2[4] = vzip_u32(vreinterpret_u32_u16(r1[2].val[0]), vreinterpret_u32_u16(r1[6].val[0]));
    r2[5] = vzip_u32(vreinterpret_u32_u16(r1[2].val[1]), vreinterpret_u32_u16(r1[6].val[1]));
    r2[6] = vzip_u32(vreinterpret_u32_u16(r1[3].val[0]), vreinterpret_u32_u16(r1[7].val[0]));
    r2[7] = vzip_u32(vreinterpret_u32_u16(r1[3].val[1]), vreinterpret_u32_u16(r1[7].val[1]));
    /* Store the results to the destination vector */
    vst1_u8(dest + k*8 + 0*total_elements, vreinterpret_u8_u32(r2[0].val[0]));
    vst1_u8(dest + k*8 + 1*total_elements, vreinterpret_u8_u32(r2[0].val[1]));
    vst1_u8(dest + k*8 + 2*total_elements, vreinterpret_u8_u32(r2[1].val[0]));
    vst1_u8(dest + k*8 + 3*total_elements, vreinterpret_u8_u32(r2[1].val[1]));
    vst1_u8(dest + k*8 + 4*total_elements, vreinterpret_u8_u32(r2[2].val[0]));
    vst1_u8(dest + k*8 + 5*total_elements, vreinterpret_u8_u32(r2[2].val[1]));
    vst1_u8(dest + k*8 + 6*total_elements, vreinterpret_u8_u32(r2[3].val[0]));
    vst1_u8(dest + k*8 + 7*total_elements, vreinterpret_u8_u32(r2[3].val[1]));
    vst1_u8(dest + k*8 + 8*total_elements, vreinterpret_u8_u32(r2[4].val[0]));
    vst1_u8(dest + k*8 + 9*total_elements, vreinterpret_u8_u32(r2[4].val[1]));
    vst1_u8(dest + k*8 + 10*total_elements, vreinterpret_u8_u32(r2[5].val[0]));
    vst1_u8(dest + k*8 + 11*total_elements, vreinterpret_u8_u32(r2[5].val[1]));
    vst1_u8(dest + k*8 + 12*total_elements, vreinterpret_u8_u32(r2[6].val[0]));
    vst1_u8(dest + k*8 + 13*total_elements, vreinterpret_u8_u32(r2[6].val[1]));
    vst1_u8(dest + k*8 + 14*total_elements, vreinterpret_u8_u32(r2[7].val[0]));
    vst1_u8(dest + k*8 + 15*total_elements, vreinterpret_u8_u32(r2[7].val[1]));
  }
}

